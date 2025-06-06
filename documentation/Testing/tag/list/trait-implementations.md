# Trait Implementations

**Framework**: Swift Testing

## Topics

### Instance Properties
- [var comments: [Comment]](tag/list/comments.md)
  The user-provided comments for this trait.
### Instance Methods
- [func prepare(for: Test) async throws](tag/list/prepare(for:).md)
  Prepare to run the test that has this trait.
- [func scopeProvider(for: Test, testCase: Test.Case?) -> Never?](tag/list/scopeprovider(for:testcase:).md)
  Get this trait’s scope provider for the specified test or test case.
### Type Aliases
- [typealias TestScopeProvider](tag/list/testscopeprovider.md)
  The type of the test scope provider for this trait.
### Type Methods
- [static func tags(Tag...) -> Self](tag/list/tags(_:).md)
  Construct a list of tags to apply to a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/tag/list/trait-implementations)*