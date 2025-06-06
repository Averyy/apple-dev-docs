# init(_:showsIndicators:content:)

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
init(_ axes: Axis.Set = .vertical, showsIndicators: Bool = true, @ViewBuilder content: () -> Content)
```

## Parameters

- `axes`: The scroll view’s scrollable axis. The default axis is the   vertical axis.
- `showsIndicators`: A Boolean value that indicates whether the scroll   view displays the scrollable component of the content offset, in a way   suitable for the platform. The default value for this parameter is   .
- `content`: The view builder that creates the scrollable view.

## See Also

- [init(Axis.Set, content: () -> Content)](scrollview/init(_:content:).md)
  Creates a new instance that’s scrollable in the direction of the given axis and can show indicators while scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollview/init(_:showsindicators:content:))*