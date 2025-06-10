# UICollectionViewTransitionLayout

**Framework**: UIKit  
**Kind**: class

A special type of layout object that lets you implement behaviors when changing from one layout to another in your collection view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewTransitionLayout
```

#### Overview

You can use [`UICollectionViewTransitionLayout`](uicollectionviewtransitionlayout.md) as-is or subclass it to provide specialized behavior for your app. A common use for transition layouts is to create interactive transitions, such as those that are driven by gesture recognizers or touch events.

During a layout change, the collection view installs this layout object temporarily to manage the changeover. This layout object determines the layout of each item by interpolating between the layout values in the current and new layout objects. The interpolation is driven by the value in the [`transitionProgress`](uicollectionviewtransitionlayout/transitionprogress.md) property, which you update periodically from your code to drive the transition. For example, if you use this class in conjunction with a gesture recognizer, the handler for your gesture recognizer would update that property and invalidate the layout.

If you want to provide more than just a linear transition from the old to new layout over time, you need to subclass and provide the layout attributes for items yourself. Subclassing requires you to override all of the same methods you would override when subclassing [`UICollectionViewLayout`](uicollectionviewlayout.md). The difference is that your custom methods can work with your gesture recognizers or touch event code to change the layout based on input from the user. For example, you could use a custom layout object in conjunction with a gesture recognizer to make items track the location of the user’s finger on the screen. You also need to implement the [`collectionView(_:transitionLayoutForOldLayout:newLayout:)`](uicollectionviewdelegate/collectionview(_:transitionlayoutforoldlayout:newlayout:).md) method of your collection view delegate and return your custom layout object when asked for it.

## Topics

### Initializing the transition layout object
- [init(currentLayout: UICollectionViewLayout, nextLayout: UICollectionViewLayout)](uicollectionviewtransitionlayout/init(currentlayout:nextlayout:).md)
  Initializes and returns a transition layout object.
- [init?(coder: NSCoder)](uicollectionviewtransitionlayout/init(coder:).md)
  Creates a transition layout object from data in an unarchiver.
### Updating the transition information
- [var transitionProgress: CGFloat](uicollectionviewtransitionlayout/transitionprogress.md)
  The completion percentage of the transition.
- [func updateValue(CGFloat, forAnimatedKey: String)](uicollectionviewtransitionlayout/updatevalue(_:foranimatedkey:).md)
  Sets the value for an animatable key.
- [func value(forAnimatedKey: String) -> CGFloat](uicollectionviewtransitionlayout/value(foranimatedkey:).md)
  Returns the most recently set value for the specified key.
### Accessing the layout objects
- [var currentLayout: UICollectionViewLayout](uicollectionviewtransitionlayout/currentlayout.md)
  The collection view’s current layout object.
- [var nextLayout: UICollectionViewLayout](uicollectionviewtransitionlayout/nextlayout.md)
  The collection view’s new layout object.

## Relationships

### Inherits From
- [UICollectionViewLayout](uicollectionviewlayout.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Customizing collection view layouts](customizing-collection-view-layouts.md)
  Customize a view layout by changing the size of cells in the flow or implementing a mosaic style.
- [class UICollectionViewLayout](uicollectionviewlayout.md)
  An abstract base class for generating layout information for a collection view.
- [class UICollectionViewFlowLayout](uicollectionviewflowlayout.md)
  A layout object that organizes items into a grid with optional header and footer views for each section.
- [class UICollectionViewLayoutAttributes](uicollectionviewlayoutattributes.md)
  A layout object that manages the layout-related attributes for a given item in a collection view.
- [class UICollectionViewFlowLayoutInvalidationContext](uicollectionviewflowlayoutinvalidationcontext.md)
  A set of properties for determining whether to recompute the size of items or their position in the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout)*