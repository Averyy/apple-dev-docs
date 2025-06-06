# fitzpatrickSkinType()

**Framework**: Healthkit  
**Kind**: method

Reads the user’s Fitzpatrick Skin Type from the HealthKit store.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject
```

## Mentions

- [About the HealthKit framework](about-the-healthkit-framework.md)

#### Return Value

A skin type object representing the skin type selected by the user.

#### Discussion

If the user has not yet specified a skin type, or if the user has denied your app permission to read the skin type, this method returns [`HKFitzpatrickSkinType.notSet`](hkfitzpatrickskintype/notset.md).

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Topics

### Possible Values
- [class HKFitzpatrickSkinTypeObject](hkfitzpatrickskintypeobject.md)
  This class acts as a wrapper for the [`HKFitzpatrickSkinType`](hkfitzpatrickskintype.md) enumeration.
- [enum HKFitzpatrickSkinType](hkfitzpatrickskintype.md)
  Categories representing the user’s skin type based on the Fitzpatrick scale.

## See Also

- [func biologicalSex() throws -> HKBiologicalSexObject](hkhealthstore/biologicalsex.md)
  Reads someone’s biological sex from the HealthKit store.
- [func bloodType() throws -> HKBloodTypeObject](hkhealthstore/bloodtype.md)
  Reads the user’s blood type from the HealthKit store.
- [func dateOfBirth() throws -> Date](hkhealthstore/dateofbirth.md)
  Reads the user’s date of birth from the HealthKit store as a date value.
- [func dateOfBirthComponents() throws -> DateComponents](hkhealthstore/dateofbirthcomponents.md)
  Reads the user’s date of birth from the HealthKit store as date components.
- [func wheelchairUse() throws -> HKWheelchairUseObject](hkhealthstore/wheelchairuse.md)
  Reads the user’s wheelchair use from the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/fitzpatrickskintype())*