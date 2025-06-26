# callAsFunction(ageGates:_:_:)

**Framework**: Declared Age Range  
**Kind**: method

Returns a response indicating whether the person has declared their age range.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
func callAsFunction(ageGates threshold1: Int, _ threshold2: Int? = nil, _ threshold3: Int? = nil) async throws -> AgeRangeService.Response
```

## Parameters

- `threshold1`: The first age gate threshold.
- `threshold2`: The second threshold in the age gate.
- `threshold3`: The minimum age for accessing the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/declaredagerangeaction/callasfunction(agegates:_:_:))*