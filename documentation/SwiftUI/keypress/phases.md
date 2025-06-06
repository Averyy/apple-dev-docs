# KeyPress.Phases

**Framework**: SwiftUI  
**Kind**: struct

Options for matching different phases of a key-press event.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct Phases
```

## Topics

### Getting the phases
- [static let down: KeyPress.Phases](keypress/phases/down.md)
  The user pressed down on a key.
- [static let up: KeyPress.Phases](keypress/phases/up.md)
  The user released a key.
- [static let `repeat`: KeyPress.Phases](keypress/phases/repeat.md)
  The user held a key down to issue a sequence of repeating events.
- [static let all: KeyPress.Phases](keypress/phases/all.md)
  A value that matches all key press phases.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [let phase: KeyPress.Phases](keypress/phase.md)
  The phase of the key-press event (`.down`, `.repeat`, or `.up`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keypress/phases)*