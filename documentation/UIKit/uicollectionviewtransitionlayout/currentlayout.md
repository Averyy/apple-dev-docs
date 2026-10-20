# currentLayout

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The collection view’s current layout object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var currentLayout: UICollectionViewLayout { get }
```

```objc
@property (nonatomic, readonly) UICollectionViewLayout * currentLayout;
```

#### Discussion

This object provides the layout attributes representing the initial position of items in the collection view. If you ultimately cancel the transition, the collection view animates its items back to the positions provided by this object.

## See Also

### Accessing the layout objects
- [var nextLayout: UICollectionViewLayout](./nextlayout.md)
  The collection view’s new layout object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/currentlayout)*