# toolTip

**Framework**: AppKit  
**Kind**: property

The tooltip for this window tab.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var toolTip: String! { get set }
```

#### Discussion

By default, the window tab’s tooltip displays its [`title`](nswindowtab/title.md) string. Once customized, setting the [`toolTip`](nswindowtab/tooltip.md) property to [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) causes it to follow the [`title`](nswindowtab/title.md) property again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtab/tooltip)*