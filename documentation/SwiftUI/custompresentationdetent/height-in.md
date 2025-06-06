# height(in:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Calculates and returns a height based on the context.

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
static func height(in context: Self.Context) -> CGFloat?
```

#### Return Value

The height of the detent, or `nil` if the detent should be inactive based on the `contenxt` input.

## Parameters

- `context`: Information that can help to determine the   height of the detent.

## See Also

- [CustomPresentationDetent.Context](custompresentationdetent/context.md)
  Information that you can use to calculate the height of a custom detent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/custompresentationdetent/height(in:))*