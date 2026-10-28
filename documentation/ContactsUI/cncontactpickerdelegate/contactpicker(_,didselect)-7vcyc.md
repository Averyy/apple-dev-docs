# contactPicker(_:didSelect:)

**Framework**: Contacts UI  
**Kind**: method  
**Role**: Instance Method

Called after a contact has been selected by the user.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
optional func contactPicker(_ picker: CNContactPickerViewController, didSelect contact: CNContact)
```

*macOS*

```swift
optional func contactPicker(_ picker: CNContactPicker, didSelect contact: CNContact)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (void) contactPicker:(CNContactPickerViewController *) picker didSelectContact:(CNContact *) contact;
```

*macOS*

```objc
- (void) contactPicker:(CNContactPicker *) picker didSelectContact:(CNContact *) contact;
```

## Discussion

This delegate method is called when the user selects a single contact.

## Parameters

- `picker`: The contact picker where the selection was made.
- `contact`: The selected contact.

## See Also

### Responding to User Selections
- [func contactPicker(CNContactPickerViewController, didSelect: CNContactProperty)](./contactpicker%28_,didselect%29-1xfpt.md)
  Called when a property of the contact has been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelect: [CNContact])](./contactpicker%28_,didselect%29-5neeo.md)
  Called after contacts have been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelectContactProperties: [CNContactProperty])](./contactpicker%28_,didselectcontactproperties%29.md)
  Called after contact properties have been selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/contactpicker(_:didselect:)-7vcyc)*