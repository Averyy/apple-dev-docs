# CKFetchRecordZoneChangesOperation.ZoneOptions

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

A configuration object that describes the information to fetch from a record zone.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- iPadOS 10.0+ - Deprecated in 12.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- macOS 10.12+ - Deprecated in 10.14 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- tvOS 10.0+ - Deprecated in 12.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- watchOS 3.0+ - Deprecated in 5.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)

> **Deprecated**: Use [`CKFetchRecordZoneChangesOperation.ZoneConfiguration`](./zoneconfiguration.md) instead.

## Declaration

```swift
class ZoneOptions
```

```objc
@interface CKFetchRecordZoneChangesOptions : NSObject
```

## Topics

### Zone Change Options
- [var desiredKeys: [String]?](./zoneoptions/desiredkeys.md)
  The fields to fetch for the requested records.
- [var previousServerChangeToken: CKServerChangeToken?](./zoneoptions/previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var resultsLimit: Int](./zoneoptions/resultslimit.md)
  The maximum number of records to fetch from the record zone.
### Initializers
- [init?(coder: NSCoder)](./zoneoptions/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Deprecated Methods
- [convenience init(recordZoneIDs: [CKRecordZone.ID], optionsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneOptions]?)](./init%28recordzoneids,optionsbyrecordzoneid%29.md)
  Creates an operation for fetching record zone changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneoptions)*