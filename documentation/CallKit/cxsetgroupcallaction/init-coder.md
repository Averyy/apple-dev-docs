# init(coder:)

**Framework**: CallKit  
**Kind**: init

Creates a new action to group calls with data in an unarchiver.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init?(coder aDecoder: NSCoder)
```

## Parameters

- `aDecoder`: An unarchiver object.

## See Also

- [init(call: UUID, callUUIDToGroupWith: UUID?)](cxsetgroupcallaction/init(call:calluuidtogroupwith:).md)
  Initializes a new action for a call identified by a given UUID, as well as a call to group with identified by another UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsetgroupcallaction/init(coder:))*