# CKFetchRecordZoneChangesOperation.ZoneConfiguration

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

A configuration object that describes the information to fetch from a record zone.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class ZoneConfiguration
```

```objc
@interface CKFetchRecordZoneChangesConfiguration : NSObject
```

## Topics

### Creating a Zone Change Configuration
- [convenience init(previousServerChangeToken: CKServerChangeToken?, resultsLimit: Int?, desiredKeys: [CKRecord.FieldKey]?)](./zoneconfiguration/init%28previousserverchangetoken,resultslimit,desiredkeys%29.md)
  Creates a zone configuration with the desired keys and a result limit for updates.
### Accessing a Zone Change Configuration
- [var previousServerChangeToken: CKServerChangeToken?](./zoneconfiguration/previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var resultsLimit: Int](./zoneconfiguration/resultslimit.md)
  The maximum number of records to fetch from the record zone.
- [var desiredKeys: [CKRecord.FieldKey]?](./zoneconfiguration/desiredkeys.md)
  The fields to fetch for the requested records.
- [desiredKeys](../ckfetchrecordzonechangesconfiguration/desiredkeys.md)
  The fields to fetch for the requested records.
### Initializers
- [init?(coder: NSCoder)](./zoneconfiguration/init%28coder%29.md)

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
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the Zone Change Operation
- [var configurationsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneConfiguration]?](./configurationsbyrecordzoneid.md)
  A dictionary of configurations for fetching change operations by zone identifier.
- [var fetchAllChanges: Bool](./fetchallchanges.md)
  A Boolean value that indicates whether to send repeated requests to the server.
- [var recordZoneIDs: [CKRecordZone.ID]?](./recordzoneids.md)
  The IDs of the record zones that contain the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneconfiguration)*