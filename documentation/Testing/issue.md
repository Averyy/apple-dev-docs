# Issue

**Framework**: Swift Testing  
**Kind**: struct

A type describing a failure or warning which occurred during a test.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
struct Issue
```

## Mentions

- [Associating bugs with tests](associatingbugs.md)
- [Interpreting bug identifiers](bugidentifiers.md)

## Topics

### Instance Properties
- [var comments: [Comment]](issue/comments.md)
  Any comments provided by the developer and associated with this issue.
- [var error: (any Error)?](issue/error.md)
  The error which was associated with this issue, if any.
- [var kind: Issue.Kind](issue/kind-swift.property.md)
  The kind of issue this value represents.
- [var sourceLocation: SourceLocation?](issue/sourcelocation.md)
  The location in source where this issue occurred, if available.
### Type Methods
- [static func record(any Error, Comment?, sourceLocation: SourceLocation) -> Issue](issue/record(_:_:sourcelocation:).md)
  Record a new issue when a running test unexpectedly catches an error.
- [static func record(Comment?, sourceLocation: SourceLocation) -> Issue](issue/record(_:sourcelocation:).md)
  Record an issue when a running test fails unexpectedly.
### Enumerations
- [Issue.Kind](issue/kind-swift.enum.md)
  Kinds of issues which may be recorded.
### Default Implementations
- [CustomDebugStringConvertible Implementations](issue/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](issue/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue)*