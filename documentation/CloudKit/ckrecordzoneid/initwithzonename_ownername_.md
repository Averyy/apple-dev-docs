# initWithZoneName:ownerName:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates a record zone ID with the specified name and owner.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```objc
- (instancetype) initWithZoneName:(NSString *) zoneName ownerName:(NSString *) ownerName;
```

#### Return Value

A new record zone ID.

## Parameters

- `zoneName`: The name that identifies the record zone. Zone names consist of up to 255 ASCII characters, and don’t start with an underscore. To specify the default zone of the current database, use [`CKRecordZoneDefaultName`](../ckrecordzonedefaultname-8mfij.md). This parameter must not be `nil` or an empty string.
- `ownerName`: The user who creates the record zone. To specify the current user, use [`CKCurrentUserDefaultName`](../ckcurrentuserdefaultname.md). If you provide `nil` or an empty string for this parameter, the method throws an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzoneid/initwithzonename:ownername:)*