# adaptsToUserAccentColor

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the tint configuration alters its effect based on the user’s preferred accent color choice.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var adaptsToUserAccentColor: Bool { get }
```

#### Discussion

When this property is `YES`, the tint configuration alters it effect based on the user’s preferred accent color. Otherwise, the tint configuration produces a constant effect regardless of the accent color preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstintconfiguration/adaptstouseraccentcolor)*