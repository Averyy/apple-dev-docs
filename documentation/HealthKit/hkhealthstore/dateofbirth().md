# dateOfBirth()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Reads the user’s date of birth from the HealthKit store as a date value.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Use [`dateOfBirthComponents()`](./dateofbirthcomponents%28%29.md) instead.

## Declaration

```swift
func dateOfBirth() throws -> Date
```

```objc
- (NSDate *) dateOfBirthWithError:(NSError **) error;
```

## Mentions

- [About the HealthKit framework](../about-the-healthkit-framework.md)

## Return Value

An [`NSDate`](../../Foundation/nsdate.md) object representing the user’s birthdate, or `nil`.

## Discussion

If the user has not yet specified a birth date, or if the user has denied your app permission to read the birth date, this method returns `nil`.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Reading characteristic data
- [func biologicalSex() throws -> HKBiologicalSexObject](./biologicalsex%28%29.md)
  Reads someone’s biological sex from the HealthKit store.
- [func bloodType() throws -> HKBloodTypeObject](./bloodtype%28%29.md)
  Reads the user’s blood type from the HealthKit store.
- [func dateOfBirthComponents() throws -> DateComponents](./dateofbirthcomponents%28%29.md)
  Reads the user’s date of birth from the HealthKit store as date components.
- [func fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject](./fitzpatrickskintype%28%29.md)
  Reads the user’s Fitzpatrick Skin Type from the HealthKit store.
- [func wheelchairUse() throws -> HKWheelchairUseObject](./wheelchairuse%28%29.md)
  Reads the user’s wheelchair use from the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/dateofbirth())*