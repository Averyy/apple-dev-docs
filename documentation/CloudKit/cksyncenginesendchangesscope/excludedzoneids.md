# excludedZoneIDs

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A specific set of zone IDs to exclude from this scope. If you know that you don’t want to send changes for a particular set of zones, you can set those zones here.

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
@property (copy, readonly) NSSet<CKRecordZoneID *> * excludedZoneIDs;
```

## Discussion

> **Note**: A scope with a non-nil [`zoneIDs`](./zoneids.md) always has an empty `excludedZoneIDs`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginesendchangesscope/excludedzoneids)*