# CKAccountChangedNotification

**Framework**: CloudKit  
**Kind**: var  
**Role**: Global Variable

A notification that a container posts when the status of an iCloud account changes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
extern NSString * const CKAccountChangedNotification;
```

#### Discussion

Create an instance of [`CKContainer`](./ckcontainer.md) to receive this notification. The container posts the notification using an arbitrary queue. Use the [`accountStatus(completionHandler:)`](./ckcontainer/accountstatus%28completionhandler%29.md) method to obtain the account’s status.

## See Also

### Accessing Container Metadata
- [func fetchShareMetadata(with: URL, completionHandler: (CKShare.Metadata?, (any Error)?) -> Void)](./ckcontainer/fetchsharemetadata%28with,completionhandler%29.md)
  Fetches the share metadata for the specified share URL.
- [func accept(CKShare.Metadata, completionHandler: (CKShare?, (any Error)?) -> Void)](./ckcontainer/accept%28_,completionhandler%29-949ea.md)
  Accepts the specified share metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckaccountchangednotification)*