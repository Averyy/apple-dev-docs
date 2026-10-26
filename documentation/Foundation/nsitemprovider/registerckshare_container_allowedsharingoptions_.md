# registerCKShare:container:allowedSharingOptions:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Registers an existing collaboration object on a server.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```objc
- (void) registerCKShare:(CKShare *) share container:(CKContainer *) container allowedSharingOptions:(CKAllowedSharingOptions *) allowedOptions;
```

#### Discussion

Use this method when a [`CKShare`](../../CloudKit/ckshare.md) currently exists on the server. When the system invokes the share sheet with a `CKShare` that you register with this method, it allows the owner to make modifications to the share settings, and allows a participant to view the share settings.

## Parameters

- `share`: An existing [`CKShare`](../../CloudKit/ckshare.md) on the server.
- `container`: A [`CKContainer`](../../CloudKit/ckcontainer.md) the system uses to coordinate all the interactions between your app and the server.
- `allowedOptions`: The [`CKAllowedSharingOptions`](../../CloudKit/ckallowedsharingoptions.md). The standard option is the default.

## See Also

### Registering CloudKit shares
- [func registerCloudKitShare(CKShare, container: CKContainer)](./registercloudkitshare%28_,container%29.md)
  Registers a CloudKit share for the user to modify.
- [func registerCloudKitShare(preparationHandler: ((CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)](./registercloudkitshare%28preparationhandler%29.md)
  Registers a handler that prepares a new CloudKit share.
- [- registerCKShareWithContainer:allowedSharingOptions:preparationHandler:](./registercksharewithcontainer_allowedsharingoptions_preparationhandler_.md)
  Creates and registers a new collaboration object using a collection of records to share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerckshare:container:allowedsharingoptions:)*