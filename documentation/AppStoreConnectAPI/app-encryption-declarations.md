# App Encryption Declarations

**Framework**: Appstoreconnectapi

View, and assign to builds, the declarations about types of encryption used in your app.

#### Overview

To comply with regulatory requirements, you sometimes need to provide information and supporting documentation in the form of declarations about the types of encryption used by your app. The app encryption declarations resource represents this information, and enables you to:

- View information about the declaration, and
- Assign the declaration to a build.
- Create app encryption declarations in App Store Connect.
- Upload app encryption declaration documents.

> **Note**:  Builds that have the `usesNonExemptEncryption` flag set to true in the app’s property list must link to an app encryption declaration before the app can be submitted for beta app review.

For more information, see [`Overview of export compliance`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance).

## Topics

### Getting App Encryption Declarations
- [List App Encryption Declarations](get-v1-appencryptiondeclarations.md)
  Find and list all available app encryption declarations.
- [Read App Encryption Declaration Information](get-v1-appencryptiondeclarations-_id_.md)
  Get information about a specific app encryption declaration.
- [Read the App Information of an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-app.md)
  Get the app information from a specific app encryption declaration.
- [Read a specific App Encryption Declaration Document](get-v1-appencryptiondeclarationdocuments-_id_.md)
  Get detailed information about a specified App Encryption Declaration document.
- [Read the Declaration Document for an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-appencryptiondeclarationdocument.md)
  Read the associate document for a specific App Encryption Declaration.
### Assigning App Encryption Declarations
- [Create an app encryption declarations](post-v1-appencryptiondeclarations.md)
  Add an app encryption delcaration for a specific app.
- [Assign Builds to an App Encryption Declaration](post-v1-appencryptiondeclarations-_id_-relationships-builds.md)
  Assign one or more builds to an app encryption declaration.
### Uploading App Encryption Declaration Documents
- [Upload an App Encryption Declaration Document](post-v1-appencryptiondeclarationdocuments.md)
  Add an App Encryption Declaration Document to an existing App Encryption Declaration.
- [Modify an App Encryption Declaration Document](patch-v1-appencryptiondeclarationdocuments-_id_.md)
  Commit an App Encryption Declaration Document after uploading it.
### Objects and Data Types
- [object AppEncryptionDeclarationCreateRequest](appencryptiondeclarationcreaterequest.md)
  The request body you use to create an app encryption declaration.
- [object AppEncryptionDeclarationDocument](appencryptiondeclarationdocument.md)
- [object AppEncryptionDeclarationDocumentCreateRequest](appencryptiondeclarationdocumentcreaterequest.md)
- [object AppEncryptionDeclarationDocumentResponse](appencryptiondeclarationdocumentresponse.md)
- [object AppEncryptionDeclarationDocumentUpdateRequest](appencryptiondeclarationdocumentupdaterequest.md)
- [object AppEncryptionDeclaration](appencryptiondeclaration.md)
  The data structure that represents an App Encryption Declarations resource.
- [object AppEncryptionDeclarationBuildsLinkagesRequest](appencryptiondeclarationbuildslinkagesrequest.md)
  A request body you use to add builds to an app encryption declaration.
- [object AppEncryptionDeclarationResponse](appencryptiondeclarationresponse.md)
  A response that contains a single App Encryption Declarations resource.
- [object AppEncryptionDeclarationWithoutIncludesResponse](appencryptiondeclarationwithoutincludesresponse.md)
- [object AppEncryptionDeclarationsResponse](appencryptiondeclarationsresponse.md)
  A response that contains a list of App Encryption Declaration resources.
- [type AppEncryptionDeclarationState](appencryptiondeclarationstate.md)
  Strings that represent the review or acceptance status of an app encryption declaration submitted to Apple.

## See Also

- [Builds](builds.md)
  Manage builds for testers and submit builds for review.
- [Build Bundles](build-bundles.md)
  Read metadata for app and App Clip binaries included in a build you upload to App Store Connect.
- [Build Icons](build-icons.md)
  Get icons from your app’s binary that are uploaded to App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreConnectAPI/app-encryption-declarations)*