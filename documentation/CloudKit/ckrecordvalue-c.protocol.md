# CKRecordValue

**Framework**: CloudKit  
**Kind**: protocol  
**Role**: Protocol

The protocol that provides strong type-checking for objects that the CloudKit framework stores on the server.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```objc
@protocol CKRecordValue <NSObject>
```

## Overview

CloudKit supports the following classes that adopt this protocol:

- [`NSString`](../Foundation/nsstring.md)
- [`NSNumber`](../Foundation/nsnumber.md)
- [`NSArray`](../Foundation/nsarray.md)
- [`NSDate`](../Foundation/nsdate.md)
- [`NSData`](../Foundation/nsdata.md)
- [`CKRecord.Reference`](./ckrecord/reference.md)
- [`CKAsset`](./ckasset.md)
- [`CLLocation`](../CoreLocation/cllocation.md)

Don’t adopt this protocol in your custom classes. CloudKit doesn’t support writing custom data types to the server. Attempting to do so results in an error.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [CKAsset](./ckasset.md)
- [CKRecord.Reference](./ckrecord/reference.md)

## See Also

### Core objects
- [class CKContainer](./ckcontainer.md)
  A conduit to your app’s databases.
- [class CKDatabase](./ckdatabase.md)
  An object that represents a collection of record zones and subscriptions.
- [class CKOperationGroup](./ckoperationgroup.md)
  An explicit association between two or more operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordvalue-c.protocol)*