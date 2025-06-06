# init(destination:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a navigation link that presents the destination view.

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
init(@ViewBuilder destination: () -> Destination, @ViewBuilder label: () -> Label)
```

## Mentions

- [Understanding the navigation stack](understanding-the-composition-of-navigation-stack.md)

## Parameters

- `destination`: A view for the navigation link to present.
- `label`: A view builder to produce a label describing the    to present.

## See Also

- [init(_:destination:)](navigationlink/init(_:destination:).md)
  Creates a navigation link that presents a destination view, with a text label that the link generates from a localized string key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(destination:label:))*