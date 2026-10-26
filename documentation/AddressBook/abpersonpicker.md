# ABPersonPicker

**Framework**: Address Book  
**Kind**: class  
**Role**: Class

A picker object that you display when you want the user to select contacts.

**Availability**:
- macOS 10.9+

## Declaration

```objc
@interface ABPersonPicker : NSObject
```

## Topics

### Managing the Picker Interface
- [delegate](./abpersonpicker/delegate.md)
  An object the system notifies as the user interacts with the picker.
- [ABPersonPickerDelegate](./abpersonpickerdelegate.md)
  Methods you use to respond to user selections in a person picker.
### Showing and Closing the Picker
- [- showRelativeToRect:ofView:preferredEdge:](./abpersonpicker/showrelativetorect_ofview_preferrededge_.md)
  Shows the picker in a popover relative to a view.
- [- close](./abpersonpicker/close.md)
  Closes the picker.
### Specifying Picker Properties
- [properties](./abpersonpicker/properties.md)
  An array of properties to display in the picker when the user selects a person.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Pickers
- [class ABPeoplePickerView](./abpeoplepickerview.md)
  An object you use to customize the behavior of people-picker views in an app’s user interface.
- [class ABPersonView](./abpersonview.md)
  An object that provides a view for displaying and editing contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonpicker)*