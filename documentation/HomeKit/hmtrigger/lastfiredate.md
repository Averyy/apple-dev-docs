# lastFireDate

**Framework**: HomeKit  
**Kind**: property

The last time this trigger fired.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var lastFireDate: Date? { get }
```

#### Discussion

`nil` if the trigger has never fired.

## See Also

- [var name: String](hmtrigger/name.md)
  The name of the trigger.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmtrigger/updatename(_:completionhandler:).md)
  Updates the name of the trigger.
- [var isEnabled: Bool](hmtrigger/isenabled.md)
  State of the trigger.
- [func enable(Bool, completionHandler: ((any Error)?) -> Void)](hmtrigger/enable(_:completionhandler:).md)
  Changes the enabled state of the trigger.
- [var uniqueIdentifier: UUID](hmtrigger/uniqueidentifier.md)
  A unique identifier for this trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger/lastfiredate)*