# predicateForSelectionOfPerson

**Framework**: Address Book UI  
**Kind**: property

Optionally determines if a selected person should be returned to the app or displayed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@NSCopying
@MainActor var predicateForSelectionOfPerson: NSPredicate? { get set }
```

#### Discussion

If the predicate evaluates to true for the selected person, the selected person is returned to the app. If the predicate evaluates to false, the selected person is displayed.

If this property is `nil`, the person is returned to the app if the delegate implements [`peoplePickerNavigationController(_:didSelectPerson:)`](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:didselectperson:).md), and the person is displayed if the delegate implements [`peoplePickerNavigationController(_:didSelectPerson:property:identifier:)`](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:didselectperson:property:identifier:).md).

## See Also

- [var predicateForEnablingPerson: NSPredicate?](abpeoplepickernavigationcontroller/predicateforenablingperson.md)
  Optionally determines if a person can be selected.
- [var predicateForSelectionOfProperty: NSPredicate?](abpeoplepickernavigationcontroller/predicateforselectionofproperty.md)
  Optionally determines if a selected property should be returned to the app or if the default action for the property should be performed


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/predicateforselectionofperson)*