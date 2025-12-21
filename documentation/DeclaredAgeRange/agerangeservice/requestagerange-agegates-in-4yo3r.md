# requestAgeRange(ageGates:_:_:in:)

**Framework**: Declared Age Range  
**Kind**: method

Requests an age range for the person logged onto iCloud on the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func requestAgeRange(ageGates threshold1: Int, _ threshold2: Int? = nil, _ threshold3: Int? = nil, in window: NSWindow) async throws -> AgeRangeService.Response
```

#### Return Value

An [`AgeRangeService.Response`](agerangeservice/response.md) value indicating whether the person shared their age range.

#### Discussion

This method presents a system-provided interface that allows people to share their age information with your app. The interface explains what information will be shared and gives people control over whether to provide this information.

The system may return geo-specific age ranges that override your provided age gates based on the person’s location and applicable regulations. When geo-specific ranges are required, the returned age range reflects regulatory requirements rather than the bounds of your age gates.

> **Note**: An [`AgeRangeService.Error`](agerangeservice/error.md) when the request fails.

## Parameters

- `threshold1`: The primary age gate for your app.
- `threshold2`: An optional second age gate for additional content tiers.
- `threshold3`: An optional third age gate for further content differentiation.
- `window`: The window that anchors the system UI presentation. The system UI appears as a sheet   or popover attached to this window.

## See Also

- [AgeRangeService.AgeRangeDeclaration](agerangeservice/agerangedeclaration.md)
  Constants that describe how an adult, parent, or guardian set the age range.
- [AgeRangeService.AgeRange](agerangeservice/agerange.md)
  Information about a person’s age range based on their response to your age range request.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md)
  Requests an age range for the person signed in to iCloud on the device.
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating whether a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](agerangeservice/parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r)*