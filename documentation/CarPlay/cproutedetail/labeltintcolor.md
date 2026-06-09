# labelTintColor

**Framework**: CarPlay  
**Kind**: property

The labelTintColor to apply to the label.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var labelTintColor: UIColor? { get set }
```

#### Discussion

The system requires a dynamic color that adapts to appearance changes. Static colors without light and dark variants fall back to the system default label color. Alpha components are ignored and all colors render at full opacity.

dynamic colors that adapt to light and dark appearances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/labeltintcolor)*