# enable(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Changes the enabled state of the trigger.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func enable(_ enable: Bool) async throws
```

#### Discussion

Triggers can only be enabled when they are in a home. You add triggers to a home using the [`addTrigger(_:completionHandler:)`](hmhome/addtrigger(_:completionhandler:).md) method of [`HMHome`](hmhome.md).

When a trigger is enabled its firing conditions are checked for validity and the system starts tracking the trigger and when it will next fire.

In addition to having valid firing conditions, to be successfully enabled a trigger must have at least one action set associated with it, and every action set associated with the trigger must have at least one action.

## Parameters

- `enable`:   to enable the trigger,   to disable it.
- `completion`: The block executed after the request is processed.

## See Also

- [var name: String](hmtrigger/name.md)
  The name of the trigger.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmtrigger/updatename(_:completionhandler:).md)
  Updates the name of the trigger.
- [var isEnabled: Bool](hmtrigger/isenabled.md)
  State of the trigger.
- [var lastFireDate: Date?](hmtrigger/lastfiredate.md)
  The last time this trigger fired.
- [var uniqueIdentifier: UUID](hmtrigger/uniqueidentifier.md)
  A unique identifier for this trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger/enable(_:completionhandler:))*