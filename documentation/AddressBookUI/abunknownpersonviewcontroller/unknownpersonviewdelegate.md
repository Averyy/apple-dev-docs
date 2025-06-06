# unknownPersonViewDelegate

**Framework**: Address Book UI  
**Kind**: property

The unknown-person view controller delegate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
unowned(unsafe) var unknownPersonViewDelegate: (any ABUnknownPersonViewControllerDelegate)? { get set }
```

#### Discussion

The delegate must adopt the [`ABUnknownPersonViewControllerDelegate`](abunknownpersonviewcontrollerdelegate.md) protocol.

## See Also

- [protocol ABUnknownPersonViewControllerDelegate](abunknownpersonviewcontrollerdelegate.md)
  The methods you use to respond to events in an unknown person view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/unknownpersonviewdelegate)*