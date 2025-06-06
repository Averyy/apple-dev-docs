# init(call:digits:type:)

**Framework**: CallKit  
**Kind**: init

Initializes a new action for a call identified by a given UUID, as well as a specified type and sequence of digits.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(call callUUID: UUID, digits: String, type: CXPlayDTMFCallAction.ActionType)
```

#### Return Value

#### Discussion

A new action for the specified call UUID, type, and digits.

## Parameters

- `callUUID`: The unique identifier for the associated   object.
- `digits`: A sequence of digits.
- `type`: The type of the call action. For possible values, see  .

## See Also

- [init?(coder: NSCoder)](cxplaydtmfcallaction/init(coder:).md)
  Creates a new action to play dual-tone multifrequency (DTMF) tones with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/init(call:digits:type:))*