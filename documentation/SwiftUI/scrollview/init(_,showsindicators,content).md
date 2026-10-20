# init(_:showsIndicators:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new instance that’s scrollable in the direction of the given axis and can show indicators while scrolling.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use the ScrollView(_:content:) initializer and the scrollIndicators(:_) modifier

## Declaration

```swift
nonisolated
init(_ axes: Axis.Set = .vertical, showsIndicators: Bool = true, @ContentBuilder content: () -> Content)
```

## Parameters

- `axes`: The scroll view’s scrollable axis. The default axis is the vertical axis.
- `showsIndicators`: A Boolean value that indicates whether the scroll view displays the scrollable component of the content offset, in a way suitable for the platform. The default value for this parameter is `true`.
- `content`: The content builder that creates the scrollable view.

## See Also

### Creating a scroll view
- [init(Axis.Set, content: () -> Content)](./init%28_,content%29.md)
  Creates a new instance that’s scrollable in the direction of the given axis and can show indicators while scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollview/init(_:showsindicators:content:))*