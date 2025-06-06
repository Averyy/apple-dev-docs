# Issue.Kind.timeLimitExceeded(timeLimitComponents:)

**Framework**: Swift Testing  
**Kind**: case

An issue due to a test reaching its time limit and timing out.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
indirect case timeLimitExceeded(timeLimitComponents: (seconds: Int64, attoseconds: Int64))
```

## Mentions

- [Limiting the running time of tests](limitingexecutiontime.md)

## Parameters

- `timeLimitComponents`: The time limit reached by the test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue/kind-swift.enum/timelimitexceeded(timelimitcomponents:))*