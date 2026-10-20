# updateVisibleMenu(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the currently visible menu.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func updateVisibleMenu(_ block: (UIMenu) -> UIMenu)
```

```objc
- (void) updateVisibleMenuWithBlock:(UIMenu * (^)(UIMenu *visibleMenu)) block;
```

## Parameters

- `block`: A mutable copy of the menu.

## See Also

### Managing menu interactions
- [func dismissMenu()](./dismissmenu%28%29.md)
  Dismisses the context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteraction/updatevisiblemenu(_:))*