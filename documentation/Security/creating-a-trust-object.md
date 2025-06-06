# Creating a Trust Object

**Framework**: Security

Construct a trust object from a certificate and a policy.

#### Overview

Evaluating trust is a two-step process. First, the system examines the certificate’s digital signature. The Certificate Authority (CA) that issues the certificate creates the signature using its own identity (private key plus certificate) and embeds this byte stream in the leaf certificate (the one under evaluation). If the signature checks out, and as long as the CA’s own certificate is valid, then the leaf certificate must also be valid. The CA’s certificate is in turn signed by another issuer, whose certificate is signed by another, and so on. This chain of certificates ends with the anchor certificate, which is typically one of the inherently trusted root certificates embedded in the operating system. For example, your app can rely on any of the root certificates embedded in [`iOS`](https://developer.apple.comhttps://support.apple.com/en-us/HT204132) or [`macOS`](https://developer.apple.comhttps://support.apple.com/en-us/HT202858). Alternatively, you can supply your own.

The second step in trust evaluation is testing the certificate against a trust policy. The policy indicates how particular fields or extensions of a certificate affect whether it should be trusted for a particular use. For example, the policy may state that a certificate must not be expired or must be marked as valid for encryption, code signing, or some other specific purpose.

All of this activity is facilitated by an instance of the [`SecTrust`](sectrust.md) object that you prepare with one or more certificates and a policy objects.

##### Prepare the Certificate Chain

When you have a certificate that you want to evaluate, obtained using one of the methods described in [`Getting a Certificate`](getting-a-certificate.md), you prepare an array containing at least that certificate:

You can also include in this array the root certificate and any intermediates in the chain, but the system automatically looks for these if you don’t include them. It searches the keychain and the operating system’s collection of known root certificates. It may also download intermediate certificates from the network, if appropriate. As a result, explicitly including in the array any intermediate certificates that might otherwise require fetching may speed up the evaluation.

##### Prepare a Policy

You can construct your own policy from properties defined in the API using [`SecPolicyCreateWithProperties(_:_:)`](secpolicycreatewithproperties(_:_:).md), but the best option is usually to use one of the predefined policies. For example, you can create an SSL policy with the [`SecPolicyCreateSSL(_:_:)`](secpolicycreatessl(_:_:).md) function or the basic X509 policy with the [`SecPolicyCreateBasicX509()`](secpolicycreatebasicx509().md) function. For example, for X509:

##### Create a Trust Object

After you have prepared the certificate chain and policy, you then use the [`SecTrustCreateWithCertificates(_:_:_:)`](sectrustcreatewithcertificates(_:_:_:).md) function to create a trust object:


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/creating-a-trust-object)*