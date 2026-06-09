# ResolvedIntentResult

**Framework**: App Intents Testing  
**Kind**: struct

A type-safe result from performing an app intent.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@dynamicMemberLookup
struct ResolvedIntentResult
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Overview

After performing the app intent with [`run()`](anyappintent/run().md), use the `value` property to inspect the output as shown in the following example:

```swift
let result = try await intent.run()

// Compare the result with an expected value.
XCTAssertEqual(try result.value, "Hello World")

// Access the return value's nested properties.
let name: String = try result.value.customerName

// Pass the return value to another intent for additional verification.
intent2.coffee = try result.value
```

## Topics

### Supporting types
- [ResolvedIntentResult.ValueKeyPath](resolvedintentresult/valuekeypath.md)
  A structure that enables key-path syntax for the intent result.
### Subscripts
- [subscript(dynamicMember _: KeyPath<ResolvedIntentResult.ValueKeyPath, Never>) -> DynamicPropertyPath](resolvedintentresult/subscript(dynamicmember:)-69dzb.md)
  Accesses nested properties of the result’s return value.
- [subscript(dynamicMember _: KeyPath<ResolvedIntentResult.ValueKeyPath, Never>) -> (any IntentValueExpressing)?](resolvedintentresult/subscript(dynamicmember:)-7og7e.md)
  Accesses the return value of the result, without casting.
- [subscript<T>(dynamicMember _: KeyPath<ResolvedIntentResult.ValueKeyPath, Never>) -> T](resolvedintentresult/subscript(dynamicmember:)-kbqk.md)
  Returns the intent’s output, converted to the inferred type.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ResolvedValueQueryResult](resolvedvaluequeryresult.md)
  The result of an intent value query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/resolvedintentresult)*