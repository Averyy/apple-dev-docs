# requestAgeRange(ageGates:_:_:in:)

**Framework**: Declared Age Range  
**Kind**: method

Requests an age range for the person signed in to iCloud on the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func requestAgeRange(ageGates threshold1: Int, _ threshold2: Int? = nil, _ threshold3: Int? = nil, in viewController: UIViewController) async throws -> AgeRangeService.Response
```

#### Return Value

An [`AgeRangeService.Response`](agerangeservice/response.md) value containing either the person’s age range or an indication that the person declined to share their age range.

#### Discussion

Use [`requestAgeRange(ageGates:_:_:in:)`](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md) to implement age-range based restrictions to your app’s content. People who meet the minimum age requirements that you specify can access age appropriate features and content.

This method presents a system-provided interface that explains what information a person shares with your app and allows people to make an informed decision about providing their age range information to your app.

The system may return age ranges that override the age gates you specify based on the person’s location and applicable regulations. When geo-specific ranges are required, the returned age range reflects regulatory requirements rather than the bounds of your age gates.

> **Note**: An [`AgeRangeService.Error`](agerangeservice/error.md) when the request fails.

## Parameters

- `threshold1`: The primary minimum age requirement for your app.
- `threshold2`: An optional second age threshold for additional content tiers.
- `threshold3`: An optional third age threshold for further content differentiation.
- `viewController`: The view controller that anchors the system UI presentation. The system UI   appears modally over this view controller.

## See Also

- [AgeRangeService.AgeRangeDeclaration](agerangeservice/agerangedeclaration.md)
  Constants that describe how an adult, parent, or guardian set the age range.
- [AgeRangeService.AgeRange](agerangeservice/agerange.md)
  Information about a person’s age range based on their response to your age range request.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r.md)
  Requests an age range for the person logged onto iCloud on the device.
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating whether a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](agerangeservice/parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/requestagerange(agegates:_:_:in:)-2go8c)*