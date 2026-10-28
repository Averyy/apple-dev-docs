# tabImage

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An image that represents the content of the tab.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var tabImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * tabImage;
```

## Discussion

This image has precedence over any system item that [`tabSystemItem`](./tabsystemitem.md) specifies, and CarPlay only uses it when the template is a root-template of a tab bar.

## See Also

### Accessing Tab Information
- [var tabTitle: String?](./tabtitle.md)
  A short title that describes the content of the tab.
- [var tabSystemItem: UITabBarItem.SystemItem](./tabsystemitem.md)
  A system object that provides a title and image for common tab content, such as contacts or favorites.
- [var showsTabBadge: Bool](./showstabbadge.md)
  An indicator you use to call attention to the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplate/tabimage)*