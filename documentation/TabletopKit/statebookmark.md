# StateBookmark

**Framework**: TabletopKit  
**Kind**: struct

A snapshot of the game state at a point in time.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct StateBookmark
```

#### Overview

Add bookmarks between turns so that you can jump to a prior turn and continue gameplay from there. When you jump to a bookmark, you reset the game state back to that point in time.

To add a bookmark, use the [`createBookmark(_:context:)`](tabletopaction/createbookmark(_:context:).md) or similar method. To jump to a bookmark, use the [`jumpToBookmark(_:)`](tabletopgame/jumptobookmark(_:).md) or similar method.

## Topics

### Initializing bookmarks
- [init(id: StateBookmark.ID)](statebookmark/init(id:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct StateBookmarkIdentifier](statebookmarkidentifier.md)
  A unique identifier for bookmarks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/statebookmark)*