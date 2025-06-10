# init(currentLayout:nextLayout:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns a transition layout object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(currentLayout: UICollectionViewLayout, nextLayout newLayout: UICollectionViewLayout)
```

#### Return Value

An initialized transition layout object or `nil` if the object could not be created.

#### Discussion

This method initializes the transition layout object and saves references to the current and new layout objects so that you can access them later. If you subclass and implement your own initialization method, you must call this method to initialize the superclass.

## Parameters

- `currentLayout`: The layout object currently in use by the collection view.
- `newLayout`: The new layout object that is being installed into the collection view.

## See Also

- [init?(coder: NSCoder)](uicollectionviewtransitionlayout/init(coder:).md)
  Creates a transition layout object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/init(currentlayout:nextlayout:))*