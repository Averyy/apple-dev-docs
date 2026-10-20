# unknownPersonViewController(_:didResolveToPerson:)

**Framework**: Address Book UI  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) unknownPersonViewController:(ABUnknownPersonViewController *) unknownCardViewController didResolveToPerson:(ABRecordRef) person;
```

## Parameters

- `person`: The contact the user created or to which they added information. This record is saved in the Address Book database.

  `NULL` when the user cancelled the interaction.

## See Also

### Responding to User Events
- [func unknownPersonViewController(ABUnknownPersonViewController, shouldPerformDefaultActionForPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](./unknownpersonviewcontroller%28_,shouldperformdefaultactionforperson,property,identifier%29.md)
  Sent when the user selects a property value of the person displayed in a person view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontrollerdelegate/unknownpersonviewcontroller(_:didresolvetoperson:))*