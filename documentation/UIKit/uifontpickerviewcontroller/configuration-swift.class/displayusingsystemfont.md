# displayUsingSystemFont

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether to use the system font for all font names in the font picker.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var displayUsingSystemFont: Bool { get set }
```

#### Discussion

By default, the font picker uses each font face to display that font face name in the font picker. Set this property to [`true`](https://developer.apple.com/documentation/swift/true) if you want the font picker to display all font names in the system font instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/displayusingsystemfont)*