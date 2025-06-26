# AgeRangeService.AgeRangeDeclaration

**Framework**: Declared Age Range  
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

The system specifies whether the age was self declared or declared by a Family Organizer in an Family Sharing group.

## Topics

### Determining the age range
- [AgeRangeService.AgeRangeDeclaration.selfDeclared](agerangeservice/agerangedeclaration/selfdeclared.md)
  The age was declared by the person signed in to iCloud.
- [AgeRangeService.AgeRangeDeclaration.guardianDeclared](agerangeservice/agerangedeclaration/guardiandeclared.md)
  The age of the person was declared by a Family Organizer in a Family Sharing group.
### Comparing values
- [static func == (AgeRangeService.AgeRangeDeclaration, AgeRangeService.AgeRangeDeclaration) -> Bool](agerangeservice/agerangedeclaration/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [var hashValue: Int](agerangeservice/agerangedeclaration/hashvalue.md)
  The hash value.
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
  A person’s age range is based on the age they provided in response to the age range request.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md)
  Determines an age range for the person logged onto iCloud on the device.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r.md)
  Determines an age range for the person logged onto iCloud on the device.
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating either a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](agerangeservice/parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration)*