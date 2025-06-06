# registerCKShare(_:container:allowedSharingOptions:)

**Framework**: Foundation  
**Kind**: method

Registers an existing collaboration object on a server.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func registerCKShare(_ share: CKShare, container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions = CKAllowedSharingOptions.standard)
```

#### Discussion

Use this method when a [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) currently exists on the server. When the system invokes the share sheet with a `CKShare` that you register with this method, it allows the owner to make modifications to the share settings, and allows a participant to view the share settings.

## Parameters

- `share`: An existing   on the server.
- `container`: A   the system uses to coordinate all the interactions between your app and the server.
- `allowedSharingOptions`: The  . The standard option is the default.

## See Also

- [func registerCloudKitShare(CKShare, container: CKContainer)](nsitemprovider/registercloudkitshare(_:container:).md)
  Registers a CloudKit share for the user to modify.
- [func registerCloudKitShare(preparationHandler: ((CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)](nsitemprovider/registercloudkitshare(preparationhandler:).md)
  Registers a handler that prepares a new CloudKit share.
- [func registerCKShare(container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions, preparationHandler: () async throws -> CKShare)](nsitemprovider/registerckshare(container:allowedsharingoptions:preparationhandler:).md)
  Creates and registers a new collaboration object using a collection of records to share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerckshare(_:container:allowedsharingoptions:))*