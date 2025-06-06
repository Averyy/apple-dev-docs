# ABPersonViewControllerDelegate

**Framework**: Address Book UI  
**Kind**: protocol

The `ABPersonViewControllerDelegate` protocol declares the interface that must be implemented by [`ABPersonViewController`](abpersonviewcontroller.md) delegates.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 14.0+

## Declaration

```swift
protocol ABPersonViewControllerDelegate : NSObjectProtocol
```

## Topics

### Responding to User Events
- [func personViewController(ABPersonViewController, shouldPerformDefaultActionForPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](abpersonviewcontrollerdelegate/personviewcontroller(_:shouldperformdefaultactionforperson:property:identifier:).md)
  Sent when the user selects a property value of the person displayed in a person view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var personViewDelegate: (any ABPersonViewControllerDelegate)?](abpersonviewcontroller/personviewdelegate.md)
  The person-view controller delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontrollerdelegate)*