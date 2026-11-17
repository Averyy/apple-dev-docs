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

## Discussion

The value in this property never exceeds the maximum number of items, as set in the [`maximumItemCount`](./maximumitemcount.md) property. If you initialize or update the list with more items than the allowed maximum, CarPlay adds items until it reaches the maximum and discards the rest.

## See Also

### Getting item details
- [func indexPath(for: any CPListTemplateItem) -> IndexPath?](./indexpath%28for%29.md)
  Returns the index path for the specified item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/itemcount)*