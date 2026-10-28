# toolTip

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tooltip for this window tab.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var toolTip: String! { get set }
```

```objc
@property (copy, null_resettable) NSString * toolTip;
```

## Discussion

By default, the window tab’s tooltip displays its [`title`](./title.md) string. Once customized, setting the [`toolTip`](./tooltip.md) property to [`nil`](../../ObjectiveC/nil-227m0.md) causes it to follow the [`title`](./title.md) property again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtab/tooltip)*