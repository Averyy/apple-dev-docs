# Trait Implementations

**Framework**: Swift Testing

## Topics

### Instance Properties
- [var comments: [Comment]](parallelizationtrait/comments.md)
  The user-provided comments for this trait.
### Instance Methods
- [func prepare(for: Test) async throws](parallelizationtrait/prepare(for:).md)
  Prepare to run the test that has this trait.
- [func scopeProvider(for: Test, testCase: Test.Case?) -> Never?](parallelizationtrait/scopeprovider(for:testcase:).md)
  Get this trait’s scope provider for the specified test or test case.
### Type Properties
- [static var serialized: ParallelizationTrait](parallelizationtrait/serialized.md)
  A trait that serializes the test to which it is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/parallelizationtrait/trait-implementations)*