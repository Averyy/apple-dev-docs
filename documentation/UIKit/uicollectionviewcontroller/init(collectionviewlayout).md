# init(collectionViewLayout:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a collection view controller and configures the collection view with the provided layout.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(collectionViewLayout layout: UICollectionViewLayout)
```

```objc
- (instancetype) initWithCollectionViewLayout:(UICollectionViewLayout *) layout;
```

#### Return Value

An initialized `UICollectionViewController` object or `nil` if the object could not be created.

## Parameters

- `layout`: The layout object to associate with the collection view. The layout controls how the collection view presents its cells and supplementary views.

## See Also

### Creating a collection view controller
- [init(nibName: String?, bundle: Bundle?)](./init%28nibname,bundle%29.md)
  Returns a newly initialized view controller with the nib file in the specified bundle.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a collection view controller with the nib file in the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/init(collectionviewlayout:))*