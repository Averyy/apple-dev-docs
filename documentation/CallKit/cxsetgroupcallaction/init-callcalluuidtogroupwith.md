# init(call:callUUIDToGroupWith:)

**Framework**: CallKit  
**Kind**: init

Initializes a new action for a call identified by a given UUID, as well as a call to group with identified by another UUID.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(call callUUID: UUID, callUUIDToGroupWith: UUID?)
```

#### Return Value

A new action for the specified call UUID and call UUID to group with.

## Parameters

- `callUUID`: The unique identifier for the associated   object of the action.
- `callUUIDToGroupWith`: If  , the the call associated with the receiver leaves any group it’s currently a member of.

## See Also

- [init?(coder: NSCoder)](cxsetgroupcallaction/init(coder:).md)
  Creates a new action to group calls with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsetgroupcallaction/init(call:calluuidtogroupwith:))*