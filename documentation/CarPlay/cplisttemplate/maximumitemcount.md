# maximumItemCount

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum number of items, across all sections, that the template can display.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class var maximumItemCount: Int { get }
```

```objc
@property (class, nonatomic, readonly) NSUInteger maximumItemCount;
```

## Discussion

This property’s value is dependent on any user interface limits that the vehicle imposes. See [`CPSessionConfiguration`](../cpsessionconfiguration.md) for more information. At runtime, use this value to determine the maximum number of items, across all sections, that your list can display.

## See Also

### Getting Supplementary Information
- [var itemCount: Int](./itemcount.md)
  The total number of items, across all sections, in the list.
- [func indexPath(for: any CPListTemplateItem) -> IndexPath?](./indexpath%28for%29.md)
  Returns the index path for the specified item.
- [var title: String?](./title.md)
  The title that the navigation bar displays when the template is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/maximumitemcount)*