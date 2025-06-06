# Creating and configuring keys for web distribution

**Framework**: App Store Connect API

Manage keys you use to sign JSON web tokens (JWTs).

#### Overview

Use alternative distribution keys to configure your app for installation from your website. To create an alternative distribution key, you must have an existing app in App Store Connect. If you don’t have one, create one before continuing.

##### Generate Your Private Key

App Store Connect uses a private cryptographic key to generate a signature for each app that you distribute from your website. During registration, you create a public-private key pair, and send the public key to App Store Connect. The private key you create uses an Elliptic Curve Digital Signature Algorithm (ECDSA) with the P-256 curve and the SHA-256 hash algorithm.

To create your private key, open Terminal and enter the following command:

```other
openssl ecparam -name prime256v1 -genkey -noout -out private_key.pem
```

This command creates the file `private_key.pem`, which contains your private key.

> ❗ **Important**:  Secure your private keys as you do other credentials, such as passwords. Don’t share your private keys, store keys in a code repository, or include keys in client-side code. Share only your public key.

 Secure your private keys as you do other credentials, such as passwords. Don’t share your private keys, store keys in a code repository, or include keys in client-side code. Share only your public key.

##### Generate Your Public Key

Create a public key from the private key you created in the previous section. The public key is a PEM-encoded PKCS#8 EC key that uses the P-256 curve. In Terminal, enter the following command:

```other
openssl ec -in private_key.pem -pubout > public_key.pem
```

This command creates the file `public_key.pem`, which contains your public key. Run this command any time to generate a copy of your public key file. To request your existing public key from App Store Connect, see [`Read an app’s alternative distribution key`](get-v1-apps-_id_-alternativedistributionkey.md).

##### Create an Alternative Distribution Key

> **Note**:  For web-distribution apps, add a single alternative distribution key, then add an alternative distribution domain. For more information, see [`Add an alternative distribution domain`](post-v1-alternativedistributiondomains.md) and [`Add an alternative distribution key`](post-v1-alternativedistributionkeys.md).

 For web-distribution apps, add a single alternative distribution key, then add an alternative distribution domain. For more information, see [`Add an alternative distribution domain`](post-v1-alternativedistributiondomains.md) and [`Add an alternative distribution key`](post-v1-alternativedistributionkeys.md).

Next, upload your public key to App Store Connect using the endpoint described in [`Add an alternative distribution key`](post-v1-alternativedistributionkeys.md).

The `id` in the `relationships` object is the app Apple ID for your app. You can find this app Apple ID by calling [`List Apps`](get-v1-apps.md) and filtering for your app name or by going to App Store Connect.

To access your web distribution app’s Apple ID, log in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/).

1. Select Apps.
2. Select your marketplace app from the list.
3. Under General, select App Information.
4. Scroll down to General Information, and locate your app Apple ID below your SKU.

The following request uploads the public key to App Store Connect:

```other
POST https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys
{
  "data": {
    "type": "alternativeDistributionKeys",
    "id": null,
    "attributes": {
      "publicKey": "-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE7rsxeCw+hrwRgStk0J2vYmnGQZha\ngSt0fm511aTjpDVsaIy9z7jmUKjJ1jgb8P5UKmQfmw0ovD+fNTSefjrw5A==\n-----END PUBLIC KEY-----\n"
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "6473805491"
        }
      }
    }
  }
}
```

## See Also

- [Creating keys and establishing alternative marketplace connections](creating-keys-and-establishing-alternative-marketplace-connections.md)
  Manage keys you use to sign JSON web tokens and connect marketplaces with apps.
- [Add an alternative distribution key](post-v1-alternativedistributionkeys.md)
  Add an alternative distribution key for your alternative marketplace app or web distribution.
- [List alternative distribution keys](get-v1-alternativedistributionkeys.md)
  List the alternative distribution key for your account.
- [Read alternative distribution key information](get-v1-alternativedistributionkeys-_id_.md)
  Read the public key information for a specific alternative distribution key.
- [Remove an alternative distribution key](delete-v1-alternativedistributionkeys-_id_.md)
  Remove an alternative distribution key from your account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/creating-and-configuring-keys-for-web-distribution)*