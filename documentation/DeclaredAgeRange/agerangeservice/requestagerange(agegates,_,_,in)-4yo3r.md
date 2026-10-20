# requestAgeRange(ageGates:_:_:in:)

**Framework**: Declared Age Range  
**Kind**: method  
**Role**: Instance Method

Requests an age range for the person logged onto iCloud on the device.

**Availability**:
- macOS 26.0+

## Declaration

```swift
func requestAgeRange(ageGates threshold1: Int, _ threshold2: Int? = nil, _ threshold3: Int? = nil, in window: NSWindow) async throws -> AgeRangeService.Response
```

#### Return Value

An [`AgeRangeService.Response`](./response.md) value indicating whether the person shared their age range.

#### Discussion

This method presents a system-provided interface that allows people to share their age information with your app. The interface explains what information will be shared and gives people control over whether to provide this information.

The system may return age ranges that override the age gates you specify based on the person’s location and applicable regulations. When local regulations require specific age gates, the returned age range reflects regulatory requirements rather than the bounds of your age gates.

> **Throws**: An [`AgeRangeService.Error`](./error.md) when the request fails.

## Parameters

- `threshold1`: The primary age threshold for your app.
- `threshold2`: An optional second age threshold that creates an additional age range.
- `threshold3`: An optional third age threshold that creates a final age range.
- `window`: The window that anchors the system UI presentation. The system UI appears as an interface or popover attached to this window.

## See Also

### Getting the age range
- [AgeRangeService.AgeRangeDeclaration](./agerangedeclaration.md)
  Constants that describe how an adult, parent, or guardian set the age range.
- [AgeRangeService.AgeRange](./agerange.md)
  Information about a person’s age range based on their response to an age range request.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](./requestagerange%28agegates,_,_,in%29-2go8c.md)
  Requests an age range for the person signed in to iCloud on the device.
- [AgeRangeService.Response](./response.md)
  A response indicating whether a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](./parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r)*