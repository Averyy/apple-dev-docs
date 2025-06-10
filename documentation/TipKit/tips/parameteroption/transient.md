# ParameterOption.transient

**Framework**: TipKit  
**Kind**: property

An option that resets the parameter value the first time it is referenced.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static var transient: Tips.ParameterOption { get }
```

#### Overview

Use this option to to reset your parameter to a default value between app launches.

```swift
struct LandmarksUser {
    // Define the user interaction you want to use for a display rule.
    @Parameter(.transient)
    static var lastViewedLandmark: Landmark? = nil
}
```

## See Also

- [struct Parameter](tips/parameter.md)
  A type that monitors the state of its wrapped value to reevaluate any dependent tip rules when the value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/parameteroption/transient)*