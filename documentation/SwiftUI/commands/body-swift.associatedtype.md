# Body

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
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

When you create custom commands, Swift infers this type from your implementation of the required [`body`](./body-swift.property.md) property.

## See Also

### Implementing commands
- [var body: Self.Body](./body-swift.property.md)
  The contents of the command hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commands/body-swift.associatedtype)*