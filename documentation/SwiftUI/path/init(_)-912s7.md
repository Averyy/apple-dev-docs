# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a path containing a rectangle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(_ rect: CGRect)
```

**Other overloads**:

```swift
init(_ callback: (inout Path) -> ())
```

```swift
init(_ path: CGMutablePath)
```

```swift
init(_ path: CGPath)
```

```swift
init?(_ string: String)
```

## Discussion

This is a convenience function that creates a path of a rectangle. Using this convenience function is more efficient than creating a path and adding a rectangle to it.

Calling this function is equivalent to using `minX` and related properties to find the corners of the rectangle, then using the `move(to:)`, `addLine(to:)`, and `closeSubpath()` functions to add the rectangle.

## Parameters

- `rect`: The rectangle to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/init(_:)-912s7)*