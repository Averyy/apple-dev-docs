# tabSystemItem

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A system object that provides a title and image for common tab content, such as contacts or favorites.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var tabSystemItem: UITabBarItem.SystemItem { get set }
```

```objc
@property (nonatomic) UITabBarSystemItem tabSystemItem;
```

## Discussion

You should specify either a system item, or a tab title and tab image. The tab image has precedence over the system item if both properties are set.

CarPlay only uses this value when the template is a root-template of a tab bar.

## See Also

### Accessing Tab Information
- [var tabTitle: String?](./tabtitle.md)
  A short title that describes the content of the tab.
- [var tabImage: UIImage?](./tabimage.md)
  An image that represents the content of the tab.
- [var showsTabBadge: Bool](./showstabbadge.md)
  An indicator you use to call attention to the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplate/tabsystemitem)*