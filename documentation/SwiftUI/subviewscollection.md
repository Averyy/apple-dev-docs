# SubviewsCollection

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

An opaque collection representing the subviews of view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct SubviewsCollection
```

#### Overview

Subviews collection constructs subviews on demand, so only access the part of the collection you need to create the resulting content.

You can get access to a view’s subview collection by using the `Group/init(sectionsOf:transform:)` initializer.

The collection’s elements are the pieces that make up the given view, and the collection as a whole acts as a proxy for the original view.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sequence](../Swift/sequence.md)
- [View](./view.md)

## See Also

### Accessing a container’s subviews
- [struct Subview](./subview.md)
  An opaque value representing a subview of another view.
- [struct SubviewsCollectionSlice](./subviewscollectionslice.md)
  A slice of a SubviewsCollection.
- [func containerValue<V>(WritableKeyPath<ContainerValues, V>, V) -> some View](./view/containervalue%28_,_%29.md)
  Sets a particular container value of a view.
- [struct ContainerValues](./containervalues.md)
  A collection of container values associated with a given view.
- [protocol ContainerValueKey](./containervaluekey.md)
  A key for accessing container values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/subviewscollection)*