# zoneID

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The unique ID of the zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var zoneID: CKRecordZone.ID { get }
```

```objc
@property (copy, readonly) CKRecordZoneID * zoneID;
```

## Discussion

The zone ID contains the name of the zone and the name of the user who owns the zone. Use this property to access both of those values.

## See Also

### Getting the Zone Attributes
- [var capabilities: CKRecordZone.Capabilities](./capabilities-swift.property.md)
  The capabilities that the zone supports.
- [CKRecordZone.Capabilities](./capabilities-swift.struct.md)
  The capabilities that a record zone supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/zoneid)*