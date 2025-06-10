# AgeRangeService.AgeRangeDeclaration

**Framework**: DeclaredAgeRange  
**Kind**: enum

An enumeration that describes the declared age range.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
enum AgeRangeDeclaration
```

#### Overview

The system specifies whether the person declared the age range or an adult made the determination.

## Topics

### Determining the age range
- [AgeRangeService.AgeRangeDeclaration.selfDeclared](agerangeservice/agerangedeclaration/selfdeclared.md)
  The age range was declared by the person.
- [AgeRangeService.AgeRangeDeclaration.guardianDeclared](agerangeservice/agerangedeclaration/guardiandeclared.md)
  The age range was declared by a parent or guardian.
### Operators
- [static func == (AgeRangeService.AgeRangeDeclaration, AgeRangeService.AgeRangeDeclaration) -> Bool](agerangeservice/agerangedeclaration/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](agerangeservice/agerangedeclaration/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](agerangeservice/agerangedeclaration/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](agerangeservice/agerangedeclaration/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [AgeRangeService.AgeRange](agerangeservice/agerange.md)
  A person’s age range is based on the information they provided in response to the age range request.
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating either a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](agerangeservice/parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration)*