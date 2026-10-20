# StateBookmark

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

A snapshot of the game state at a point in time.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct StateBookmark
```

#### Overview

Add bookmarks between turns so that you can jump to a prior turn and continue gameplay from there. When you jump to a bookmark, you reset the game state back to that point in time.

To add a bookmark, use the [`createBookmark(_:context:)`](./tabletopaction/createbookmark%28_,context%29.md) or similar method. To jump to a bookmark, use the [`jumpToBookmark(_:)`](./tabletopgame/jumptobookmark%28_%29.md) or similar method.

## Topics

### Initializing bookmarks
- [init(id: StateBookmark.ID)](./statebookmark/init%28id%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Bookmarks
- [struct StateBookmarkIdentifier](./statebookmarkidentifier.md)
  A unique identifier for bookmarks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/statebookmark)*