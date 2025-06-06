# summary

**Framework**: ClassKit  
**Kind**: property

An optional, user-visible description of the context.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var summary: String? { get set }
```

#### Discussion

The Schoolwork app may display this string to help the user understand the kinds of activities the context provides.

Localize the summary string, and limit its length to 4,000 characters.

## See Also

- [var identifier: String](clscontext/identifier.md)
  A string that uniquely identifies a context among its siblings.
- [var title: String](clscontext/title.md)
  The name of the context as it appears to users.
- [var thumbnail: CGImage?](clscontext/thumbnail.md)
  An optional thumbnail image associated with the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/summary)*