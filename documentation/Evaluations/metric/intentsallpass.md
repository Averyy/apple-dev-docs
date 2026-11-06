# intentsAllPass

**Framework**: Evaluations  
**Kind**: property  
**Role**: Type Property

A metric that passes when every intent expectation in the scenario holds.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- Xcode 27.0+

## Declaration

```swift
static let intentsAllPass: Metric
```

## Discussion

This covers `Calls` of every ordering: ordered, unordered and disallowed. The report’s table shows each one that did not hold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/intentsallpass)*