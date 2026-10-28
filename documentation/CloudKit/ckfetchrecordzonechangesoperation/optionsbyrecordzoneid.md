# optionsByRecordZoneID

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

Configuration options for each record zone that the operation retrieves.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 5.0

> **Deprecated**: Use [`configurationsByRecordZoneID`](./configurationsbyrecordzoneid.md) instead.

## Declaration

```swift
var optionsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneOptions]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDictionary<CKRecordZoneID *,CKFetchRecordZoneChangesOptions *> * optionsByRecordZoneID;
```

## Discussion

You can associate each record zone ID with options that define what CloudKit fetches for that record zone.  See [`CKFetchRecordZoneChangesOperation.ZoneOptions`](./zoneoptions.md) for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/optionsbyrecordzoneid)*