# Trait Implementations

**Framework**: Swift Testing

## Topics

### Instance Properties
- [var comments: [Comment]](timelimittrait/comments.md)
  The user-provided comments for this trait.
### Instance Methods
- [func prepare(for: Test) async throws](timelimittrait/prepare(for:).md)
  Prepare to run the test that has this trait.
- [func scopeProvider(for: Test, testCase: Test.Case?) -> Never?](timelimittrait/scopeprovider(for:testcase:).md)
  Get this trait’s scope provider for the specified test or test case.
### Type Methods
- [static func timeLimit(TimeLimitTrait.Duration) -> Self](timelimittrait/timelimit(_:).md)
  Construct a time limit trait that causes a test to time out if it runs for too long.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/timelimittrait/trait-implementations)*