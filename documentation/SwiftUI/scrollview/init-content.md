# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new instance that’s scrollable in the direction of the given axis and can show indicators while scrolling.

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
nonisolated
init(_ axes: Axis.Set = .vertical, @ViewBuilder content: () -> Content)
```

## Parameters

- `axes`: The scroll view’s scrollable axis. The default axis is the   vertical axis.
- `content`: The view builder that creates the scrollable view.

## See Also

- [init(Axis.Set, showsIndicators: Bool, content: () -> Content)](scrollview/init(_:showsindicators:content:).md)
  Creates a new instance that’s scrollable in the direction of the given axis and can show indicators while scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollview/init(_:content:))*