# init(nibName:bundle:)

**Framework**: UIKit  
**Kind**: init

Returns a newly initialized view controller with the nib file in the specified bundle.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?)
```

#### Return Value

A newly initialized [`UICollectionViewController`](uicollectionviewcontroller.md) object.

#### Discussion

For more information on how to initialize a view controller from a nib file, see [`init(nibName:bundle:)`](uiviewcontroller/init(nibname:bundle:).md).

## Parameters

- `nibNameOrNil`: The name of the nib file to associate with the view controller. The nib file name shouldn’t contain any leading path information. If you specify  , the   property is set to  .
- `nibBundleOrNil`: The bundle in which to search for the nib file. This method looks for the nib file in the bundle’s language-specific project directories first, followed by the Resources directory.

## See Also

- [init(collectionViewLayout: UICollectionViewLayout)](uicollectionviewcontroller/init(collectionviewlayout:).md)
  Initializes a collection view controller and configures the collection view with the provided layout.
- [init?(coder: NSCoder)](uicollectionviewcontroller/init(coder:).md)
  Creates a collection view controller with the nib file in the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/init(nibname:bundle:))*