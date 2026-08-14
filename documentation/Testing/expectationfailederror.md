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
- [Error](../swift/error.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct Expectation](expectation.md)
  A type describing an expectation that has been evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/expectationfailederror)*