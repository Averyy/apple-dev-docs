# optionsByRecordZoneID

**Framework**: CloudKit  
**Kind**: property

Configuration options for each record zone that the operation retrieves.

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
var optionsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneOptions]? { get set }
```

#### Discussion

You can associate each record zone ID with options that define what CloudKit fetches for that record zone.  See [`CKFetchRecordZoneChangesOperation.ZoneOptions`](ckfetchrecordzonechangesoperation/zoneoptions.md) for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/optionsbyrecordzoneid)*