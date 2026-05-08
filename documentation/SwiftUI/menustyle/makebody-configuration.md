# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a view that represents the body of a menu.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Discussion

The system calls this method for each [`Menu`](menu.md) instance in a view hierarchy where this style is the current menu style.

## Parameters

- `configuration`: The properties of the menu.

## See Also

- [MenuStyle.Configuration](menustyle/configuration.md)
  The properties of a menu.
- [associatedtype Body : View](menustyle/body.md)
  A view that represents the body of a menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menustyle/makebody(configuration:))*