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
  The server change token.
- [var resultsLimit: Int](ckfetchrecordzonechangesoperation/zoneconfiguration/resultslimit.md)
  The maximum number of records that CloudKit retrieves when fetching zone changes.
- [var desiredKeys: [CKRecord.FieldKey]?](ckfetchrecordzonechangesoperation/zoneconfiguration/desiredkeys.md)
  An array of the record keys to retrieve.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var configurationsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneConfiguration]?](ckfetchrecordzonechangesoperation/configurationsbyrecordzoneid.md)
  A dictionary of configurations for fetching change operations by zone identifier.
- [var fetchAllChanges: Bool](ckfetchrecordzonechangesoperation/fetchallchanges.md)
  A Boolean value that indicates whether to send repeated requests to the server.
- [var recordZoneIDs: [CKRecordZone.ID]?](ckfetchrecordzonechangesoperation/recordzoneids.md)
  The IDs of the record zones that contain the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneconfiguration)*