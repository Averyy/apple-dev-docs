# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a view representing the body of a gauge.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Discussion

The system calls this modifier on each instance of gauge within a view hierarchy where this style is the current gauge style.

## Parameters

- `configuration`: The properties to apply to the gauge instance.

## See Also

- [GaugeStyle.Configuration](gaugestyle/configuration.md)
  The properties of a gauge instance.
- [associatedtype Body : View](gaugestyle/body.md)
  A view representing the body of a gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gaugestyle/makebody(configuration:))*