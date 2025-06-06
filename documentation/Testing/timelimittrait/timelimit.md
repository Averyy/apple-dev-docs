# timeLimit(_:)

**Framework**: Swift Testing  
**Kind**: method

Construct a time limit trait that causes a test to time out if it runs for too long.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
static func timeLimit(_ timeLimit: TimeLimitTrait.Duration) -> Self
```

#### Return Value

An instance of [`TimeLimitTrait`](timelimittrait.md).

#### Discussion

Test timeouts do not support high-precision, arbitrarily short durations due to variability in testing environments. You express the duration in minutes, with a minimum duration of one minute.

When you associate this trait with a test, that test must complete within a time limit of, at most, `timeLimit`. If the test runs longer, the testing library records a [`Issue.Kind.timeLimitExceeded(timeLimitComponents:)`](issue/kind-swift.enum/timelimitexceeded(timelimitcomponents:).md) issue, which it treats as a test failure.

The testing library can use a shorter time limit than that specified by `timeLimit` if you configure it to enforce a maximum per-test limit. When you configure a maximum per-test limit, the time limit of the test this trait is applied to is the shorter of `timeLimit` and the maximum per-test limit. For information on configuring maximum per-test limits, consult the documentation for the tool you use to run your tests.

If a test is parameterized, this time limit is applied to each of its test cases individually. If a test has more than one time limit associated with it, the testing library uses the shortest time limit.

## Parameters

- `timeLimit`: The maximum amount of time the test may run for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/timelimittrait/timelimit(_:))*