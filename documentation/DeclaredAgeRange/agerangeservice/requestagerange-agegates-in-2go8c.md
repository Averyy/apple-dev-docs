# requestAgeRange(ageGates:_:_:in:)

**Framework**: Declared Age Range  
**Kind**: method

Determines an age range for the person logged onto iCloud on the device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
func requestAgeRange(ageGates threshold1: Int, _ threshold2: Int? = nil, _ threshold3: Int? = nil, in viewController: UIViewController) async throws -> AgeRangeService.Response
```

#### Return Value

An [`AgeRangeService.Response`](agerangeservice/response.md) or throws [`AgeRangeService.Error`](agerangeservice/error.md).

#### Discussion

Use [`requestAgeRange(ageGates:_:_:in:)`](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md) for age-gated access to your apps content. People that meet the minimum age requirement you set can access age appropriate content.

## Parameters

- `threshold1`: The required minimum age for your app.
- `threshold2`: An optional additional minimum age for your app.
- `threshold3`: An optional additional minimum age for your app.
- `viewController`: The view controller to anchor and present system UI off of.

## See Also

- [AgeRangeService.AgeRangeDeclaration](agerangeservice/agerangedeclaration.md)
  An enumeration that describes the declared age range.
- [AgeRangeService.AgeRange](agerangeservice/agerange.md)
  A person’s age range is based on the age they provided in response to the age range request.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r.md)
  Determines an age range for the person logged onto iCloud on the device.
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating either a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](agerangeservice/parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/requestagerange(agegates:_:_:in:)-2go8c)*