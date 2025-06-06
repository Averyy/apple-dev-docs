# SuiteTrait

**Framework**: Swift Testing  
**Kind**: protocol

A protocol describing a trait that you can add to a test suite.

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
protocol SuiteTrait : Trait
```

#### Overview

The testing library defines a number of traits that you can add to test suites. You can also define your own traits by creating types that conform to this protocol, or to the [`TestTrait`](testtrait.md) protocol.

## Topics

### Instance Properties
- [var isRecursive: Bool](suitetrait/isrecursive.md)
  Whether this instance should be applied recursively to child test suites and test functions.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [Trait](trait.md)
### Conforming Types
- [Bug](bug.md)
- [Comment](comment.md)
- [ConditionTrait](conditiontrait.md)
- [ParallelizationTrait](parallelizationtrait.md)
- [Tag.List](tag/list.md)
- [TimeLimitTrait](timelimittrait.md)

## See Also

- [protocol Trait](trait.md)
  A protocol describing traits that can be added to a test function or to a test suite.
- [protocol TestTrait](testtrait.md)
  A protocol describing a trait that you can add to a test function.
- [protocol TestScoping](testscoping.md)
  A protocol that tells the test runner to run custom code before or after it runs a test suite or test function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/suitetrait)*