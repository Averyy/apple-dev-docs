# Trait Implementations

**Framework**: Swift Testing

## Topics

### Instance Properties
- [var comments: [Comment]](bug/comments.md)
  The user-provided comments for this trait.
### Instance Methods
- [func prepare(for: Test) async throws](bug/prepare(for:).md)
  Prepare to run the test that has this trait.
- [func scopeProvider(for: Test, testCase: Test.Case?) -> Never?](bug/scopeprovider(for:testcase:).md)
  Get this trait’s scope provider for the specified test or test case.
### Type Aliases
- [typealias TestScopeProvider](bug/testscopeprovider.md)
  The type of the test scope provider for this trait.
### Type Methods
- [static func bug(String, Comment?) -> Self](bug/bug(_:_:).md)
  Constructs a bug to track with a test.
- [static func bug(String?, id: String, Comment?) -> Self](bug/bug(_:id:_:)-5uinv.md)
  Constructs a bug to track with a test.
- [static func bug(String?, id: some Numeric, Comment?) -> Self](bug/bug(_:id:_:)-9jvpc.md)
  Constructs a bug to track with a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/bug/trait-implementations)*