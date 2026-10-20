# indentationLevel

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The level of indentation for the cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var indentationLevel: Int { get set }
```

```objc
@property (nonatomic) NSInteger indentationLevel;
```

#### Discussion

The indentation level sets automatically when you use a hierarchical data source, such as an [`NSDiffableDataSourceSectionSnapshot`](../nsdiffabledatasourcesectionsnapshot-swift.struct.md).

## See Also

### Customizing layout
- [var indentationWidth: CGFloat](./indentationwidth.md)
  The width of an indentation level.
- [var indentsAccessories: Bool](./indentsaccessories.md)
  A Boolean value that detemines whether the cell indents accessories on the leading side.
- [var separatorLayoutGuide: UILayoutGuide](./separatorlayoutguide.md)
  A guide for laying out separators in relation to the primary content in the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/indentationlevel)*