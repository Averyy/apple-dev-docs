# Body

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

The type of commands that represents the body of this command hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
associatedtype Body : Commands
```

#### Discussion

When you create custom commands, Swift infers this type from your implementation of the required [`body`](commands/body-swift.property.md) property.

## See Also

- [var body: Self.Body](commands/body-swift.property.md)
  The contents of the command hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commands/body-swift.associatedtype)*