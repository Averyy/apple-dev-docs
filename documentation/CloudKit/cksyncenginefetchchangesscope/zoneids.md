# zoneIDs

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A specific set of zone IDs to include in the scope.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@property (copy, readonly, nullable) NSSet<CKRecordZoneID *> * zoneIDs;
```

## Discussion

For example, if you want to fetch changes for a specific set of zones, you can specify them here. If `nil`, this scope includes all zones except those in `excludedZoneIDs`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginefetchchangesscope/zoneids)*