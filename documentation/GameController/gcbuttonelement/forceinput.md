# forceInput

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

Get the input containing the measured force applied to the button.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var forceInput: (any GCLinearInput)? { get }
```

#### Discussion

Some buttons feature load cells (also known as button force transducers) capable of measuring applied mechanical force.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcbuttonelement/forceinput)*