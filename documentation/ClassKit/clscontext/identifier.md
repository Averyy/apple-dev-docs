# identifier

**Framework**: ClassKit  
**Kind**: property

A string that uniquely identifies a context among its siblings.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var identifier: String { get }
```

#### Discussion

All contexts with a given parent context must have different identifiers. No such requirement exists for contexts that have different parent contexts. So, for example, the `chapter-1` and `chapter-2` contexts can each have child contexts with the identifier `section-1`, but `chapter-1` can’t have two contexts with that identifier.

## See Also

- [var title: String](clscontext/title.md)
  The name of the context as it appears to users.
- [var summary: String?](clscontext/summary.md)
  An optional, user-visible description of the context.
- [var thumbnail: CGImage?](clscontext/thumbnail.md)
  An optional thumbnail image associated with the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/identifier)*