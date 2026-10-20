# contactPicker(_:didSelect:)

**Framework**: Contacts UI  
**Kind**: method  
**Role**: Instance Method

Called when a property of the contact has been selected by the user.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
optional func contactPicker(_ picker: CNContactPickerViewController, didSelect contactProperty: CNContactProperty)
```

*macOS*

```swift
optional func contactPicker(_ picker: CNContactPicker, didSelect contactProperty: CNContactProperty)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (void) contactPicker:(CNContactPickerViewController *) picker didSelectContactProperty:(CNContactProperty *) contactProperty;
```

*macOS*

```objc
- (void) contactPicker:(CNContactPicker *) picker didSelectContactProperty:(CNContactProperty *) contactProperty;
```

#### Discussion

This delegate method ia called when the user selects a single property of the contact.

## Parameters

- `picker`: The contact picker where the selection was made.
- `contactProperty`: The selected contact property.

## See Also

### Responding to User Selections
- [func contactPicker(CNContactPickerViewController, didSelect: CNContact)](./contactpicker%28_,didselect%29-7vcyc.md)
  Called after a contact has been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelect: [CNContact])](./contactpicker%28_,didselect%29-5neeo.md)
  Called after contacts have been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelectContactProperties: [CNContactProperty])](./contactpicker%28_,didselectcontactproperties%29.md)
  Called after contact properties have been selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/contactpicker(_:didselect:)-1xfpt)*