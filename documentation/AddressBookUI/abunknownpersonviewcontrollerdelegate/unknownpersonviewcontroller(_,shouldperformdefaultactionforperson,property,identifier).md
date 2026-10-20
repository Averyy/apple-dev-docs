# unknownPersonViewController(_:shouldPerformDefaultActionForPerson:property:identifier:)

**Framework**: Address Book UI  
**Kind**: method  
**Role**: Instance Method

Sent when the user selects a property value of the person displayed in a person view controller.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func unknownPersonViewController(_ personViewController: ABUnknownPersonViewController, shouldPerformDefaultActionForPerson person: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool
```

```objc
- (BOOL) unknownPersonViewController:(ABUnknownPersonViewController *) personViewController shouldPerformDefaultActionForPerson:(ABRecordRef) person property:(ABPropertyID) property identifier:(ABMultiValueIdentifier) identifier;
```

#### Return Value

[`true`](../../Swift/true.md) if `unknownPersonViewController` should perform its default action. Your application may quit as a result of this action. [`false`](../../Swift/false.md): if `unknownPersonViewController` should do nothing. The delegate may perform custom action processing.

## Parameters

- `person`: The person `unknownPersonViewController` is displaying.
- `property`: The property whose value the user selected.
- `identifier`: The identifier for the value the user selected if `property` is a multivalue property; otherwise, `kABMultiValueInvalidIdentifier`.

## See Also

### Responding to User Events
- [func unknownPersonViewController(ABUnknownPersonViewController, didResolveToPerson: ABRecord?)](./unknownpersonviewcontroller%28_,didresolvetoperson%29.md)
  Sent when the user finishes creating a contact or adding the displayed person properties to an existing contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontrollerdelegate/unknownpersonviewcontroller(_:shouldperformdefaultactionforperson:property:identifier:))*