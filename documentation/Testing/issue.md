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
- [var isFailure: Bool](issue/isfailure.md)
  Whether or not this issue should cause the test it’s associated with to be considered a failure.
- [var kind: Issue.Kind](issue/kind-swift.property.md)
  The kind of issue this value represents.
- [var severity: Issue.Severity](issue/severity-swift.property.md)
  The severity of this issue.
- [var sourceLocation: SourceLocation?](issue/sourcelocation.md)
  The location in source where this issue occurred, if available.
### Type Methods
- [static func record(any Error, Comment?, sourceLocation: SourceLocation) -> Issue](issue/record(_:_:sourcelocation:).md)
  Record a new issue when a running test unexpectedly catches an error.
- [static func record(Comment?, severity: Issue.Severity, sourceLocation: SourceLocation) -> Issue](issue/record(_:severity:sourcelocation:).md)
  Records an issue that a test encounters while it’s running.
- [static func record(Comment?, sourceLocation: SourceLocation) -> Issue](issue/record(_:sourcelocation:).md)
  Records an issue that a test encounters while it’s running.
### Enumerations
- [Issue.Kind](issue/kind-swift.enum.md)
  Kinds of issues which may be recorded.
- [Issue.Severity](issue/severity-swift.enum.md)
  An enumeration representing the level of severity of a recorded issue.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue)*