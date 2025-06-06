# custom(_:)

**Framework**: SwiftUI  
**Kind**: method

A custom detent with a calculated height.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func custom<D>(_ type: D.Type) -> PresentationDetent where D : CustomPresentationDetent
```

## See Also

- [static func fraction(CGFloat) -> PresentationDetent](presentationdetent/fraction(_:).md)
  A custom detent with the specified fractional height.
- [static func height(CGFloat) -> PresentationDetent](presentationdetent/height(_:).md)
  A custom detent with the specified height.
- [PresentationDetent.Context](presentationdetent/context.md)
  Information that you use to calculate the presentation’s height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationdetent/custom(_:))*