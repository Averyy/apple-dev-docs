# requestAgeRange(ageGates:_:_:in:)

**Framework**: DeclaredAgeRange  
**Kind**: method

Determines an age range for the person logged onto the device.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/requestagerange(agegates:_:_:in:)-2go8c)*