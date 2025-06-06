# UINib

**Framework**: UIKit  
**Kind**: class

An object that contains Interface Builder nib files.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UINib
```

#### Overview

A [`UINib`](uinib.md) object caches the contents of a nib file in memory, ready for unarchiving and instantiation. When your app needs to instantiate the contents of the nib file, it can do so without having to load the data from the nib file first, which improves performance. The [`UINib`](uinib.md) object can automatically release this cached nib data to free up memory for your app under low-memory conditions, reloading that data the next time your app instantiates the nib.

Your app should use [`UINib`](uinib.md) objects whenever it needs to repeatedly instantiate the same nib data. For example, if your table view uses a nib file to instantiate table view cells, caching the nib in a [`UINib`](uinib.md) object can improve performance.

When you create a [`UINib`](uinib.md) object using the contents of a nib file, the object loads the object graph in the referenced nib file, but it doesn’t unarchive it yet. To unarchive all of the nib data and instantiate the nib, your app calls the [`instantiate(withOwner:options:)`](uinib/instantiate(withowner:options:).md) method. For more information about the steps that the [`UINib`](uinib.md) object follows to instantiate the nib’s object graph, see [`Resource Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Introduction/Introduction.html#//apple_ref/doc/uid/10000051i).

## Topics

### Creating a nib object
- [init(nibName: String, bundle: Bundle?)](uinib/init(nibname:bundle:).md)
  Returns a nib object from the nib file in the specified bundle.
- [init(data: Data, bundle: Bundle?)](uinib/init(data:bundle:).md)
  Creates a nib object from nib data stored in memory.
### Retrieving objects from the nib file
- [func instantiate(withOwner: Any?, options: [UINib.OptionsKey : Any]?) -> [Any]](uinib/instantiate(withowner:options:).md)
  Unarchives and instantiates the in-memory contents of the nib object’s nib file, creating a distinct object tree and set of top-level objects.
- [struct OptionsKey](uinib/optionskey.md)
  Options that specify how to unarchive and instantiate the nib.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinib)*