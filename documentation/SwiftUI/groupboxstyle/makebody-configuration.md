# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a view representing the body of a group box.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Discussion

SwiftUI calls this method for each instance of [`GroupBox`](groupbox.md) created within a view hierarchy where this style is the current group box style.

## Parameters

- `configuration`: The properties of the group box instance being   created.

## See Also

- [GroupBoxStyle.Configuration](groupboxstyle/configuration.md)
  The properties of a group box instance.
- [associatedtype Body : View](groupboxstyle/body.md)
  A view that represents the body of a group box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupboxstyle/makebody(configuration:))*