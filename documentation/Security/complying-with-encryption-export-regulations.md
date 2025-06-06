# Complying with Encryption Export Regulations

**Framework**: Security

Declare the use of encryption in your app to streamline the app submission process.

#### Overview

When you submit your app to TestFlight or the App Store, you upload your app to a server in the United States. If you distribute your app outside the U.S. or Canada, your app is subject to U.S. export laws, regardless of where your legal entity is based. If your app uses, accesses, contains, implements, or incorporates encryption, this is considered an export of encryption software, which means your app is subject to U.S. export compliance requirements, as well as the import compliance requirements of the countries where you distribute your app.

Every time you submit a new version of your app, App Store Connect asks you questions to guide you through a compliance review. You can bypass these questions and streamline the submission process by providing the required information in your app’s [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List) file.

For more information about export compliance, read [`Export compliance overview`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev88f5c7bf9).

##### Declare Your Apps Use of Encryption

Add the [`ITSAppUsesNonExemptEncryption`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ITSAppUsesNonExemptEncryption) key to your app’s `Info.plist` file with a Boolean value that indicates whether your app uses encryption. Set the value to `NO` if your app—including any third-party libraries it links against—doesn’t use encryption, or if it only uses forms of encryption that are exempt from export compliance documentation requirements. Otherwise, set it to `YES`.

![None](https://docs-assets.developer.apple.com/published/f2655239d17f666aa363e42d1a5d69f0/media-3150498%402x.png)

Typically, the use of encryption that’s built into the operating system—for example, when your app makes HTTPS connections using [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession)—is exempt from export documentation upload requirements, whereas the use of proprietary encryption is not. To determine whether your use of encryption is considered exempt, see [`Determine your export compliance requirements`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev63c95e436).

> ❗ **Important**:  If your app uses exempt forms of encryption, you might alternatively be required to submit a year-end self-classification report to the U.S. government. (If you use non-exempt encryption and provide documentation to Apple, the self-classification report isn’t necessary.) To learn more, see [`How to file an Annual Self Classification Report`](https://developer.apple.comhttps://www.bis.doc.gov/index.php/policy-guidance/encryption/4-reports-and-reviews/a-annual-self-classification).

 If your app uses exempt forms of encryption, you might alternatively be required to submit a year-end self-classification report to the U.S. government. (If you use non-exempt encryption and provide documentation to Apple, the self-classification report isn’t necessary.) To learn more, see [`How to file an Annual Self Classification Report`](https://developer.apple.comhttps://www.bis.doc.gov/index.php/policy-guidance/encryption/4-reports-and-reviews/a-annual-self-classification).

##### Provide Compliance Documentation

If your app requires export compliance documentation, upload the required items to App Store Connect, as described in [`Upload export compliance documentation`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev38f592ac9). After successfully reviewing the documents, Apple provides you with a code. Add this string as the value for the [`ITSEncryptionExportComplianceCode`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ITSEncryptionExportComplianceCode) key in your app’s `Info.plist` file.

![None](https://docs-assets.developer.apple.com/published/ca34fbcb2028db89215039913ebd1527/media-3150497%402x.png)

## Topics

### Encryption Export Compliance Keys
- [ITSAppUsesNonExemptEncryption](../BundleResources/Information-Property-List/ITSAppUsesNonExemptEncryption.md)
  A Boolean value indicating whether the app uses encryption.
- [ITSEncryptionExportComplianceCode](../BundleResources/Information-Property-List/ITSEncryptionExportComplianceCode.md)
  The export compliance code provided by App Store Connect for apps that require it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations)*