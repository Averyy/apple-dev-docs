# KeyPress.Phases

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [static let down: KeyPress.Phases](./phases/down.md)
  The user pressed down on a key.
- [static let up: KeyPress.Phases](./phases/up.md)
  The user released a key.
- [static let `repeat`: KeyPress.Phases](./phases/repeat.md)
  The user held a key down to issue a sequence of repeating events.
- [static let all: KeyPress.Phases](./phases/all.md)
  A value that matches all key press phases.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting the phase of the keypress
- [let phase: KeyPress.Phases](./phase.md)
  The phase of the key-press event (`.down`, `.repeat`, or `.up`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keypress/phases)*