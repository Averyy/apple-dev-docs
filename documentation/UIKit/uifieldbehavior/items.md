# items

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The dynamic items associated with the current field behavior.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var items: [any UIDynamicItem] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<id<UIDynamicItem>> * items;
```

## Discussion

When it is enabled, the current field applies its behavior to all of the items in the array.

## See Also

### Managing the associated dynamic items
- [func addItem(any UIDynamicItem)](./additem%28_%29.md)
  Associates the field behavior with the specified dynamic item.
- [func removeItem(any UIDynamicItem)](./removeitem%28_%29.md)
  Removes the field behavior from the specified dynamic item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/items)*