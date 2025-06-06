# isEnabled

**Framework**: HomeKit  
**Kind**: property

State of the trigger.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isEnabled: Bool { get }
```

#### Discussion

Triggers that are not enabled never fire.

## See Also

- [var name: String](hmtrigger/name.md)
  The name of the trigger.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmtrigger/updatename(_:completionhandler:).md)
  Updates the name of the trigger.
- [func enable(Bool, completionHandler: ((any Error)?) -> Void)](hmtrigger/enable(_:completionhandler:).md)
  Changes the enabled state of the trigger.
- [var lastFireDate: Date?](hmtrigger/lastfiredate.md)
  The last time this trigger fired.
- [var uniqueIdentifier: UUID](hmtrigger/uniqueidentifier.md)
  A unique identifier for this trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger/isenabled)*