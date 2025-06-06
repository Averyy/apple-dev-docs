# setValidationPredicates(_:withValidationWarnings:)

**Framework**: Core Data  
**Kind**: method

Sets the validation predicates and warnings of the receiver.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setValidationPredicates(_ validationPredicates: [NSPredicate]?, withValidationWarnings validationWarnings: [String]?)
```

#### Discussion

The `validationPredicates` and `validationWarnings` arrays should contain the same number of elements, and corresponding elements should appear at the same index in each array.

Instead of implementing individual validation methods, you can use this method to provide a list of predicates that are evaluated against the managed objects and a list of corresponding error messages (which can be localized).

##### Special Considerations

This method raises an exception if the receiver’s model has been used by an object graph manager.

## Parameters

- `validationPredicates`: An array containing the validation predicates for the receiver.
- `validationWarnings`: An array containing the validation warnings for the receiver.

## See Also

- [var validationPredicates: [NSPredicate]](nspropertydescription/validationpredicates.md)
  The validation predicates of the receiver.
- [var validationWarnings: [Any]](nspropertydescription/validationwarnings.md)
  The error strings associated with the receiver’s validation predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/setvalidationpredicates(_:withvalidationwarnings:))*