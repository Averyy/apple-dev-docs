# expect

**Framework**: App Intents Testing  
**Kind**: property  
**Role**: Instance Property

A callable that creates an entity expectation from value expectations for the entity’s properties.

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
var expect: IntentValueExpectationCallable<any IntentValueExpectation, AppEntityExpectation> { get }
```

## Discussion

Call `expect` with a labeled argument for each property you want to check. Each label names a property, and each argument is the value expectation for it. The expectation doesn’t check properties you omit or pass `nil` for. Pass [`isNil`](../intentvalueexpectation/isnil.md) to expect a property to be absent. For example:

```swift
let expectation = eventEntityDefinition.expect(
    title: .contains("NASA"),
    endDate: .isNil
)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/expect)*