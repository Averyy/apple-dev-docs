# NSCollectionViewTransitionLayout

**Framework**: Appkit  
**Kind**: class

An object that implements custom behaviors when changing from one layout to another in a collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
class NSCollectionViewTransitionLayout
```

#### Overview

Transition layout objects are commonly used to implement interactive transitions between layouts, where the transition itself is driven by a gesture recognizer.

> **Note**:  In macOS 10.11, collection views do not provide built-in support for driving layout transitions.

## Topics

### Initializing the Transition Layout Object
- [init(currentLayout: NSCollectionViewLayout, nextLayout: NSCollectionViewLayout)](nscollectionviewtransitionlayout/init(currentlayout:nextlayout:).md)
  Initializes and returns the transition layout object.
### Updating the Transition Information
- [var transitionProgress: CGFloat](nscollectionviewtransitionlayout/transitionprogress.md)
  The completion percentage of the transition.
- [func updateValue(CGFloat, forAnimatedKey: NSCollectionViewTransitionLayout.AnimatedKey)](nscollectionviewtransitionlayout/updatevalue(_:foranimatedkey:).md)
  Sets the value of a key whose value you use during the animation.
- [func value(forAnimatedKey: NSCollectionViewTransitionLayout.AnimatedKey) -> CGFloat](nscollectionviewtransitionlayout/value(foranimatedkey:).md)
  Returns the most recently set value for the specified key.
- [NSCollectionViewTransitionLayout.AnimatedKey](nscollectionviewtransitionlayout/animatedkey.md)
### Accessing the Layout Objects
- [var currentLayout: NSCollectionViewLayout](nscollectionviewtransitionlayout/currentlayout.md)
  The collection view’s current layout object.
- [var nextLayout: NSCollectionViewLayout](nscollectionviewtransitionlayout/nextlayout.md)
  The collection view’s new layout object.

## Relationships

### Inherits From
- [NSCollectionViewLayout](nscollectionviewlayout.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Implementing modern collection views](../UIKit/implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [class NSCollectionViewFlowLayout](nscollectionviewflowlayout.md)
  A layout that organizes items into a flexible and configurable arrangement.
- [protocol NSCollectionViewDelegateFlowLayout](nscollectionviewdelegateflowlayout.md)
  A set of methods that a delegate implements to provide layout information to a flow layout object in a collection view.
- [class NSCollectionViewGridLayout](nscollectionviewgridlayout.md)
  A layout that displays a single section of items in a row and column grid.
- [class NSCollectionViewLayoutAttributes](nscollectionviewlayoutattributes.md)
  An object that contains layout-related attributes for an element in a collection view.
- [class NSCollectionViewLayout](nscollectionviewlayout.md)
  An abstract base class that you subclass and use to generate layout information for a collection view.
- [class NSCollectionViewCompositionalLayout](nscollectionviewcompositionallayout.md)
  A layout object that lets you combine items in highly adaptive and flexible visual arrangements.
- [class NSCollectionViewCompositionalLayoutConfiguration](nscollectionviewcompositionallayoutconfiguration.md)
  An object that defines scroll direction, section spacing, and headers or footers for the layout.
- [typealias NSCollectionViewCompositionalLayoutSectionProvider](nscollectionviewcompositionallayoutsectionprovider.md)
  A closure that creates and returns each of the layout’s sections.
- [enum NSCollectionLayoutSectionOrthogonalScrollingBehavior](nscollectionlayoutsectionorthogonalscrollingbehavior.md)
  The scrolling behavior of the layout’s sections in relation to the main layout axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nscollectionviewtransitionlayout)*