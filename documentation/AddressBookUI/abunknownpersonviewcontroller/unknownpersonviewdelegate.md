# unknownPersonViewDelegate

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

The unknown-person view controller delegate.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use +[CNContactViewController viewControllerForUnknownContact:] from ContactsUI.framework instead

## Declaration

```swift
unowned(unsafe) var unknownPersonViewDelegate: (any ABUnknownPersonViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<ABUnknownPersonViewControllerDelegate> unknownPersonViewDelegate;
```

## Discussion

The delegate must adopt the [`ABUnknownPersonViewControllerDelegate`](../abunknownpersonviewcontrollerdelegate.md) protocol.

## See Also

### Responding to View Controller Interactions
- [protocol ABUnknownPersonViewControllerDelegate](../abunknownpersonviewcontrollerdelegate.md)
  The methods you use to respond to events in an unknown person view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/unknownpersonviewdelegate)*