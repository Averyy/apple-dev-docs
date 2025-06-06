# biologicalSex()

**Framework**: Healthkit  
**Kind**: method

Reads someone’s biological sex from the HealthKit store.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func biologicalSex() throws -> HKBiologicalSexObject
```

## Mentions

- [About the HealthKit framework](about-the-healthkit-framework.md)

#### Return Value

An object containing information about someone’s biological sex.

#### Discussion

For a list of possible values, see [`HKBiologicalSex`](hkbiologicalsex.md).

If a person hasn’t set their biological sex or if they’ve denied permission to read the biological sex, this method returns an [`HKBiologicalSex.notSet`](hkbiologicalsex/notset.md) value.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

## Topics

### Possible Values
- [class HKBiologicalSexObject](hkbiologicalsexobject.md)
  This class acts as a wrapper for the [`HKBiologicalSex`](hkbiologicalsex.md) enumeration.
- [enum HKBiologicalSex](hkbiologicalsex.md)
  Constants indicating the user’s sex.

## See Also

- [func bloodType() throws -> HKBloodTypeObject](hkhealthstore/bloodtype.md)
  Reads the user’s blood type from the HealthKit store.
- [func dateOfBirth() throws -> Date](hkhealthstore/dateofbirth.md)
  Reads the user’s date of birth from the HealthKit store as a date value.
- [func dateOfBirthComponents() throws -> DateComponents](hkhealthstore/dateofbirthcomponents.md)
  Reads the user’s date of birth from the HealthKit store as date components.
- [func fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject](hkhealthstore/fitzpatrickskintype.md)
  Reads the user’s Fitzpatrick Skin Type from the HealthKit store.
- [func wheelchairUse() throws -> HKWheelchairUseObject](hkhealthstore/wheelchairuse.md)
  Reads the user’s wheelchair use from the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/biologicalsex())*