# Identifying an App’s Containers

**Framework**: CloudKit

Use Xcode’s Project navigator to find the identifiers of active CloudKit containers.

#### Overview

An app’s Xcode project manages which CloudKit containers are available to that app. When you write code that needs to provide container identifiers for all of the containers your app uses, reference the list of active containers in Xcode.

##### Identify the Containers Your App Uses

In your app’s Xcode project, select Signing & Capabilities > iCloud in the Project navigator.

![A screenshot of an Xcode project’s Signing & Capabilities pane. The project contains the iCloud capability with the CloudKit option in a selected state. There are three custom CloudKit containers — app, docs, and settings — and each is in a selected state.](https://docs-assets.developer.apple.com/published/834483e205503a63b239752195f2c377/media-3743337%402x.png)

After you identify the containers that your app uses, you can create instances of [`CKContainer`](ckcontainer.md) in your app and interact with CloudKit data.

```swift
// These constants correspond to the containers you configure for your
// target in your project's Signing & Capabilities tab.
let app = CKContainer(identifier: "iCloud.com.example.MyCloudKitApp.app")
let docs = CKContainer(identifier: "iCloud.com.example.MyCloudKitApp.docs")
let settings = CKContainer(identifier: "iCloud.com.example.MyCloudKitApp.settings")
```

## See Also

- [Encrypting User Data](encrypting-user-data.md)
  Deploy industry-standard security technologies using CloudKit encryption.
- [Providing User Access to CloudKit Data](providing-user-access-to-cloudkit-data.md)
  Provide users access to the data your app stores on their behalf.
- [Changing Access Controls on User Data](changing-access-controls-on-user-data.md)
  Restrict access to or remove restrictions from a user’s data at their request.
- [class CKFetchWebAuthTokenOperation](ckfetchwebauthtokenoperation.md)
  An operation that creates an authentication token for use with CloudKit web services.
- [Responding to Requests to Delete Data](responding-to-requests-to-delete-data.md)
  Provide options for users to delete their CloudKit data from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/identifying-an-app-s-containers)*