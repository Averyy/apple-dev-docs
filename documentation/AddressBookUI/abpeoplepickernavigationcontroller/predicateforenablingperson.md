# predicateForEnablingPerson

**Framework**: Address Book UI  
**Kind**: property

Optionally determines if a person can be selected.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@NSCopying
@MainActor var predicateForEnablingPerson: NSPredicate? { get set }
```

#### Discussion

If not set, all persons are selectable.

## See Also

- [var predicateForSelectionOfPerson: NSPredicate?](abpeoplepickernavigationcontroller/predicateforselectionofperson.md)
  Optionally determines if a selected person should be returned to the app or displayed.
- [var predicateForSelectionOfProperty: NSPredicate?](abpeoplepickernavigationcontroller/predicateforselectionofproperty.md)
  Optionally determines if a selected property should be returned to the app or if the default action for the property should be performed


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/predicateforenablingperson)*