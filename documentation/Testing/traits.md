# Traits

**Framework**: Swift Testing

Annotate test functions and suites, and customize their behavior.

#### Overview

Pass built-in traits to test functions or suite types to comment, categorize, classify, and modify the runtime behavior of test suites and test functions. Implement the [`TestTrait`](testtrait.md), and [`SuiteTrait`](suitetrait.md) protocols to create your own types that customize the behavior of your tests.

## Topics

### Customizing runtime behaviors
- [Enabling and disabling tests](enablinganddisabling.md)
  Conditionally enable or disable individual tests before they run.
- [Limiting the running time of tests](limitingexecutiontime.md)
  Set limits on how long a test can run for until it fails.
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
- [static func timeLimit(TimeLimitTrait.Duration) -> Self](trait/timelimit(_:).md)
  Construct a time limit trait that causes a test to time out if it runs for too long.
### Running tests serially or in parallel
- [Running tests serially or in parallel](parallelization.md)
  Control whether tests run serially or in parallel.
- [static var serialized: ParallelizationTrait](trait/serialized.md)
  A trait that serializes the test to which it is applied.
### Annotating tests
- [Adding tags to tests](addingtags.md)
  Use tags to provide semantic information for organization, filtering, and customizing appearances.
- [Adding comments to tests](addingcomments.md)
  Add comments to provide useful information about tests.
- [Associating bugs with tests](associatingbugs.md)
  Associate bugs uncovered or verified by tests.
- [Interpreting bug identifiers](bugidentifiers.md)
  Examine how the testing library interprets bug identifiers provided by developers.
- [macro Tag()](tag().md)
  Declare a tag that can be applied to a test function or test suite.
- [static func bug(String, Comment?) -> Self](trait/bug(_:_:).md)
  Constructs a bug to track with a test.
- [static func bug(String?, id: String, Comment?) -> Self](trait/bug(_:id:_:)-10yf5.md)
  Constructs a bug to track with a test.
- [static func bug(String?, id: some Numeric, Comment?) -> Self](trait/bug(_:id:_:)-3vtpl.md)
  Constructs a bug to track with a test.
### Handling issues
- [static func compactMapIssues((Issue) -> Issue?) -> Self](trait/compactmapissues(_:).md)
  Constructs an trait that transforms issues recorded by a test.
- [static func filterIssues((Issue) -> Bool) -> Self](trait/filterissues(_:).md)
  Constructs a trait that filters issues recorded by a test.
### Creating custom traits
- [protocol Trait](trait.md)
  A protocol describing traits that can be added to a test function or to a test suite.
- [protocol TestTrait](testtrait.md)
  A protocol describing a trait that you can add to a test function.
- [protocol SuiteTrait](suitetrait.md)
  A protocol describing a trait that you can add to a test suite.
- [protocol TestScoping](testscoping.md)
  A protocol that tells the test runner to run custom code before or after it runs a test suite or test function.
### Supporting types
- [struct Bug](bug.md)
  A type that represents a bug report tracked by a test.
- [struct Comment](comment.md)
  A type that represents a comment related to a test.
- [struct ConditionTrait](conditiontrait.md)
  A type that defines a condition which must be satisfied for the testing library to enable a test.
- [struct IssueHandlingTrait](issuehandlingtrait.md)
  A type that allows transforming or filtering the issues recorded by a test.
- [struct ParallelizationTrait](parallelizationtrait.md)
  A type that defines whether the testing library runs this test serially or in parallel.
- [struct Tag](tag.md)
  A type representing a tag that can be applied to a test.
- [struct List](tag/list.md)
  A type representing one or more tags applied to a test.
- [struct TimeLimitTrait](timelimittrait.md)
  A type that defines a time limit to apply to a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/traits)*