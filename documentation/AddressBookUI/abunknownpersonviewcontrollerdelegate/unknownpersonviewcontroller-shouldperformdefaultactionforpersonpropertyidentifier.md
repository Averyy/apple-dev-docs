# unknownPersonViewController(_:shouldPerformDefaultActionForPerson:property:identifier:)

**Framework**: Address Book UI  
**Kind**: method

Sent when the user selects a property value of the person displayed in a person view controller.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func unknownPersonViewController(_ personViewController: ABUnknownPersonViewController, shouldPerformDefaultActionForPerson person: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `unknownPersonViewController` should perform its default action. Your application may quit as a result of this action. [`false`](https://developer.apple.com/documentation/swift/false): if `unknownPersonViewController` should do nothing. The delegate may perform custom action processing.

## Parameters

- `person`: The person   is displaying.
- `property`: The property whose value the user selected.
- `identifier`: The identifier for the value the user selected if   is a multivalue property; otherwise,  .

## See Also

- [func unknownPersonViewController(ABUnknownPersonViewController, didResolveToPerson: ABRecord?)](abunknownpersonviewcontrollerdelegate/unknownpersonviewcontroller(_:didresolvetoperson:).md)
  Sent when the user finishes creating a contact or adding the displayed person properties to an existing contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontrollerdelegate/unknownpersonviewcontroller(_:shouldperformdefaultactionforperson:property:identifier:))*