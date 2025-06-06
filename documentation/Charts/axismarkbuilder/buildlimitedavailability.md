# buildLimitedAvailability(_:)

**Framework**: Swift Charts  
**Kind**: method

Provides support for “if” statements with `#available()` clauses in multi-statement closures, producing conditional content for the “then” branch, i.e. the conditionally-available branch.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func buildLimitedAvailability<Content>(_ content: Content) -> AnyAxisMark where Content : AxisMark
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axismarkbuilder/buildlimitedavailability(_:))*