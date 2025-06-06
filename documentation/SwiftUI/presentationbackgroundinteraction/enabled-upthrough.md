# enabled(upThrough:)

**Framework**: SwiftUI  
**Kind**: method

People can interact with the view behind a presentation up through a specified detent.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
static func enabled(upThrough detent: PresentationDetent) -> PresentationBackgroundInteraction
```

#### Discussion

At detents larger than the one you specify, SwiftUI disables interaction.

## Parameters

- `detent`: The largest detent at which people can interact with   the view behind the presentation.

## See Also

- [static var automatic: PresentationBackgroundInteraction](presentationbackgroundinteraction/automatic.md)
  The default background interaction for the presentation.
- [static var disabled: PresentationBackgroundInteraction](presentationbackgroundinteraction/disabled.md)
  People can’t interact with the view behind a presentation.
- [static var enabled: PresentationBackgroundInteraction](presentationbackgroundinteraction/enabled.md)
  People can interact with the view behind a presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationbackgroundinteraction/enabled(upthrough:))*