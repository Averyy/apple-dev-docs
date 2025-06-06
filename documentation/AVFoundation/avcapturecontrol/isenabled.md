# isEnabled

**Framework**: Avfoundation  
**Kind**: property

A Boolean value that indicates whether this control supports user interaction.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

Controls support user interaction by default. You can temporarily disable user interaction on a control without removing it from a capture session by setting it’s enabled state to `false`.

The default value is `true`.

> **Note**:  Apps can programmatically change the value of a control while in a disabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturecontrol/isenabled)*