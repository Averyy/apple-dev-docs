# AgeRangeService.ParentalControls

**Framework**: Declared Age Range  
**Kind**: struct

An option set to define parental controls enabled and shared as a part of age range declaration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
struct ParentalControls
```

## Topics

### Creating a value
- [init(rawValue: Int)](agerangeservice/parentalcontrols/init(rawvalue:).md)
  Creates a parental controls option set with the specified raw value.
### Accessing the raw value
- [var description: String](agerangeservice/parentalcontrols/description.md)
  A list of parental controls that are turned on, for debugging purposes.
- [let rawValue: Int](agerangeservice/parentalcontrols/rawvalue.md)
  The raw value of the option set.
### Defining parental control options
- [static let communicationLimits: AgeRangeService.ParentalControls](agerangeservice/parentalcontrols/communicationlimits.md)
  Indicates that the system limits communication features for the minor.
- [static let significantAppChangeApprovalRequired: AgeRangeService.ParentalControls](agerangeservice/parentalcontrols/significantappchangeapprovalrequired.md)
  Indicates a notification obligation for significant app updates.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [AgeRangeService.AgeRangeDeclaration](agerangeservice/agerangedeclaration.md)
  Constants that describe how an adult, parent, or guardian set the age range.
- [AgeRangeService.AgeRange](agerangeservice/agerange.md)
  Information about a person’s age range based on their response to your age range request.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md)
  Requests an age range for the person signed in to iCloud on the device.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r.md)
  Requests an age range for the person logged onto iCloud on the device.
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating whether a person shared their age range or declined to share it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/parentalcontrols)*