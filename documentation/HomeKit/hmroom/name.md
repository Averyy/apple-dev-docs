# name

**Framework**: HomeKit  
**Kind**: property

The name of the room.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String { get }
```

#### Discussion

Allow the user to choose room names. Room names must be unique within a home.

## See Also

- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmroom/updatename(_:completionhandler:).md)
  Updates the name of the room.
- [var uniqueIdentifier: UUID](hmroom/uniqueidentifier.md)
  The unique identifier for a room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmroom/name)*