# accept(_:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Accepts the specified share metadata.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func accept(_ metadata: CKShare.Metadata, completionHandler: @escaping @Sendable (CKShare?, (any Error)?) -> Void)
```

```objc
- (void) acceptShareMetadata:(CKShareMetadata *) metadata completionHandler:(void (^)(CKShare *acceptedShare, NSError *error)) completionHandler;
```

#### Discussion

The closure doesn’t return a value and takes the following parameters:

- The corresponding share, or `nil` if CloudKit can’t accept the metadata.
- An error if a problem occurs, or `nil` if CloudKit successfully accepts the metadata.

## Parameters

- `metadata`: The metadata of the share to accept.
- `completionHandler`: The handler to execute when the process finishes.

## See Also

### Accessing Container Metadata
- [func fetchShareMetadata(with: URL, completionHandler: (CKShare.Metadata?, (any Error)?) -> Void)](./fetchsharemetadata%28with,completionhandler%29.md)
  Fetches the share metadata for the specified share URL.
- [static let CKAccountChanged: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/ckaccountchanged.md)
  A notification that a container posts when the status of an iCloud account changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/accept(_:completionhandler:)-949ea)*