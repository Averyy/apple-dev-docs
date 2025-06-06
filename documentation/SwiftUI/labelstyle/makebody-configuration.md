# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a view that represents the body of a label.

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

The system calls this method for each [`Label`](label.md) instance in a view hierarchy where this style is the current label style.

## Parameters

- `configuration`: The properties of the label.

## See Also

- [LabelStyle.Configuration](labelstyle/configuration.md)
  The properties of a label.
- [associatedtype Body : View](labelstyle/body.md)
  A view that represents the body of a label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labelstyle/makebody(configuration:))*