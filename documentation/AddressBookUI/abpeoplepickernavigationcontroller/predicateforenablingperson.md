# predicateForEnablingPerson

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Optionally determines if a person can be selected.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactPickerViewController`](../../ContactsUI/cncontactpickerviewcontroller.md) instead.

## Declaration

```swift
@NSCopying
var predicateForEnablingPerson: NSPredicate? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSPredicate * predicateForEnablingPerson;
```

## Discussion

If not set, all persons are selectable.

## See Also

### Customizing Display and Selection
- [var predicateForSelectionOfPerson: NSPredicate?](./predicateforselectionofperson.md)
  Optionally determines if a selected person should be returned to the app or displayed.
- [var predicateForSelectionOfProperty: NSPredicate?](./predicateforselectionofproperty.md)
  Optionally determines if a selected property should be returned to the app or if the default action for the property should be performed


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/predicateforenablingperson)*