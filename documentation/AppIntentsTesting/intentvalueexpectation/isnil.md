# isNil

**Framework**: App Intents Testing  
**Kind**: property  
**Role**: Type Property

An expectation that requires a parameter, property, or result to have no value.

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
static var isNil: PrimitiveExpectation { get }
```

Available when `Self` is `PrimitiveExpectation`.

## Discussion

Use this expectation to check that a value is absent. To leave a value unchecked, pass `nil` or leave out its label instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentvalueexpectation/isnil)*