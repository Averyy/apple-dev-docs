# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a view representing the body of a progress view.

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
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Discussion

The view hierarchy calls this method for each progress view where this style is the current progress view style.

## Parameters

- `configuration`: The properties of the progress view being   created.

## See Also

- [ProgressViewStyle.Configuration](progressviewstyle/configuration.md)
  A type alias for the properties of a progress view instance.
- [associatedtype Body : View](progressviewstyle/body.md)
  A view representing the body of a progress view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressviewstyle/makebody(configuration:))*