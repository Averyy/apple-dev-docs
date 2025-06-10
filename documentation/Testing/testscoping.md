# TestScoping

**Framework**: Swift Testing  
**Kind**: protocol

A protocol that tells the test runner to run custom code before or after it runs a test suite or test function.

**Availability**:
- Swift 6.1+
- Xcode 16.3+

## Declaration

```swift
protocol TestScoping : Sendable
```

#### Overview

Provide custom scope for tests by implementing the [`scopeProvider(for:testCase:)`](trait/scopeprovider(for:testcase:).md) method, returning a type that conforms to this protocol. Create a custom scope to consolidate common set-up and tear-down logic for tests which have similar needs, which allows each test function to focus on the unique aspects of its test.

## Topics

### Instance Methods
- [func provideScope(for: Test, testCase: Test.Case?, performing: () async throws -> Void) async throws](testscoping/providescope(for:testcase:performing:).md)
  Provide custom execution scope for a function call which is related to the specified test or test case.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [ParallelizationTrait](parallelizationtrait.md)

## See Also

- [protocol Trait](trait.md)
  A protocol describing traits that can be added to a test function or to a test suite.
- [protocol TestTrait](testtrait.md)
  A protocol describing a trait that you can add to a test function.
- [protocol SuiteTrait](suitetrait.md)
  A protocol describing a trait that you can add to a test suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/testscoping)*