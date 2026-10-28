# attributedTitle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The title for the window tab, specified as an attributed string.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@NSCopying
var attributedTitle: NSAttributedString? { get set }
```

```objc
@property (copy, nullable) NSAttributedString * attributedTitle;
```

## Discussion

If you provide an attributed title, the window tab uses all of the attributes that are explicitly provided in the attributed string. Attributes that are left unspecified, including the font and foreground color, are automatically filled in using default values appropriate for the window tab.

If the [`attributedTitle`](./attributedtitle.md) property is nil, the window tab uses the [`title`](./title.md) property instead. The default value is [`nil`](../../ObjectiveC/nil-227m0.md).

## See Also

### Customizing the Title
- [var title: String!](./title.md)
  The title for the window tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtab/attributedtitle)*