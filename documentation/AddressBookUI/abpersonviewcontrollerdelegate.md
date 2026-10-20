# ABPersonViewControllerDelegate

**Framework**: Address Book UI  
**Kind**: protocol  
**Role**: Protocol

The `ABPersonViewControllerDelegate` protocol declares the interface that must be implemented by [`ABPersonViewController`](./abpersonviewcontroller.md) delegates.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 14.0+

> **Deprecated**: Use [`CNContactViewController`](../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
protocol ABPersonViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol ABPersonViewControllerDelegate <NSObject>
```

## Topics

### Responding to User Events
- [func personViewController(ABPersonViewController, shouldPerformDefaultActionForPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](./abpersonviewcontrollerdelegate/personviewcontroller%28_,shouldperformdefaultactionforperson,property,identifier%29.md)
  Sent when the user selects a property value of the person displayed in a person view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to View Controller Interactions
- [var personViewDelegate: (any ABPersonViewControllerDelegate)?](./abpersonviewcontroller/personviewdelegate.md)
  The person-view controller delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontrollerdelegate)*