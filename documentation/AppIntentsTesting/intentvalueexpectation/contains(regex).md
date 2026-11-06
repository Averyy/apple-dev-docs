# contains(regex:)

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Type Method

Creates an expectation that requires the value to be a string that contains a match for a regular expression.

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
static func contains(regex: String) -> Self
```

Available when `Self` is `PrimitiveExpectation`.

## Return Value

An expectation that searches a string value for a match for `regex`.

## Discussion

The regular expression can match anywhere in the string, so `.contains(regex: "Building")` also matches “Old Building 4”. To match the whole string, anchor the regular expression with `^` and `$`. A value that isn’t a string doesn’t satisfy the expectation.

## Parameters

- `regex`: The regular expression to search for in the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentvalueexpectation/contains(regex:))*