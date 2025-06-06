# predicateForSelectionOfProperty

**Framework**: Address Book UI  
**Kind**: property

Optionally determines if a selected property should be returned to the app or if the default action for the property should be performed

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@NSCopying
@MainActor var predicateForSelectionOfProperty: NSPredicate? { get set }
```

#### Discussion

If the predicate evaluates to true, the selected property is returned to the app. If the predicate evaluates to false, the default action for the property is performed.

If this property is `nil`, the selected property is returned to the app if the delegate implements [`peoplePickerNavigationController(_:didSelectPerson:property:identifier:)`](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:didselectperson:property:identifier:).md).

## See Also

- [var predicateForEnablingPerson: NSPredicate?](abpeoplepickernavigationcontroller/predicateforenablingperson.md)
  Optionally determines if a person can be selected.
- [var predicateForSelectionOfPerson: NSPredicate?](abpeoplepickernavigationcontroller/predicateforselectionofperson.md)
  Optionally determines if a selected person should be returned to the app or displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/predicateforselectionofproperty)*