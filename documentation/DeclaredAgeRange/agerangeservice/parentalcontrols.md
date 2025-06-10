# AgeRangeService.ParentalControls

**Framework**: DeclaredAgeRange  
**Kind**: struct

An option set to define parental controls enabled and shared as a part of age range declaration.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
struct ParentalControls
```

## Topics

### Creating a value
- [init(rawValue: Int)](agerangeservice/parentalcontrols/init(rawvalue:).md)
  Creates an option set with the specified raw value.
### Accessing the raw value
- [var description: String](agerangeservice/parentalcontrols/description.md)
  The raw value of the option set.
- [let rawValue: Int](agerangeservice/parentalcontrols/rawvalue-swift.property.md)
  The raw value of the option set.
### Accessing communication limits
- [static let communicationLimits: AgeRangeService.ParentalControls](agerangeservice/parentalcontrols/communicationlimits.md)
  The system limits communication with the person.
### Type Aliases
- [AgeRangeService.ParentalControls.ArrayLiteralElement](agerangeservice/parentalcontrols/arrayliteralelement.md)
  The type of the elements of an array literal.
- [AgeRangeService.ParentalControls.Element](agerangeservice/parentalcontrols/element.md)
  The element type of the option set.
- [AgeRangeService.ParentalControls.RawValue](agerangeservice/parentalcontrols/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](agerangeservice/parentalcontrols/equatable-implementations.md)
- [OptionSet Implementations](agerangeservice/parentalcontrols/optionset-implementations.md)
- [SetAlgebra Implementations](agerangeservice/parentalcontrols/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [AgeRangeService.AgeRangeDeclaration](agerangeservice/agerangedeclaration.md)
  An enumeration that describes the declared age range.
- [AgeRangeService.AgeRange](agerangeservice/agerange.md)
  A person’s age range is based on the information they provided in response to the age range request.
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating either a person shared their age range or declined to share it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/parentalcontrols)*