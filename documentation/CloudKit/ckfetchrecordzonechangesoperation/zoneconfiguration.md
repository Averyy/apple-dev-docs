# CKFetchRecordZoneChangesOperation.ZoneConfiguration

**Framework**: CloudKit  
**Kind**: class

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

## Topics

### Creating a Zone Change Configuration
- [convenience init(previousServerChangeToken: CKServerChangeToken?, resultsLimit: Int?, desiredKeys: [CKRecord.FieldKey]?)](ckfetchrecordzonechangesoperation/zoneconfiguration/init(previousserverchangetoken:resultslimit:desiredkeys:).md)
  Creates a zone configuration with the desired keys and a result limit for updates.
### Accessing a Zone Change Configuration
- [var previousServerChangeToken: CKServerChangeToken?](ckfetchrecordzonechangesoperation/zoneconfiguration/previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var resultsLimit: Int](ckfetchrecordzonechangesoperation/zoneconfiguration/resultslimit.md)
  The maximum number of records to fetch from the record zone.
- [var desiredKeys: [CKRecord.FieldKey]?](ckfetchrecordzonechangesoperation/zoneconfiguration/desiredkeys.md)
  The fields to fetch for the requested records.
### Initializers
- [init?(coder: NSCoder)](ckfetchrecordzonechangesoperation/zoneconfiguration/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var configurationsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneConfiguration]?](ckfetchrecordzonechangesoperation/configurationsbyrecordzoneid.md)
  A dictionary of configurations for fetching change operations by zone identifier.
- [var fetchAllChanges: Bool](ckfetchrecordzonechangesoperation/fetchallchanges.md)
  A Boolean value that indicates whether to send repeated requests to the server.
- [var recordZoneIDs: [CKRecordZone.ID]?](ckfetchrecordzonechangesoperation/recordzoneids.md)
  The IDs of the record zones that contain the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneconfiguration)*