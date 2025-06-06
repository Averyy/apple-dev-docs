# Setting Up Push Notifications for Your MDM Customers

**Framework**: Device Management

Create and sign a certificate signing request (CSR) to enable push notifications.

#### Overview

As an MDM vendor, you can use the Apple Push Notification Service (APNs) to create a push certificate and start push notification service for your customers. The process involves creating and then signing a CSR for each customer. This certificate based process is the only way to send push notifications through MDM - MDM doesn’t support the token based push process.

Use a separate push certificate for each customer. This enables independent management of each customer’s certificate and prevents customers from being able to see each other’s device tokens.

##### Create a Csr

During the setup process for your service, create an operation that generates a CSR for your customer. Execute this process within the instance of your MDM service that your customer has access to.

> **Note**:  The private key for this CSR must remain within the instance of your MDM service that the customer has access to. You use this private key to sign the MDM push certificate. Be certain that the MDM service instance doesn’t make this private key available to you (the vendor).

 The private key for this CSR must remain within the instance of your MDM service that the customer has access to. You use this private key to sign the MDM push certificate. Be certain that the MDM service instance doesn’t make this private key available to you (the vendor).

Upload the CSR to your internal infrastructure and then perform the signing process.

##### Sign the Csr

Download an MDM signing certificate and its trust certificates from the iOS provisioning portal. Then create a script to sign the customer’s CSR by following these instructions:

1. If the CSR is in PEM format, convert it to a Distinguished Encoding Rules (DER) file, which has a binary format.
2. Sign the binary-formatted CSR with the private key from the MDM signing certificate using the `SHA256WithRSA` signing algorithm.
3. Encode the signature from the previous step as `Base64`.
4. Encode the binary-formatted CSR as `Base64`.
5. Create a Push Certificate Request `plist` and encode it as `Base64`.

> **Note**:  Don’t share the private key from your MDM signing certificate with anyone, including your customers or resellers of your solution. Ensure that the process of signing the CSR takes place within your internal infrastructure and isn’t accessible to customers.

 Don’t share the private key from your MDM signing certificate with anyone, including your customers or resellers of your solution. Ensure that the process of signing the CSR takes place within your internal infrastructure and isn’t accessible to customers.

Make sure that the `PushCertCertificateChain` value contains a complete certificate chain all the way back to a recognized root certificate, including the root certificate. This means it contains the following:

