# autoenablesItems

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the button enables and disables its items every time a user event occurs.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autoenablesItems: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), user events cause the button to enable and disable its items automatically according to the NSMenuValidation protocol specification.

## See Also

- [var pullsDown: Bool](nspopupbutton/pullsdown.md)
  A Boolean value indicating whether the button displays a pull-down or pop-up menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/autoenablesitems)*