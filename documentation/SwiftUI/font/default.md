# default

**Framework**: SwiftUI  
**Kind**: property

The effective SwiftUI font used in any given environment.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static var `default`: Font { get }
```

#### Discussion

The font specified by environment, preferring first any developer spedified font, via [`font`](environmentvalues/font.md), then any framework specified font, and finally the default SwiftUI font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/default)*