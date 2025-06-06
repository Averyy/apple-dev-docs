# cgColor

**Framework**: AppKit  
**Kind**: property

The Core Graphics color object corresponding to the color.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var cgColor: CGColor { get }
```

#### Discussion

This property always contains a valid color, even though the value may be an approximation in some cases. There is no guaranteed round-trip color fidelity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/cgcolor)*