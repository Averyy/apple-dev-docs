# attribute(of:)

**Framework**: RoomPlan  
**Kind**: method

Checks an object for specific attribute types.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func attribute<T>(of attributeType: T.Type) -> T? where T : CapturedRoomAttribute
```

#### Discussion

This function provides details about an object based on attribute type. For example, the following code checks whether an object the framework observes during a scan resembles a dining table:

```swift
let chairType = object.attribute(of: ChairType.self)
if chairType == .dining { /* ... */ }
```

## See Also

- [var attributes: [any CapturedRoomAttribute]](capturedroom/object/attributes.md)
  A collection of details that describe a particular object in the room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/object/attribute(of:))*