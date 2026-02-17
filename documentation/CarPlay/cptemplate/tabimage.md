# tabImage

**Framework**: CarPlay  
**Kind**: property

An image that represents the content of the tab.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var tabImage: UIImage? { get set }
```

#### Discussion

This image has precedence over any system item that [`tabSystemItem`](cptemplate/tabsystemitem.md) specifies, and CarPlay only uses it when the template is a root-template of a tab bar.

## See Also

- [var tabTitle: String?](cptemplate/tabtitle.md)
  A short title that describes the content of the tab.
- [var tabSystemItem: UITabBarItem.SystemItem](cptemplate/tabsystemitem.md)
  A system object that provides a title and image for common tab content, such as contacts or favorites.
- [var showsTabBadge: Bool](cptemplate/showstabbadge.md)
  An indicator you use to call attention to the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplate/tabimage)*