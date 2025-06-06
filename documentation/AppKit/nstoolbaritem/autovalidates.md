# autovalidates

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the toolbar automatically validates the item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
var autovalidates: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the toolbar automatically validates the item; otherwise, it doesn’t validate the item automatically. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func validate()](nstoolbaritem/validate.md)
  Validates the toolbar item’s menu and its ability to perfrom its action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/autovalidates)*