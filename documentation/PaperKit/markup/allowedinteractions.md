# allowedInteractions

**Framework**: PaperKit  
**Kind**: property  
**Required**: Yes

Interactions that people can perform on this markup.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var allowedInteractions: MarkupInteractions { get set }
```

#### Discussion

Use this to configure how people can interact with the markup, such as preventing resizing, rotation, or deletion. The default is `.all`, which allows all interactions. Set to `.readOnly` to prevent all modifications.

## See Also

- [struct MarkupInteractions](markupinteractions.md)
  Interactions that people can perform on markup elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markup/allowedinteractions)*