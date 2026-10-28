# capabilities

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The capabilities that the zone supports.

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
var capabilities: CKRecordZone.Capabilities { get }
```

```objc
@property (assign, readonly) CKRecordZoneCapabilities capabilities;
```

## Discussion

The server determines the capabilities of the zone and sets the value of this property when you save the record zone. Always check this property before performing tasks that require a specific capability.

Default zones don’t support any special capabilities. Custom zones in a private database support the options that [`CKRecordZone.Capabilities`](./capabilities-swift.struct.md) provides.

## See Also

### Getting the Zone Attributes
- [var zoneID: CKRecordZone.ID](./zoneid.md)
  The unique ID of the zone.
- [CKRecordZone.Capabilities](./capabilities-swift.struct.md)
  The capabilities that a record zone supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/capabilities-swift.property)*