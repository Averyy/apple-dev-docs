# init(_:destination:)

**Framework**: SwiftUI  
**Kind**: init

Creates a navigation link that presents a destination view, with a text label that the link generates from a localized string key.

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
init(_ titleKey: LocalizedStringKey, @ViewBuilder destination: () -> Destination)
```

## Parameters

- `titleKey`: A localized string key for creating a text label.
- `destination`: A view for the navigation link to present.

## See Also

- [init(destination:label:)](navigationlink/init(destination:label:).md)
  Creates a navigation link that presents the destination view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:destination:))*