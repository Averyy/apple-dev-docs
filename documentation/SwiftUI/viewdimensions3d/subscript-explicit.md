# subscript(explicit:)

**Framework**: SwiftUI  
**Kind**: subscript

Gets the explicit value of the given depth alignment guide

**Availability**:
- visionOS 1.0+

## Declaration

```swift
subscript(explicit guide: DepthAlignment) -> CGFloat? { get }
```

#### Overview

Find the depth offset of a particular guide in the corresponding view by using that guide as an index to read from the context:

```swift
.alignmentGuide(.front) { context in
    context[.front] - 10
}
```

This subscript returns `nil` if no value exists for the guide.

For information about using subscripts in Swift to access member elements of a collection, list, or, sequence, see [`Subscripts`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Subscripts.html) in .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewdimensions3d/subscript(explicit:))*