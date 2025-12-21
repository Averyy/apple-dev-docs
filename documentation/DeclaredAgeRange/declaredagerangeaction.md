# DeclaredAgeRangeAction

**Framework**: Declared Age Range  
**Kind**: struct

An action that requests a person’s declared age range with automatic UI context management.

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

Use [`DeclaredAgeRangeAction`](declaredagerangeaction.md) in SwiftUI views to request age ranges without manually managing the presentation context. This action automatically handles the differences between macOS windows and iOS view controllers, providing a unified interface for age range requests across platforms.

## Topics

### Requesting the age range
- [func callAsFunction(ageGates: Int, Int?, Int?) async throws -> AgeRangeService.Response](declaredagerangeaction/callasfunction(agegates:_:_:).md)
  Returns a response indicating whether the person has set their age range.

## See Also

- [struct AgeRangeService](agerangeservice.md)
  A request for the age range of a person logged onto the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/declaredagerangeaction)*