# init(collectionViewLayout:)

**Framework**: UIKit  
**Kind**: init

Initializes a collection view controller and configures the collection view with the provided layout.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(collectionViewLayout layout: UICollectionViewLayout)
```

#### Return Value

An initialized `UICollectionViewController` object or `nil` if the object could not be created.

## Parameters

- `layout`: The layout object to associate with the collection view. The layout controls how the collection view presents its cells and supplementary views.

## See Also

- [init(nibName: String?, bundle: Bundle?)](uicollectionviewcontroller/init(nibname:bundle:).md)
  Returns a newly initialized view controller with the nib file in the specified bundle.
- [init?(coder: NSCoder)](uicollectionviewcontroller/init(coder:).md)
  Creates a collection view controller with the nib file in the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/init(collectionviewlayout:))*