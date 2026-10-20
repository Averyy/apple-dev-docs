# title

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The title that the navigation bar displays when the template is visible.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var title: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * title;
```

## See Also

### Getting Supplementary Information
- [class var maximumItemCount: Int](./maximumitemcount.md)
  The maximum number of items, across all sections, that the template can display.
- [var itemCount: Int](./itemcount.md)
  The total number of items, across all sections, in the list.
- [func indexPath(for: any CPListTemplateItem) -> IndexPath?](./indexpath%28for%29.md)
  Returns the index path for the specified item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/title)*