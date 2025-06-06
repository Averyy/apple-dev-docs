# unknownPersonViewController(_:didResolveToPerson:)

**Framework**: Address Book UI  
**Kind**: method  
**Required**: Yes

Sent when the user finishes creating a contact or adding the displayed person properties to an existing contact.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func unknownPersonViewController(_ unknownCardViewController: ABUnknownPersonViewController, didResolveToPerson person: ABRecord?)
```

## Parameters

- `person`:  when the user cancelled the interaction.

## See Also

- [func unknownPersonViewController(ABUnknownPersonViewController, shouldPerformDefaultActionForPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](abunknownpersonviewcontrollerdelegate/unknownpersonviewcontroller(_:shouldperformdefaultactionforperson:property:identifier:).md)
  Sent when the user selects a property value of the person displayed in a person view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontrollerdelegate/unknownpersonviewcontroller(_:didresolvetoperson:))*