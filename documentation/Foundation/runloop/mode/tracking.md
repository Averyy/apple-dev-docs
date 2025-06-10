# tracking

**Framework**: Foundation  
**Kind**: property

The mode set while tracking in controls takes place.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let tracking: RunLoop.Mode
```

#### Discussion

You can use this mode to add timers that fire during tracking.

## See Also

- [static let common: RunLoop.Mode](runloop/mode/common.md)
  A pseudo-mode that includes one or more other run loop modes.
- [static let `default`: RunLoop.Mode](runloop/mode/default.md)
  The mode set to handle input sources other than connection objects.
- [static let eventTracking: RunLoop.Mode](runloop/mode/eventtracking.md)
  The mode set when tracking events modally, such as a mouse-dragging loop.
- [static let modalPanel: RunLoop.Mode](runloop/mode/modalpanel.md)
  The mode set when waiting for input from a modal panel, such as a save or open panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/mode/tracking)*