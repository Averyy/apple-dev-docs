# attributedTitle

**Framework**: AppKit  
**Kind**: property

The title for the window tab, specified as an attributed string.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@NSCopying
var attributedTitle: NSAttributedString? { get set }
```

#### Discussion

If you provide an attributed title, the window tab uses all of the attributes that are explicitly provided in the attributed string. Attributes that are left unspecified, including the font and foreground color, are automatically filled in using default values appropriate for the window tab.

If the [`attributedTitle`](nswindowtab/attributedtitle.md) property is nil, the window tab uses the [`title`](nswindowtab/title.md) property instead. The default value is [`Nil`](https://developer.apple.com/documentation/objectivec/nil).

## See Also

- [var title: String!](nswindowtab/title.md)
  The title for the window tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtab/attributedtitle)*