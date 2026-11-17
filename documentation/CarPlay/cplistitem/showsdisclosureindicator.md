# showsDisclosureIndicator

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

If YES, a cell displaying this list item will render with a disclosure indicator in the trailing side of the cell.

**Availability**:
- iOS 12.0+ - Deprecated in 14.0 (renamed: CPListItemAccessoryType)
- iPadOS 12.0+ - Deprecated in 14.0 (renamed: CPListItemAccessoryType)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: CPListItemAccessoryType)

## Declaration

```swift
var showsDisclosureIndicator: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL showsDisclosureIndicator;
```

## Discussion

> **Note**: If set, this property takes precedence over showsCloudLabel.

Defaults to NO.

## See Also

### Deprecated
- [init(text: String?, detailText: String?, image: UIImage?, showsDisclosureIndicator: Bool)](./init%28text,detailtext,image,showsdisclosureindicator%29.md)
  Initialize a list item with text, detailtext, an image, and a disclosure indicator.
- [var showsExplicitLabel: Bool](./showsexplicitlabel.md)
  If YES, a cell displaying this list item will render with an explicit label to the trailing edge of the text


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/showsdisclosureindicator)*