# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a view that represents the body of a table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Discussion

The system calls this method for each [`Table`](table.md) instance in a view hierarchy where this style is the current table style.

## Parameters

- `configuration`: The properties of the table.

## See Also

- [TableStyle.Configuration](tablestyle/configuration.md)
  The properties of a table.
- [associatedtype Body : View](tablestyle/body.md)
  A view that represents the body of a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablestyle/makebody(configuration:))*