# predicateForSelectionOfProperty

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Optionally determines if a selected property should be returned to the app or if the default action for the property should be performed

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactPickerViewController`](../../ContactsUI/cncontactpickerviewcontroller.md) instead.

## Declaration

```swift
@NSCopying
var predicateForSelectionOfProperty: NSPredicate? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSPredicate * predicateForSelectionOfProperty;
```

## Discussion

If the predicate evaluates to true, the selected property is returned to the app. If the predicate evaluates to false, the default action for the property is performed.

If this property is `nil`, the selected property is returned to the app if the delegate implements [`peoplePickerNavigationController(_:didSelectPerson:property:identifier:)`](../abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller%28_,didselectperson,property,identifier%29.md).

## See Also

### Customizing Display and Selection
- [var predicateForEnablingPerson: NSPredicate?](./predicateforenablingperson.md)
  Optionally determines if a person can be selected.
- [var predicateForSelectionOfPerson: NSPredicate?](./predicateforselectionofperson.md)
  Optionally determines if a selected person should be returned to the app or displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/predicateforselectionofproperty)*