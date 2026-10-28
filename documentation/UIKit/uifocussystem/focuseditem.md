# focusedItem

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The item that’s currently focused.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
weak var focusedItem: (any UIFocusItem)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<UIFocusItem> focusedItem;
```

## Discussion

If the current object or none of its children are focused, this property is set to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocussystem/focuseditem)*