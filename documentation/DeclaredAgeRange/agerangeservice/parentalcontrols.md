# AgeRangeService.ParentalControls

**Framework**: Declared Age Range  
**Kind**: struct  
**Role**: Structure

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
- [init(rawValue: Int)](./parentalcontrols/init%28rawvalue%29.md)
  Creates a parental controls option set with the specified raw value.
### Accessing the raw value
- [var description: String](./parentalcontrols/description.md)
  A list of active parental controls, for debugging purposes.
- [let rawValue: Int](./parentalcontrols/rawvalue.md)
  The raw value of the option set.
### Defining parental control options
- [static let communicationLimits: AgeRangeService.ParentalControls](./parentalcontrols/communicationlimits.md)
  Indicates that the system limits communication features for the minor.
### Deprecated
- [static let significantAppChangeApprovalRequired: AgeRangeService.ParentalControls](./parentalcontrols/significantappchangeapprovalrequired.md)
  Indicates a notification obligation for significant app updates.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting the age range
- [AgeRangeService.AgeRangeDeclaration](./agerangedeclaration.md)
  Constants that describe how an adult, parent, or guardian set the age range.
- [AgeRangeService.AgeRange](./agerange.md)
  Information about a person’s age range based on their response to an age range request.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](./requestagerange%28agegates,_,_,in%29-2go8c.md)
  Requests an age range for the person signed in to iCloud on the device.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](./requestagerange%28agegates,_,_,in%29-4yo3r.md)
  Requests an age range for the person logged onto iCloud on the device.
- [AgeRangeService.Response](./response.md)
  A response indicating whether a person shared their age range or declined to share it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/parentalcontrols)*