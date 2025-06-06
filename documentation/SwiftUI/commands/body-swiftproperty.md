# body

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The contents of the command hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@CommandsBuilder
@MainActor @preconcurrency var body: Self.Body { get }
```

#### Discussion

For any commands that you create, provide a computed `body` property that defines the scene as a composition of other scenes. You can assemble a command hierarchy from built-in commands that SwiftUI provides, as well as other commands that you’ve defined.

## See Also

- [associatedtype Body : Commands](commands/body-swift.associatedtype.md)
  The type of commands that represents the body of this command hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commands/body-swift.property)*