# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

Gets the value of the given vertical guide.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
subscript(guide: VerticalAlignment) -> CGFloat { get }
```

**Other overloads**:

```swift
subscript(guide: DepthAlignment) -> CGFloat { get }
```

```swift
subscript(guide: HorizontalAlignment) -> CGFloat { get }
```

## Overview

Find the offset of a particular guide in the corresponding view by using that guide as an index to read from the context:

```swift
.alignmentGuide(.top) { context in
    context[.top] - 10
}
```

For information about using subscripts in Swift to access member elements of a collection, list, or, sequence, see [Subscripts](https://docs.swift.org/swift-book/LanguageGuide/Subscripts.html) in *The Swift Programming Language*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewdimensions3d/subscript(_:)-or72)*