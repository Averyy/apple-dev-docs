# autovalidates

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the toolbar automatically validates the item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
var autovalidates: Bool { get set }
```

```objc
@property BOOL autovalidates;
```

## Discussion

If the value of this property is [`true`](../../Swift/true.md), the toolbar automatically validates the item; otherwise, it doesn’t validate the item automatically. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Validating the item
- [func validate()](./validate%28%29.md)
  Validates the toolbar item’s menu and its ability to perfrom its action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/autovalidates)*