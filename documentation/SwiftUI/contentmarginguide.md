# ContentMarginGuide

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A guide for resolving the content margins for a view.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
struct ContentMarginGuide
```

## Overview

Apply a guide to a view with the [`contentMargins(for:edges:alignment:)`](./view/contentmargins%28for,edges,alignment%29.md) modifier, or read its value from a [`GeometryProxy`](./geometryproxy.md). SwiftUI provides [`container`](./contentmarginguide/container.md).

## Topics

### Getting the container
- [static var container: ContentMarginGuide](./contentmarginguide/container.md)
  The margins of the container the view is in.

## See Also

### Setting margins
- [func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View](./view/contentmargins%28_,for%29.md)
  Configures the content margin for a provided placement.
- [func contentMargins(_:_:for:)](./view/contentmargins%28_,_,for%29.md)
  Configures the content margin for a provided placement.
- [struct ContentMarginPlacement](./contentmarginplacement.md)
  The placement of margins.
- [func contentMargins(for: ContentMarginGuide, edges: Edge.Set, alignment: Alignment?) -> some View](./view/contentmargins%28for,edges,alignment%29.md)
  Insets the content of this view by a content margin guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentmarginguide)*