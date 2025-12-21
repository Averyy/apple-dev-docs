# default

**Framework**: SwiftUI  
**Kind**: property

The effective SwiftUI font used in any given environment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static var `default`: Font { get }
```

#### Discussion

The font specified by environment, preferring first any developer spedified font, via [`font`](environmentvalues/font.md), then any framework specified font, and finally the default SwiftUI font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/default)*