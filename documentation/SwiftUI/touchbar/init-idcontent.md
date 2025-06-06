# init(id:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a customizable Touch Bar view container with a globally unique identifier.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(id: String, @ViewBuilder content: () -> Content)
```

#### Discussion

Be sure that each view in `content` has an explicit `touchBarItemPresence` value with customization identifier.

## Parameters

- `id`: A globally unique identifier for this Touch Bar.
- `content`: A collection of views to be displayed by the Touch Bar.

## See Also

- [init(content: () -> Content)](touchbar/init(content:).md)
  Creates a non-customizable Touch Bar view container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/touchbar/init(id:content:))*