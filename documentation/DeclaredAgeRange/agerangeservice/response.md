# AgeRangeService.Response

**Framework**: Declared Age Range  
**Kind**: enum  
**Role**: Enumeration

A response indicating whether a person shared their age range or declined to share it.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum Response
```

## Topics

### Getting the age range response
- [AgeRangeService.Response.declinedSharing](./response/declinedsharing.md)
  Indicates the person declined to share their age range with your app.
- [case sharing(range: AgeRangeService.AgeRange)](./response/sharing%28range%29.md)
  Contains the person’s shared age range information.

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
- [AgeRangeService.ParentalControls](./parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/response)*