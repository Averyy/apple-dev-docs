# symbols

**Framework**: SwiftUI  
**Kind**: property

A view that provides child views that you can use in the drawing callback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var symbols: Symbols
```

#### Discussion

Uniquely tag each child view using the `View/tag(_:)` modifier, so that you can find them from within your renderer using the [`resolveSymbol(id:)`](graphicscontext/resolvesymbol(id:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/canvas/symbols)*