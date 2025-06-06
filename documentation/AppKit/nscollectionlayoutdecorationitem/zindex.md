# zIndex

**Framework**: AppKit  
**Kind**: property

The vertical stacking order of the decoration item in relation to other items in the section.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
var zIndex: Int { get set }
```

#### Discussion

The default value of this property is `0`, which means the decoration item appears below all other items in the section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutdecorationitem/zindex)*