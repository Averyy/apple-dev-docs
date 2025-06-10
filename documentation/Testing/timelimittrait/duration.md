# TimeLimitTrait.Duration

**Framework**: Swift Testing  
**Kind**: struct

A type representing the duration of a time limit applied to a test.

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
struct Duration
```

#### Overview

Use this type to specify a test timeout with [`TimeLimitTrait`](timelimittrait.md). `TimeLimitTrait` uses this type instead of Swift’s built-in `Duration` type because the testing library doesn’t support high-precision, arbitrarily short durations for test timeouts. The smallest unit of time you can specify in a `Duration` is minutes.

## Topics

### Type Methods
- [static func minutes(some BinaryInteger) -> TimeLimitTrait.Duration](timelimittrait/duration/minutes(_:).md)
  Construct a time limit duration given a number of minutes.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/timelimittrait/duration)*