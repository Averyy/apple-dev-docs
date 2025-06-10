# Registering an ad network

**Framework**: StoreKit

Use the install-validation APIs for your ad campaigns after registering your ad network with Apple.

#### Overview

Ad networks provide and cryptographically sign ads that are eligible for ad attribution through SKAdNetwork. Ad networks need to register with Apple before using the SKAdNetwork API.

To register your ad network, go to [`Ad Network ID Request Form`](https://developer.apple.comhttps://developer.apple.com/contact/request/ad-network-id/), which prompts you to sign in to Apple Developer and opens the request form.

When registering, you:

- Receive your ad network ID.
- Create an elliptic curve cryptographic key pair and share your public key with Apple for signature verification.
- Provide a URL for receiving SKAdNetwork install-validation postback requests.

##### Share Your Ad Network Id with Developers

The ad network ID is a unique lowercased identifier in the format of “`example123.skadnetwork`”. Share your ad network ID with app developers who display your ads. Developers need to include your ad network ID in their app’s information property list to initiate the app install-validation process.

> ❗ **Important**:  Lowercase the ad network ID string; otherwise, the system doesn’t recognize it as valid.

##### Generate Your Private Key

Ad networks use a private cryptographic key to generate a signature for each ad that an app displays. During registration, ad networks create a public-private key pair, and send the public key to Apple. The private key you create uses an Elliptic Curve Digital Signature Algorithm (ECDSA) with a prime256v1 curve.

To create your private key, open Terminal and enter the following command:

```shell
openssl ecparam -name prime256v1 -genkey -noout -out companyname_skadnetwork_private_key.pem
```

In the command, replace `companyname` with the name of your company. For example, the name of the private key file for a company named  is `example_skadnetwork_private_key.pem`.

> ❗ **Important**:  Secure your private keys as you do other credentials, such as passwords. Don’t share your private keys, store keys in a code repository, or include keys in client-side code. Share only your public key.

##### Generate and Share Your Public Key

Next, you create a public key from the private key you created in the previous section. The public key is a PEM-encoded PKCS#8 EC key that uses the prime256v1 curve. In Terminal, enter the following command, again replacing `companyname` with the name of your company:

```shell
openssl ec -in companyname_skadnetwork_private_key.pem -pubout -out companyname_skadnetwork_public_key.pem
```

This command creates the file `companyname_skadnetwork_public_key.pem`, which contains your public key. Run this command any time to generate a copy of your public key file.

Send your public key file to Apple when you register your ad network.

## See Also

- [Configuring a source app](configuring-a-source-app.md)
  Set up a source app to participate in ad campaigns.
- [Configuring an advertised app](configuring-an-advertised-app.md)
  Prepare an advertised app to participate in ad campaigns.
- [SKAdNetworkItems](../BundleResources/Information-Property-List/SKAdNetworkItems.md)
  An array of dictionaries containing a list of ad network IDs.
- [NSAdvertisingAttributionReportEndpoint](../BundleResources/Information-Property-List/NSAdvertisingAttributionReportEndpoint.md)
  The URL where Private Click Measurement and SKAdNetwork send attribution information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/registering-an-ad-network)*