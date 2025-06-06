# Issue.Kind.confirmationMiscounted(actual:expected:)

**Framework**: Swift Testing  
**Kind**: case

An issue due to a confirmation being confirmed the wrong number of times.

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
indirect case confirmationMiscounted(actual: Int, expected: any RangeExpression & Sendable)
```

#### Discussion

This issue can occur when calling [`confirmation(_:expectedCount:isolation:sourceLocation:_:)`](confirmation(_:expectedcount:isolation:sourcelocation:_:)-5mqz2.md) or [`confirmation(_:expectedCount:isolation:sourceLocation:_:)`](confirmation(_:expectedcount:isolation:sourcelocation:_:)-l3il.md) when the confirmation passed to these functions’ `body` closures is confirmed too few or too many times.

## Parameters

- `actual`: The number of times   was   actually called.
- `expected`: The expected number of times    should have been called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue/kind-swift.enum/confirmationmiscounted(actual:expected:))*