# Tag()

**Framework**: Swift Testing  
**Kind**: macro  
**Role**: Macro

Declare a tag that can be applied to a test function or test suite.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
@attached
(accessor) @attached(peer) macro Tag()
```

## Mentions

- [Adding tags to tests](./addingtags.md)

#### Overview

Use this tag with members of the [`Tag`](./tag.md) type declared in an extension to mark them as usable with tests. For more information on declaring tags, see [Adding tags to tests](./addingtags.md).

## See Also

### Annotating tests
- [Adding tags to tests](./addingtags.md)
  Use tags to provide semantic information for organization, filtering, and customizing appearances.
- [Adding comments to tests](./addingcomments.md)
  Add comments to provide useful information about tests.
- [Associating bugs with tests](./associatingbugs.md)
  Associate bugs uncovered or verified by tests.
- [Interpreting bug identifiers](./bugidentifiers.md)
  Examine how the testing library interprets bug identifiers provided by developers.
- [static func bug(String, Comment?) -> Self](./trait/bug%28_,_%29.md)
  Constructs a bug to track with a test.
- [static func bug(String?, id: String, Comment?) -> Self](./trait/bug%28_,id,_%29-10yf5.md)
  Constructs a bug to track with a test.
- [static func bug(String?, id: some Numeric, Comment?) -> Self](./trait/bug%28_,id,_%29-3vtpl.md)
  Constructs a bug to track with a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/tag())*