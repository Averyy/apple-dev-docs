# isEnabled

**Framework**: CarPlay  
**Kind**: property

A Boolean value that indicates if the item is enabled.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var handler: ((any CPSelectableListItem, () -> Void) -> Void)?](cplistitem/handler.md)
  An optional closure that CarPlay invokes when the user selects the list item.
- [var userInfo: Any?](cplistitem/userinfo.md)
  An opaque value for the list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/isenabled)*