# updateName(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the name of the trigger.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateName(_ name: String) async throws
```

## Parameters

- `name`: The new name. Must be unique within the home.
- `completion`: The block executed after the request is processed.

## See Also

- [var name: String](hmtrigger/name.md)
  The name of the trigger.
- [var isEnabled: Bool](hmtrigger/isenabled.md)
  State of the trigger.
- [func enable(Bool, completionHandler: ((any Error)?) -> Void)](hmtrigger/enable(_:completionhandler:).md)
  Changes the enabled state of the trigger.
- [var lastFireDate: Date?](hmtrigger/lastfiredate.md)
  The last time this trigger fired.
- [var uniqueIdentifier: UUID](hmtrigger/uniqueidentifier.md)
  A unique identifier for this trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger/updatename(_:completionhandler:))*