- Your MDM signing certificate
- The WWDR intermediate certificate, which is available from [`https://www.apple.com/certificateauthority/AppleWWDRCAG3.cer`](https://developer.apple.comhttps://www.apple.com/certificateauthority/AppleWWDRCAG3.cer).
- The Apple root certificate, which is available from [`http://www.apple.com/appleca/AppleIncRootCertificate.cer`](https://developer.apple.comhttp://www.apple.com/appleca/AppleIncRootCertificate.cer)

Also, ensure that each of the above certificates complies with PEM-formatting standards, which includes that each line except the last contains exactly 64 printable characters, and the last line contains 64 or fewer printable characters.

Save the certificate and its chain as a file that ends in `.pem` and then verify your certificate chain using either of the following command-line tools:

- `certtool -e < filename.pem`
- `openssl verify filename.pem`

To learn more about certificates and chains of trust, see [`Security Overview`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/Security/Conceptual/Security_Overview/Introduction/Introduction.html).

After you deliver the signed CSR back to the customer, the customer must log in to `https://identity.apple.com/pushcert` using a verified Apple ID and upload the CSR to the Apple Push Certificates Portal. The portal creates a certificate titled `MDM__Certificate.pem`. The customer then returns to your setup process to upload the APNs certificate for MDM.

See the sample code references below for additional information.

##### Java Sample Code

```other
/**
* Sign the CSR in DER format with the signing private key.
* Use SHA256withRSA for signing, SHA1 for message digest, and RSA to encrypt the message digest.
*/
byte[] signedData = signCSR(signingCertPrivateKey, csr);

String certChain = "-----BEGIN CERTIFICATE"----;

/**
* Create the Request plist. The CSR and signature are Base64-encoded.
*/
byte[] reqPlist = createPlist(new String(Base64.encodeBase64(csr)),certChain, new String(Base64.encodeBase64(signedData)));

/**
*  The signature uses two algorithms: one to calculate a message digest and one to encrypt the message digest.
*  The message digest is calculated using SHA1 and encrypted using RSA.
*  Initialize the signature with the signer's private key using initSign().
*  Use update() to add the data of the message into the signature.
**  @param privateKey Private key used to sign the data.
*  @param data Data to be signed.
*  @return Signature as a byte array.
*  @throws Exception
*/private byte[] signCSR( PrivateKey privateKey, byte[] data ) throws Exception{
    Signature sig = Signature.getInstance("SHA256withRSA"); 
    sig.initSign(privateKey);
    sig.update(data);
    byte[] signatureBytes = sig.sign();
    return signatureBytes;
}
```

##### Net Sample Code

```other
var privateKey = new PrivateKey(PrivateKey.KeySpecification.AtKeyExchange, 2048, false, true);
var caCertificateRequest = new CaCertificateRequest();
string csr = caCertificateRequest.GenerateRequest("cn=test", privateKey);

// Load-signing certificate from MDM_pfx.pfx. This is generated using signingCertificatePrivate.pem and SigningCert.pem.pem using openssl.
var cert = new X509Certificate2(MY_MDM_PFX, PASSWORD, X509KeyStorageFlags.Exportable);

// Use RSA provider to generate SHA256WithRSA.
var crypt = (RSACryptoServiceProvider)cert.PrivateKey;
var sha256 = new SHA256CryptoServiceProvider();
byte[] data = Convert.FromBase64String(csr);
byte[] hash = sha256.ComputeHash(data);

// Sign the hash.
byte[] signedHash = crypt.SignHash(hash, CryptoConfig.MapNameToOID("SHA256"));
var signedHashBytesBase64 = Convert.ToBase64String(signedHash);
```

##### Property List Sample Code

```other
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PushCertRequestCSR</key>
    <string> MIIDjzCCAncCAQAwDzENMAsGA1UEAwwEdGVzdDCCASIwDQYJKoZIhvcNAQEBBQAD</string>
    <key>PushCertCertificateChain</key>
    <string>
-----BEGIN CERTIFICATE-----
MIIDkzCCAnugAwIBAgIIQcQgtHQb9wwwDQYJKoZIhvcNAQEFBQAwUjEaMBgGA1UEAwwRU0FDSSBUZXN0IFJvb3QgQ0ExEjAQBgNVBAsMCUFwcGxlIElTVDETMBEGA1UE
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIDlTCCAn2gAwIBAgIIBInl9fQbaAkwDQYJKoZIhvcNAQEFBQAwXDEkMCIGA1UEAwwbU0FDSSBUZXN0IEludGVybWVkaWF0ZSBDQSAxMRIwEAYDVQQLDAlBcHBsZSBJ
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIDpjCCAo6gAwIBAgIIKRyFYgyyFPgwDQYJKoZIhvcNAQEFBQAwXDEkMCIGA1UEAwwbU0FDSSBUZXN0IEludGVybWVkaWF0ZSBDQSAxMRIwEAYDVQQLDAlBcHBsZSBJ
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIDiTCCAnGgAwIBAgIIdv/cjbnBgEgwDQYJKoZIhvcNAQEFBQAwUjEaMBgGA1UEAwwRU0FDSSBUZXN0IFJvb3QgQ0ExEjAQBgNVBAsMCUFwcGxlIElTVDETMBEGA1UE
-----END CERTIFICATE-----
</string>
    <key>PushCertSignature</key>
    <string>CGt6QWuixaO0PIBc9dr2kJpFBE1BZx2D8L0XH0Mtc/DePGJOjrM2W/IBFY0AVhhEx</string>
</dict>
</plist>
```

## See Also

- [Managing Certificates for MDM Servers and Devices](managing-certificates-for-mdm-servers-and-devices.md)
  Ensure secure MDM connectivity with valid certificates.
- [Deploying MDM Enrollment Profiles](deploying-mdm-enrollment-profiles.md)
  Choose the technique to deploy MDM enrollment profiles for your organization.
- [Installing Profiles on Devices](installing-profiles-on-devices.md)
  Optimize deployment of profiles and provisioning profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/setting-up-push-notifications-for-your-mdm-customers)*