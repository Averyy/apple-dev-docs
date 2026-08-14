# CKFetchRecordZoneChangesOperation.ZoneOptions

**Framework**: CloudKit  
**Kind**: class

A configuration object that describes the information to fetch from a record zone.

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
class ZoneOptions
```

## Topics

### Zone Change Options
- [var desiredKeys: [String]?](ckfetchrecordzonechangesoperation/zoneoptions/desiredkeys.md)
  The fields to fetch for the requested records.
- [var previousServerChangeToken: CKServerChangeToken?](ckfetchrecordzonechangesoperation/zoneoptions/previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var resultsLimit: Int](ckfetchrecordzonechangesoperation/zoneoptions/resultslimit.md)
  The maximum number of records to fetch from the record zone.
### Initializers
- [init?(coder: NSCoder)](ckfetchrecordzonechangesoperation/zoneoptions/init(coder:).md)

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

## See Also

- [convenience init(recordZoneIDs: [CKRecordZone.ID], optionsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneOptions]?)](ckfetchrecordzonechangesoperation/init(recordzoneids:optionsbyrecordzoneid:).md)
  Creates an operation for fetching record zone changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneoptions)*