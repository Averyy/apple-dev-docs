# thumbnail

**Framework**: ClassKit  
**Kind**: property

An optional thumbnail image associated with the context.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var thumbnail: CGImage? { get set }
```

#### Discussion

Schoolwork displays the thumbnail along with your content to help teachers and students more easily recognize a given context. For example, you could use a variation of your app icon for your main app context, an open book for a reading exercise, or a calculator to represent a math quiz. Create thumbnails that match the style of your app.

The image you provide should have at least 80 pixels on a side, and at most 330 pixels. ClassKit won’t use an image that’s too small, and automatically scales down an image that’s too large. For the best experience across all devices, use an image that’s close to or at the maximum dimensions.

## See Also

- [var identifier: String](clscontext/identifier.md)
  A string that uniquely identifies a context among its siblings.
- [var title: String](clscontext/title.md)
  The name of the context as it appears to users.
- [var summary: String?](clscontext/summary.md)
  An optional, user-visible description of the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/thumbnail)*