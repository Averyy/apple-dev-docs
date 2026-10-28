# predicateForSelectionOfPerson

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Optionally determines if a selected person should be returned to the app or displayed.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactPickerViewController`](../../ContactsUI/cncontactpickerviewcontroller.md) instead.

## Declaration

```swift
@NSCopying
var predicateForSelectionOfPerson: NSPredicate? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSPredicate * predicateForSelectionOfPerson;
```

## Discussion

If the predicate evaluates to true for the selected person, the selected person is returned to the app. If the predicate evaluates to false, the selected person is displayed.

If this property is `nil`, the person is returned to the app if the delegate implements [`peoplePickerNavigationController(_:didSelectPerson:)`](../abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller%28_,didselectperson%29.md), and the person is displayed if the delegate implements [`peoplePickerNavigationController(_:didSelectPerson:property:identifier:)`](../abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller%28_,didselectperson,property,identifier%29.md).

## See Also

### Customizing Display and Selection
- [var predicateForEnablingPerson: NSPredicate?](./predicateforenablingperson.md)
  Optionally determines if a person can be selected.
- [var predicateForSelectionOfProperty: NSPredicate?](./predicateforselectionofproperty.md)
  Optionally determines if a selected property should be returned to the app or if the default action for the property should be performed


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/predicateforselectionofperson)*