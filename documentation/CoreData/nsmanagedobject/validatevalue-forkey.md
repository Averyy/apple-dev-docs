# validateValue(_:forKey:)

**Framework**: Core Data  
**Kind**: method

Validates a property value for a given key.

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
func validateValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws
```

#### Discussion

This method is responsible for two things: coercing the value into an appropriate type for the object, and validating it according to the object’s rules.

The default implementation provided by `NSManagedObject` consults the object’s entity description to coerce the value and to check for basic errors, such as a null value when that isn’t allowed and the length of strings when a field width is specified for the attribute. It then searches for a method of the form `validate<Key>:error:` and invokes it if it exists.

You can implement methods of the form `validate<Key>:error:` to perform validation that is not possible using the constraints available in the property description. If it finds an unacceptable value, your validation method should return [`false`](https://developer.apple.com/documentation/Swift/false) and in `error` an `NSError` object that describes the problem. For more details, see Managed Object Validation. For inter-property validation (to check for combinations of values that are invalid), see [`validateForUpdate()`](nsmanagedobject/validateforupdate().md) and related methods.

## Parameters

- `value`: A pointer to an object.
- `key`: The name of one of the receiver’s properties.

## See Also

- [func validateForDelete() throws](nsmanagedobject/validatefordelete.md)
  Determines whether the managed object can be deleted in its current state.
- [func validateForInsert() throws](nsmanagedobject/validateforinsert.md)
  Determines whether the managed object can be inserted in its current state.
- [func validateForUpdate() throws](nsmanagedobject/validateforupdate.md)
  Determines whether the managed object’s current state is valid.
- [Validation error codes](1535452-validation-error-codes.md)
  Error codes relating to the validation of managed objects.
- [let NSValidationKeyErrorKey: String](nsvalidationkeyerrorkey.md)
  The error key for the attribute that failed to validate.
- [let NSValidationObjectErrorKey: String](nsvalidationobjecterrorkey.md)
  The error key for the object that failed to validate.
- [let NSValidationPredicateErrorKey: String](nsvalidationpredicateerrorkey.md)
  The error key for the predicate that failed to validate.
- [let NSValidationValueErrorKey: String](nsvalidationvalueerrorkey.md)
  The error key for the value that failed to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/validatevalue(_:forkey:))*