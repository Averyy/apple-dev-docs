# personViewDelegate

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

The person-view controller delegate.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactViewController`](../../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
unowned(unsafe) var personViewDelegate: (any ABPersonViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<ABPersonViewControllerDelegate> personViewDelegate;
```

## Discussion

The delegate must adopt the [`ABPersonViewControllerDelegate`](../abpersonviewcontrollerdelegate.md) protocol.

## See Also

### Responding to View Controller Interactions
- [protocol ABPersonViewControllerDelegate](../abpersonviewcontrollerdelegate.md)
  The `ABPersonViewControllerDelegate` protocol declares the interface that must be implemented by [`ABPersonViewController`](../abpersonviewcontroller.md) delegates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/personviewdelegate)*