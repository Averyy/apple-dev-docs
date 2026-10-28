# application(_:userDidAcceptCloudKitShareWith:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user accepts a CloudKit sharing invitation.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, userDidAcceptCloudKitShareWith metadata: CKShareMetadata)
```

```objc
- (void) application:(NSApplication *) application userDidAcceptCloudKitShareWithMetadata:(CKShareMetadata *) metadata;
```

## Discussion

Use the provided metadata to begin sharing the specified content with the current user. For more information, see [CloudKit](../../CloudKit/CloudKit.md).

## Parameters

- `application`: The shared app object.
- `metadata`: The metadata associated with the invitation. Use the URL of the metadata’s [`CKShare`](../../CloudKit/ckshare.md) object and the [`containerIdentifier`](../../CloudKit/ckshare/metadata/containeridentifier.md) property to schedule a [`CKAcceptSharesOperation`](../../CloudKit/ckacceptsharesoperation.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:userdidacceptcloudkitsharewith:))*