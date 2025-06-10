# ExpectationFailedError

**Framework**: Swift Testing  
**Kind**: struct

A type describing an error thrown when an expectation fails during evaluation.

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
struct ExpectationFailedError
```

#### Overview

The testing library throws instances of this type when the `#require()` macro records an issue.

## Topics

### Instance Properties
- [var expectation: Expectation](expectationfailederror/expectation.md)
  The expectation that failed.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Expectation](expectation.md)
  A type describing an expectation that has been evaluated.
- [protocol CustomTestStringConvertible](customteststringconvertible.md)
  A protocol describing types with a custom string representation when presented as part of a test’s output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/expectationfailederror)*