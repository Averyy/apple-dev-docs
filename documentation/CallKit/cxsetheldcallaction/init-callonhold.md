# init(call:onHold:)

**Framework**: CallKit  
**Kind**: init

Initializes a new action for a call identified by a given UUID, as well as whether the call is on hold.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(call callUUID: UUID, onHold: Bool)
```

#### Return Value

A new action for the specified call UUID and whether the call is placed on hold.

## Parameters

- `callUUID`: The unique identifier for the associated   object of the action.
- `onHold`: Whether the call is on hold.

## See Also

- [init?(coder: NSCoder)](cxsetheldcallaction/init(coder:).md)
  Creates a new action to place a call on hold with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsetheldcallaction/init(call:onhold:))*