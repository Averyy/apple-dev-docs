# uniqueIdentifier

**Framework**: HomeKit  
**Kind**: property

A unique identifier for this trigger.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var uniqueIdentifier: UUID { get }
```

## See Also

- [var name: String](hmtrigger/name.md)
  The name of the trigger.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmtrigger/updatename(_:completionhandler:).md)
  Updates the name of the trigger.
- [var isEnabled: Bool](hmtrigger/isenabled.md)
  State of the trigger.
- [func enable(Bool, completionHandler: ((any Error)?) -> Void)](hmtrigger/enable(_:completionhandler:).md)
  Changes the enabled state of the trigger.
- [var lastFireDate: Date?](hmtrigger/lastfiredate.md)
  The last time this trigger fired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger/uniqueidentifier)*