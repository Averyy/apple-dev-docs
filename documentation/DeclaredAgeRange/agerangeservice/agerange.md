# AgeRangeService.AgeRange

**Framework**: Declared Age Range  
**Kind**: struct  
**Role**: Structure

Information about a person’s age range based on their response to an age range request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
struct AgeRange
```

## Overview

This structure provides the minimum information necessary for you to make content decisions while protecting the person’s privacy. The `requestAgeRange(ageGates:_:_:in:)` methods (for example, [`requestAgeRange(ageGates:_:_:in:)`](./requestagerange%28agegates,_,_,in%29-2go8c.md)) return a response that contains an instance of this structure. Rather than model an exact age, the structure contains a range bounded by the age-gate method parameters.

## Topics

### Fetching the age range
- [var lowerBound: Int?](./agerange/lowerbound.md)
  The minimum age in the person’s declared age range.
- [var upperBound: Int?](./agerange/upperbound.md)
  The maximum age in the person’s declared age range.
- [var ageRangeDeclaration: AgeRangeService.AgeRangeDeclaration?](./agerange/agerangedeclaration.md)
  Information about how the person set their age range.
- [var activeParentalControls: AgeRangeService.ParentalControls](./agerange/activeparentalcontrols.md)
  The parental controls that are active on the device.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the age range
- [AgeRangeService.AgeRangeDeclaration](./agerangedeclaration.md)
  Constants that describe how an adult, parent, or guardian set the age range.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](./requestagerange%28agegates,_,_,in%29-2go8c.md)
  Requests an age range for the person signed in to iCloud on the device.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](./requestagerange%28agegates,_,_,in%29-4yo3r.md)
  Requests an age range for the person logged onto iCloud on the device.
- [AgeRangeService.Response](./response.md)
  A response indicating whether a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](./parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange)*