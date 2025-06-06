# Expectation

**Framework**: Swift Testing  
**Kind**: struct

A type describing an expectation that has been evaluated.

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
struct Expectation
```

## Topics

### Instance Properties
- [var isPassing: Bool](expectation/ispassing.md)
  Whether the expectation passed or failed.
- [var isRequired: Bool](expectation/isrequired.md)
  Whether or not the expectation was required to pass.
- [var sourceLocation: SourceLocation](expectation/sourcelocation.md)
  The source location where this expectation was evaluated.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct ExpectationFailedError](expectationfailederror.md)
  A type describing an error thrown when an expectation fails during evaluation.
- [protocol CustomTestStringConvertible](customteststringconvertible.md)
  A protocol describing types with a custom string representation when presented as part of a test’s output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/expectation)*