# validateForUpdate()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Determines whether the managed object’s current state is valid.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func validateForUpdate() throws
```

```objc
- (BOOL) validateForUpdate:(NSError **) error;
```

#### Discussion

`NSManagedObject`‘s implementation iterates through all of the receiver’s properties validating each in turn. If this results in more than one error, the `userInfo` dictionary in the `NSError` returned in `error` contains a key `NSDetailedErrorsKey`; the corresponding value is an array containing the individual validation errors. If you pass `NULL` as the error, validation will abort after the first failure.

> ❗ **Important**:  Subclasses should invoke super’s implementation before performing their own validation, and should combine any error returned by super’s implementation with their own (see Managed Object Validation).

## See Also

### Managing Data Validation
- [func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String) throws](./validatevalue%28_,forkey%29.md)
  Validates a property value for a given key.
- [func validateForDelete() throws](./validatefordelete%28%29.md)
  Determines whether the managed object can be deleted in its current state.
- [func validateForInsert() throws](./validateforinsert%28%29.md)
  Determines whether the managed object can be inserted in its current state.
- [Validation error codes](../api-1535452-validation-error-codes.md)
  Error codes relating to the validation of managed objects.
- [let NSValidationKeyErrorKey: String](../nsvalidationkeyerrorkey.md)
  The error key for the attribute that failed to validate.
- [let NSValidationObjectErrorKey: String](../nsvalidationobjecterrorkey.md)
  The error key for the object that failed to validate.
- [let NSValidationPredicateErrorKey: String](../nsvalidationpredicateerrorkey.md)
  The error key for the predicate that failed to validate.
- [let NSValidationValueErrorKey: String](../nsvalidationvalueerrorkey.md)
  The error key for the value that failed to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/validateforupdate())*