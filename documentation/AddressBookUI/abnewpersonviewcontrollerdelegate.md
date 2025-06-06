# ABNewPersonViewControllerDelegate

**Framework**: Address Book UI  
**Kind**: protocol

The `ABNewPersonViewControllerDelegate` protocol declares the interface that [`ABNewPersonViewController`](abnewpersonviewcontroller.md) delegates must implement.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 14.0+

## Declaration

```swift
protocol ABNewPersonViewControllerDelegate : NSObjectProtocol
```

## Topics

### Responding to User Events
- [func newPersonViewController(ABNewPersonViewController, didCompleteWithNewPerson: ABRecord?)](abnewpersonviewcontrollerdelegate/newpersonviewcontroller(_:didcompletewithnewperson:).md)
  Sent when the user taps Save or Cancel. If the user tapped Save, the current address book has been saved to the Address Book database.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var newPersonViewDelegate: (any ABNewPersonViewControllerDelegate)?](abnewpersonviewcontroller/newpersonviewdelegate.md)
  The delegate of a new-person view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontrollerdelegate)*