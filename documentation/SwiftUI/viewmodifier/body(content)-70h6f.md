# body(content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Gets the current body of the caller.

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
@MainActor
@preconcurrency func body(content: Self.Content) -> Self.Body
```

Available when `Body` is `Never`.

## Discussion

`content` is a proxy for the view that will have the modifier represented by `Self` applied to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewmodifier/body(content:)-70h6f)*