# forceInput

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

Get the input containing the measured force applied to the button.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var forceInput: (any GCLinearInput)? { get }
```

#### Discussion

Some buttons feature load cells (also known as button force transducers) capable of measuring applied mechanical force.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcbuttonelement/forceinput)*