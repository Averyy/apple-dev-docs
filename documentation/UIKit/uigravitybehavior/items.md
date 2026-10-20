# items

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The set of dynamic items associated with the gravity behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var items: [any UIDynamicItem] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<id<UIDynamicItem>> * items;
```

## See Also

### Managing a gravity behavior’s items
- [func addItem(any UIDynamicItem)](./additem%28_%29.md)
  Associates the specified dynamic item with the gravity behavior.
- [func removeItem(any UIDynamicItem)](./removeitem%28_%29.md)
  Removes the specified dynamic item from the gravity behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigravitybehavior/items)*