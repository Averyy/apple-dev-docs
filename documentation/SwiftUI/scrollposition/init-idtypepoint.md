# init(idType:point:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new scroll position to be scrolled to the provided point.

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
init(idType: (some Hashable & Sendable).Type = Never.self, point: CGPoint)
```

#### Discussion

You can provide a type to the scroll position. This type should match the type of IDs associated to views in a scroll target layout. The scroll view will look for those views to update the value of the scroll position with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollposition/init(idtype:point:))*