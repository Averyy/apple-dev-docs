# tabTitle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A short title that describes the content of the tab.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var tabTitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * tabTitle;
```

## Discussion

CarPlay only uses the title when the template is a root-template of a tab bar, otherwise setting this property has no effect.

## See Also

### Accessing Tab Information
- [var tabImage: UIImage?](./tabimage.md)
  An image that represents the content of the tab.
- [var tabSystemItem: UITabBarItem.SystemItem](./tabsystemitem.md)
  A system object that provides a title and image for common tab content, such as contacts or favorites.
- [var showsTabBadge: Bool](./showstabbadge.md)
  An indicator you use to call attention to the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplate/tabtitle)*