# titleAlignment

**Framework**: UIKit  
**Kind**: property

The preferred alignment of the navigation bar’s title.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)

## Declaration

```swift
var titleAlignment: UINavigationItem.TitleAlignment { get set }
```

#### Discussion

The navigation bar resolves the alignment of its title automatically based on context, and the navigation item’s style. Use this property to override the system default.

The alignment the bar actually used is reported by `UITraitCollection.navigationTitleAlignment`.

Defaults to `UINavigationItemTitleAlignmentAutomatic`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/titlealignment-swift.property)*