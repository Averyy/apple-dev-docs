# Trait

**Framework**: Swift Testing  
**Kind**: protocol

A protocol describing traits that can be added to a test function or to a test suite.

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
protocol Trait : Sendable
```

#### Overview

The testing library defines a number of traits that can be added to test functions and to test suites. Define your own traits by creating types that conform to [`TestTrait`](testtrait.md) or [`SuiteTrait`](suitetrait.md):

You can add a trait that conforms to both [`TestTrait`](testtrait.md) and [`SuiteTrait`](suitetrait.md) to test functions and test suites.

## Topics

### Enabling and disabling tests
- [static func enabled(if: @autoclosure () throws -> Bool, Comment?, sourceLocation: SourceLocation) -> Self](trait/enabled(if:_:sourcelocation:).md)
  Constructs a condition trait that disables a test if it returns `false`.
- [static func enabled(Comment?, sourceLocation: SourceLocation, () async throws -> Bool) -> Self](trait/enabled(_:sourcelocation:_:).md)
  Constructs a condition trait that disables a test if it returns `false`.
- [static func disabled(Comment?, sourceLocation: SourceLocation) -> Self](trait/disabled(_:sourcelocation:).md)
  Constructs a condition trait that disables a test unconditionally.
- [static func disabled(if: @autoclosure () throws -> Bool, Comment?, sourceLocation: SourceLocation) -> Self](trait/disabled(if:_:sourcelocation:).md)
  Constructs a condition trait that disables a test if its value is true.
- [static func disabled(Comment?, sourceLocation: SourceLocation, () async throws -> Bool) -> Self](trait/disabled(_:sourcelocation:_:).md)
  Constructs a condition trait that disables a test if its value is true.
### Controlling how tests are run
- [static func timeLimit(TimeLimitTrait.Duration) -> Self](trait/timelimit(_:).md)
  Construct a time limit trait that causes a test to time out if it runs for too long.
- [static var serialized: ParallelizationTrait](trait/serialized.md)
  A trait that serializes the test to which it is applied.
### Categorizing tests and adding information
- [static func tags(Tag...) -> Self](trait/tags(_:).md)
  Construct a list of tags to apply to a test.
- [var comments: [Comment]](trait/comments.md)
  The user-provided comments for this trait.
### Associating bugs
- [static func bug(String, Comment?) -> Self](trait/bug(_:_:).md)
  Constructs a bug to track with a test.
- [static func bug(String?, id: String, Comment?) -> Self](trait/bug(_:id:_:)-10yf5.md)
  Constructs a bug to track with a test.
- [static func bug(String?, id: some Numeric, Comment?) -> Self](trait/bug(_:id:_:)-3vtpl.md)
  Constructs a bug to track with a test.
### Running code before and after a test or suite
- [protocol TestScoping](testscoping.md)
  A protocol that tells the test runner to run custom code before or after it runs a test suite or test function.
- [func scopeProvider(for: Test, testCase: Test.Case?) -> Self.TestScopeProvider?](trait/scopeprovider(for:testcase:).md)
  Get this trait’s scope provider for the specified test and optional test case.
- [associatedtype TestScopeProvider : TestScoping = Never](trait/testscopeprovider.md)
  The type of the test scope provider for this trait.
- [func prepare(for: Test) async throws](trait/prepare(for:).md)
  Prepare to run the test that has this trait.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [SuiteTrait](suitetrait.md)
- [TestTrait](testtrait.md)
### Conforming Types
- [Bug](bug.md)
- [Comment](comment.md)
- [ConditionTrait](conditiontrait.md)
- [ParallelizationTrait](parallelizationtrait.md)
- [Tag.List](tag/list.md)
- [TimeLimitTrait](timelimittrait.md)

## See Also

- [protocol TestTrait](testtrait.md)
  A protocol describing a trait that you can add to a test function.
- [protocol SuiteTrait](suitetrait.md)
  A protocol describing a trait that you can add to a test suite.
- [protocol TestScoping](testscoping.md)
  A protocol that tells the test runner to run custom code before or after it runs a test suite or test function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/trait)*