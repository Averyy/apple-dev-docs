# RunLoop.Mode

**Framework**: Foundation  
**Kind**: struct

Modes that a run loop operates in.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Mode
```

#### Discussion

[`NSApplication`](https://developer.apple.com/documentation/AppKit/NSApplication) defines additional run loop modes, including the following:

- [`modalPanel`](runloop/mode/modalpanel.md)
- [`eventTracking`](runloop/mode/eventtracking.md)

## Topics

### System Run Loop Modes
- [static let common: RunLoop.Mode](runloop/mode/common.md)
  A pseudo-mode that includes one or more other run loop modes.
- [static let `default`: RunLoop.Mode](runloop/mode/default.md)
  The mode set to handle input sources other than connection objects.
- [static let eventTracking: RunLoop.Mode](runloop/mode/eventtracking.md)
  The mode set when tracking events modally, such as a mouse-dragging loop.
- [static let modalPanel: RunLoop.Mode](runloop/mode/modalpanel.md)
  The mode set when waiting for input from a modal panel, such as a save or open panel.
- [static let tracking: RunLoop.Mode](runloop/mode/tracking.md)
  The mode set while tracking in controls takes place.
### Run Loop Mode Creation
- [init(String)](runloop/mode/init(_:).md)
  Creates a run loop mode using the specified string value.
- [init(rawValue: String)](runloop/mode/init(rawvalue:).md)
  Creates a run loop mode using the specified raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class var current: RunLoop](runloop/current.md)
  Returns the run loop for the current thread.
- [var currentMode: RunLoop.Mode?](runloop/currentmode.md)
  The receiver’s current input mode.
- [func limitDate(forMode: RunLoop.Mode) -> Date?](runloop/limitdate(formode:).md)
  Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [class var main: RunLoop](runloop/main.md)
  Returns the run loop of the main thread.
- [func getCFRunLoop() -> CFRunLoop](runloop/getcfrunloop.md)
  Returns the receiver’s underlying run loop object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/mode)*