# pressureChange(with:)

**Framework**: AppKit  
**Kind**: method

Indicates a pressure change as the result of a user input event on a system that supports pressure sensitivity.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
@MainActor
func pressureChange(with event: NSEvent)
```

#### Discussion

This method is invoked automatically in response to user actions. `event` is the event that initiated the change in pressure.

## Parameters

- `event`: An   object encapsulating information about the event that invoked the change in pressure.

## See Also

- [class NSEvent](nsevent.md)
  An object that contains information about an input action, such as a mouse click or a key press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/pressurechange(with:))*