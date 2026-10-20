# newPersonViewDelegate

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

The delegate of a new-person view controller.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`delegate`](../../ContactsUI/cncontactviewcontroller/delegate.md) instead.

## Declaration

```swift
unowned(unsafe) var newPersonViewDelegate: (any ABNewPersonViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<ABNewPersonViewControllerDelegate> newPersonViewDelegate;
```

## See Also

### Responding to View Controller Interactions
- [protocol ABNewPersonViewControllerDelegate](../abnewpersonviewcontrollerdelegate.md)
  The `ABNewPersonViewControllerDelegate` protocol declares the interface that [`ABNewPersonViewController`](../abnewpersonviewcontroller.md) delegates must implement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/newpersonviewdelegate)*