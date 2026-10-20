# titleAlignment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred alignment of the navigation bar’s title.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+

## Declaration

```swift
var titleAlignment: UINavigationItem.TitleAlignment { get set }
```

```objc
@property (nonatomic, assign, readwrite) UINavigationItemTitleAlignment titleAlignment;
```

#### Discussion

The navigation bar resolves the alignment of its title automatically based on context, and the navigation item’s style. Use this property to override the system default.

The alignment the bar actually used is reported by `UITraitCollection.navigationTitleAlignment`.

Defaults to `UINavigationItemTitleAlignmentAutomatic`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/titlealignment-swift.property)*