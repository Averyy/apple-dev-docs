# title

**Framework**: AppKit  
**Kind**: property

The title for the window tab.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var title: String! { get set }
```

#### Discussion

The title displays within the window tab when the associated window is part of a tabbing group.

By default, the title of the window tab follows the title of its associated window, but it may be customized using the [`title`](nswindowtab/title.md) property. If the title has been customized, setting the [`title`](nswindowtab/title.md) property to [`nil`](https://developer.apple.com/documentation/objectivec/nil) causes it to follow the window’s title again.

## See Also

- [var attributedTitle: NSAttributedString?](nswindowtab/attributedtitle.md)
  The title for the window tab, specified as an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtab/title)*