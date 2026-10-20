# itemCount

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The total number of items, across all sections, in the list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var itemCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger itemCount;
```

#### Discussion

This value never exceeds [`maximumItemCount`](./maximumitemcount.md). If you initialize a list where the total number of items, across all sections, is greater than [`maximumItemCount`](./maximumitemcount.md), CarPlay only displays items up to this limit and discards the rest.

## See Also

### Getting Supplementary Information
- [class var maximumItemCount: Int](./maximumitemcount.md)
  The maximum number of items, across all sections, that the template can display.
- [func indexPath(for: any CPListTemplateItem) -> IndexPath?](./indexpath%28for%29.md)
  Returns the index path for the specified item.
- [var title: String?](./title.md)
  The title that the navigation bar displays when the template is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/itemcount)*