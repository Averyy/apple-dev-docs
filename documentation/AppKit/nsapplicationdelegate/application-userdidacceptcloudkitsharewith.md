# application(_:userDidAcceptCloudKitShareWith:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate when the user accepts a CloudKit sharing invitation.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, userDidAcceptCloudKitShareWith metadata: CKShareMetadata)
```

#### Discussion

Use the provided metadata to begin sharing the specified content with the current user. For more information, see [`CloudKit`](https://developer.apple.com/documentation/CloudKit).

## Parameters

- `application`: The shared app object.
- `metadata`: The metadata associated with the invitation. Use the URL of the metadata’s [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) object and the [`containerIdentifier`](https://developer.apple.com/documentation/CloudKit/CKShare/Metadata/containerIdentifier) property to schedule a [`CKAcceptSharesOperation`](https://developer.apple.com/documentation/CloudKit/CKAcceptSharesOperation) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:userdidacceptcloudkitsharewith:))*