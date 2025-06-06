# init(frame:collectionViewLayout:)

**Framework**: UIKit  
**Kind**: init

Creates a collection view object with the specified frame and layout.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(frame: CGRect, collectionViewLayout layout: UICollectionViewLayout)
```

#### Return Value

An initialized collection view object, or `nil` if the object couldn’t be created.

#### Discussion

Use this method when initializing a collection view object programmatically.

This method is the designated initializer.

## Parameters

- `frame`: The frame rectangle for the collection view, measured in points. The origin of the frame is relative to the superview in which you plan to add it. This frame is passed to the superclass during initialization.
- `layout`: The layout object to use for organizing items. The collection view stores a strong reference to the specified object. Must not be  .

## See Also

- [init?(coder: NSCoder)](uicollectionview/init(coder:).md)
  Creates a collection view object from data in a given unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/init(frame:collectionviewlayout:))*