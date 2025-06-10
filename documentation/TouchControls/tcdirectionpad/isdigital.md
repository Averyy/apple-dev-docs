# isDigital

**Framework**: Touch Controls  
**Kind**: property

A Boolean value that indicates whether the control behaves as a digital button.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var isDigital: Bool { get set }
```

#### Discussion

If `YES`, dpad buttons will report 1 or 0. Ignored if radial is set, as button presses will always be digital.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontrols/tcdirectionpad/isdigital)*