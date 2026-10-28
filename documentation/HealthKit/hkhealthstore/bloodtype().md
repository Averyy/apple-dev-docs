# bloodType()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Reads the user’s blood type from the HealthKit store.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func bloodType() throws -> HKBloodTypeObject
```

```objc
- (HKBloodTypeObject *) bloodTypeWithError:(NSError **) error;
```

## Mentions

- [About the HealthKit framework](../about-the-healthkit-framework.md)

## Return Value

A blood type object that contains information about the user’s blood type.

## Discussion

If the user has not specified a blood type or if the user has denied your app permission to read the blood type, this method returns an [`HKBloodType.notSet`](../hkbloodtype/notset.md) value.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Topics

### Possible Values
- [class HKBloodTypeObject](../hkbloodtypeobject.md)
  This class acts as a wrapper for the [`HKBloodType`](../hkbloodtype.md) enumeration.
- [enum HKBloodType](../hkbloodtype.md)
  Constants indicating the user’s blood type.

## See Also

### Reading characteristic data
- [func biologicalSex() throws -> HKBiologicalSexObject](./biologicalsex%28%29.md)
  Reads someone’s biological sex from the HealthKit store.
- [func dateOfBirth() throws -> Date](./dateofbirth%28%29.md)
  Reads the user’s date of birth from the HealthKit store as a date value.
- [func dateOfBirthComponents() throws -> DateComponents](./dateofbirthcomponents%28%29.md)
  Reads the user’s date of birth from the HealthKit store as date components.
- [func fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject](./fitzpatrickskintype%28%29.md)
  Reads the user’s Fitzpatrick Skin Type from the HealthKit store.
- [func wheelchairUse() throws -> HKWheelchairUseObject](./wheelchairuse%28%29.md)
  Reads the user’s wheelchair use from the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/bloodtype())*