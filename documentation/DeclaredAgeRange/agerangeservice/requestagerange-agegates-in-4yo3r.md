# requestAgeRange(ageGates:_:_:in:)

**Framework**: DeclaredAgeRange  
**Kind**: method

Determines an age range for the person using the device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
func requestAgeRange(ageGates threshold1: Int, _ threshold2: Int? = nil, _ threshold3: Int? = nil, in window: NSWindow) async throws -> AgeRangeService.Response
```

#### Return Value

An [`AgeRangeService.Response`](agerangeservice/response.md) or throws an [`AgeRangeService.Error`](agerangeservice/error.md).

## Parameters

- `threshold1`: The required age gate for your app.
- `threshold2`: An optional additional age gate for your app.
- `threshold3`: An optional additional age gate for your app.
- `window`: The window to anchor and present system UI off of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r)*