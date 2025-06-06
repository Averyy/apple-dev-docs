# tags(_:)

**Framework**: Swift Testing  
**Kind**: method

Construct a list of tags to apply to a test.

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
static func tags(_ tags: Tag...) -> Self
```

## Mentions

- [Organizing test functions with suite types](organizingtests.md)
- [Defining test functions](definingtests.md)
- [Adding tags to tests](addingtags.md)

#### Return Value

An instance of [`Tag.List`](tag/list.md) containing the specified tags.

## Parameters

- `tags`: The list of tags to apply to the test.

## See Also

- [var comments: [Comment]](trait/comments.md)
  The user-provided comments for this trait.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/trait/tags(_:))*