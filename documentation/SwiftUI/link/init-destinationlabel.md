# init(destination:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a control, consisting of a URL and a label, used to navigate to the given URL.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(destination: URL, @ViewBuilder label: () -> Label)
```

## Parameters

- `destination`: The URL for the link.
- `label`: A view that describes the destination of URL.

## See Also

- [init(_:destination:)](link/init(_:destination:).md)
  Creates a control, consisting of a URL and a title key, used to navigate to a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/link/init(destination:label:))*