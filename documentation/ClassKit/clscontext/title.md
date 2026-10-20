# title

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

The name of the context as it appears to users.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var title: String { get set }
```

```objc
@property (nonatomic, copy) NSString * title;
```

#### Discussion

The title that you choose appears to teachers exactly as you store it. If your app works in many locales, localize the title. The framework doesn’t do that for you automatically.

## See Also

### Identifying the context
- [var identifier: String](./identifier.md)
  A string that uniquely identifies a context among its siblings.
- [var summary: String?](./summary.md)
  An optional, user-visible description of the context.
- [var thumbnail: CGImage?](./thumbnail.md)
  An optional thumbnail image associated with the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/title)*