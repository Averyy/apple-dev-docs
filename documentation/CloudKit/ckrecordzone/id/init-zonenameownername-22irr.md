# init(zoneName:ownerName:)

**Framework**: CloudKit  
**Kind**: init

Creates a record zone ID with the specified name and owner.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
convenience init(zoneName: String = CKRecordZone.ID.defaultZoneName, ownerName: String = CKCurrentUserDefaultName)
```

#### Return Value

A new record zone ID, or `nil` if CloudKit can’t create the record zone ID.

## Parameters

- `zoneName`: The name that identifies the record zone. Zone names consist of up to 255 ASCII characters, and don’t start with an underscore. To specify the default zone of the current database, use   . This parameter must not be   or an empty string.
- `ownerName`: The user who creates the record zone. To specify the current user, use  . If you provide   or an empty string for this parameter, the method throws an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/id/init(zonename:ownername:)-22irr)*