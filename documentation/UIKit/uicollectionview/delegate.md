# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object that acts as the delegate of the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UICollectionViewDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UICollectionViewDelegate> delegate;
```

## Discussion

The delegate must adopt the [`UICollectionViewDelegate`](../uicollectionviewdelegate.md) protocol. The delegate object is responsible for managing selection behavior and interactions with individual items.

## See Also

### Managing collection view interactions
- [protocol UICollectionViewDelegate](../uicollectionviewdelegate.md)
  The methods adopted by the object you use to manage user interactions with items in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/delegate)*