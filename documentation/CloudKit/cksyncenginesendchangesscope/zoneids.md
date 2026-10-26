# zoneIDs

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The scope of zone IDs in which to send changes.

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

#### Discussion

If you only want to send changes for a particular set of zones, you can initialize your scope with those zone IDs. When creating the next batch of changes to send to the server, consult this, and only send changes within these zones. If this and [`recordIDs`](./recordids.md) are `nil`, then you should send all changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginesendchangesscope/zoneids)*