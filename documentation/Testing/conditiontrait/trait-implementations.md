# Trait Implementations

**Framework**: Swift Testing

## Topics

### Instance Methods
- [func scopeProvider(for: Test, testCase: Test.Case?) -> Never?](conditiontrait/scopeprovider(for:testcase:).md)
  Get this trait’s scope provider for the specified test or test case.
### Type Methods
- [static func disabled(Comment?, sourceLocation: SourceLocation) -> Self](conditiontrait/disabled(_:sourcelocation:).md)
  Constructs a condition trait that disables a test unconditionally.
- [static func disabled(Comment?, sourceLocation: SourceLocation, () async throws -> Bool) -> Self](conditiontrait/disabled(_:sourcelocation:_:).md)
  Constructs a condition trait that disables a test if its value is true.
- [static func disabled(if: @autoclosure () throws -> Bool, Comment?, sourceLocation: SourceLocation) -> Self](conditiontrait/disabled(if:_:sourcelocation:).md)
  Constructs a condition trait that disables a test if its value is true.
- [static func enabled(Comment?, sourceLocation: SourceLocation, () async throws -> Bool) -> Self](conditiontrait/enabled(_:sourcelocation:_:).md)
  Constructs a condition trait that disables a test if it returns `false`.
- [static func enabled(if: @autoclosure () throws -> Bool, Comment?, sourceLocation: SourceLocation) -> Self](conditiontrait/enabled(if:_:sourcelocation:).md)
  Constructs a condition trait that disables a test if it returns `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/conditiontrait/trait-implementations)*