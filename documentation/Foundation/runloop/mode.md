# RunLoop.Mode

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * NSRunLoopMode;
```

## Discussion

[`NSApplication`](../../AppKit/nsapplication.md) defines additional run loop modes, including the following:

- [`modalPanel`](./mode/modalpanel.md)
- [`eventTracking`](./mode/eventtracking.md)

## Topics

### System Run Loop Modes
- [static let common: RunLoop.Mode](./mode/common.md)
  A pseudo-mode that includes one or more other run loop modes.
- [static let `default`: RunLoop.Mode](./mode/default.md)
  The mode set to handle input sources other than connection objects.
- [static let eventTracking: RunLoop.Mode](./mode/eventtracking.md)
  The mode set when tracking events modally, such as a mouse-dragging loop.
- [static let modalPanel: RunLoop.Mode](./mode/modalpanel.md)
  The mode set when waiting for input from a modal panel, such as a save or open panel.
- [static let tracking: RunLoop.Mode](./mode/tracking.md)
  The mode set while tracking in controls takes place.
### Run Loop Mode Creation
- [init(String)](./mode/init%28_%29.md)
  Creates a run loop mode using the specified string value.
- [init(rawValue: String)](./mode/init%28rawvalue%29.md)
  Creates a run loop mode using the specified raw string value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Run Loops and Modes
- [class var current: RunLoop](./current.md)
  Returns the run loop for the current thread.
- [var currentMode: RunLoop.Mode?](./currentmode.md)
  The receiver’s current input mode.
- [func limitDate(forMode: RunLoop.Mode) -> Date?](./limitdate%28formode%29.md)
  Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [class var main: RunLoop](./main.md)
  Returns the run loop of the main thread.
- [func getCFRunLoop() -> CFRunLoop](./getcfrunloop%28%29.md)
  Returns the receiver’s underlying run loop object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/mode)*