# DeclaredAgeRangeAction

**Framework**: Declared Age Range  
**Kind**: struct

An action that requests a person’s age range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
struct DeclaredAgeRangeAction
```

#### Overview

Use `DeclaredAgeRangeAction` in SwiftUI views to request a person’s age range. It automatically handles platform differences between macOS and iOS.

## Topics

### Requesting the age range
- [func callAsFunction(ageGates: Int, Int?, Int?) async throws -> AgeRangeService.Response](declaredagerangeaction/callasfunction(agegates:_:_:).md)
  Returns a response indicating whether the person shared their age range.

## See Also

- [struct AgeRangeService](agerangeservice.md)
  A request for the age range of a person logged onto the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/declaredagerangeaction)*