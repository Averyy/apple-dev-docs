# personPicker:didChoosePerson:property:identifier:

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Informs the delegate when the user selects a person, or a specific property of a person.

**Availability**:
- macOS 10.9+

## Declaration

```objc
- (void) personPicker:(ABPersonPicker *) picker didChoosePerson:(ABPerson *) person property:(NSString *) property identifier:(NSString *) identifier;
```

## Parameters

- `picker`: The picker that presented the popover.
- `person`: The person that the user selected.
- `property`: The property corresponding to the selected value, or `nil` if the user selected a person instead of a specific property.
- `identifier`: The identifier of an item in a multivalue list, such as an address property, or `nil` if the user selected a person or a value that isn’t a multivalue.

## See Also

### Handling Selections
- [- personPickerDidClose:](./personpickerdidclose_.md)
  Notifies the delegate when the user closes the  picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonpickerdelegate/personpicker:didchooseperson:property:identifier:)*