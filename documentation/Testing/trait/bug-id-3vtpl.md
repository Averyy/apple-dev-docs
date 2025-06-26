# bug(_:id:_:)

**Framework**: Swift Testing  
**Kind**: method

Constructs a bug to track with a test.

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
static func bug(_ url: String? = nil, id: some Numeric, _ title: Comment? = nil) -> Self
```

## Mentions

- [Interpreting bug identifiers](bugidentifiers.md)
- [Enabling and disabling tests](enablinganddisabling.md)
- [Associating bugs with tests](associatingbugs.md)

#### Return Value

An instance of [`Bug`](bug.md) that represents the specified bug.

## Parameters

- `url`: A URL that refers to this bug in the associated bug-tracking   system.
- `id`: The unique identifier of this bug in its associated bug-tracking   system.
- `title`: Optionally, the human-readable title of the bug.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/trait/bug(_:id:_:)-3vtpl)*