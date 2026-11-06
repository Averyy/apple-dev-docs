# equals(_:)

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Type Method

Creates an expectation that requires the value to be a string that equals a specified string.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
static func equals(_ value: String) -> Self
```

Available when `Self` is `PrimitiveExpectation`.

## Return Value

An expectation that compares a string value to `value`.

## Discussion

The comparison is exact and case-sensitive. A value that isn’t a string doesn’t satisfy the expectation.

## Parameters

- `value`: The string to compare the value to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentvalueexpectation/equals(_:))*