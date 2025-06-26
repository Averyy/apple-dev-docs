# AgeRangeService.Response

**Framework**: Declared Age Range  
**Kind**: enum

A response indicating either a person shared their age range or declined to share it.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
enum Response
```

## Topics

### Getting the age range response
- [AgeRangeService.Response.declinedSharing](agerangeservice/response/declinedsharing.md)
  The person declined to share their age range.
- [case sharing(range: AgeRangeService.AgeRange)](agerangeservice/response/sharing(range:).md)
  The person shared the age range successfully.

## See Also

- [AgeRangeService.AgeRangeDeclaration](agerangeservice/agerangedeclaration.md)
  An enumeration that describes the declared age range.
- [AgeRangeService.AgeRange](agerangeservice/agerange.md)
  A person’s age range is based on the age they provided in response to the age range request.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md)
  Determines an age range for the person logged onto iCloud on the device.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r.md)
  Determines an age range for the person logged onto iCloud on the device.
- [AgeRangeService.ParentalControls](agerangeservice/parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/response)*