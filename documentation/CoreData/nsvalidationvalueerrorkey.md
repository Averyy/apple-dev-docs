# NSValidationValueErrorKey

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

The error key for the value that failed to validate.

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
let NSValidationValueErrorKey: String
```

```c
extern NSString * const NSValidationValueErrorKey;
```

## See Also

### Managing Data Validation
- [func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String) throws](./nsmanagedobject/validatevalue%28_,forkey%29.md)
  Validates a property value for a given key.
- [func validateForDelete() throws](./nsmanagedobject/validatefordelete%28%29.md)
  Determines whether the managed object can be deleted in its current state.
- [func validateForInsert() throws](./nsmanagedobject/validateforinsert%28%29.md)
  Determines whether the managed object can be inserted in its current state.
- [func validateForUpdate() throws](./nsmanagedobject/validateforupdate%28%29.md)
  Determines whether the managed object’s current state is valid.
- [Validation error codes](./api-1535452-validation-error-codes.md)
  Error codes relating to the validation of managed objects.
- [let NSValidationKeyErrorKey: String](./nsvalidationkeyerrorkey.md)
  The error key for the attribute that failed to validate.
- [let NSValidationObjectErrorKey: String](./nsvalidationobjecterrorkey.md)
  The error key for the object that failed to validate.
- [let NSValidationPredicateErrorKey: String](./nsvalidationpredicateerrorkey.md)
  The error key for the predicate that failed to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsvalidationvalueerrorkey)*