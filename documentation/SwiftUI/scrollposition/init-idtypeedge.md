# init(idType:edge:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new scroll position to be scrolled to the provided edge.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(idType: (some Hashable & Sendable).Type = Never.self, edge: Edge)
```

#### Discussion

You can provide a type to indicate the type of ID the scroll view should look for views with an ID of that type within its scroll target layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollposition/init(idtype:edge:))*