# ResolvedValueQueryResult

**Framework**: App Intents Testing  
**Kind**: struct

The result of an intent value query.

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
struct ResolvedValueQueryResult
```

#### Overview

Use the resolved value query result to verify that your [`IntentValueQuery`](https://developer.apple.com/documentation/AppIntents/IntentValueQuery) returns the expected results as shown in the following example:

```swift
let result = try await searchQuery.values(for: "Arizona")

// Verify individual items.
XCTAssertEqual(try result.items[0].name, "Botanical Garden")

// Cast items to a concrete value for additional verifications.
let entity: AnyAppEntity =
    try result.items[0].as(AnyAppEntity.self)
```

## Topics

### Accessing query results
- [let items: DynamicPropertyPathCollection](resolvedvaluequeryresult/items.md)
  The results that the query returns.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ResolvedIntentResult](resolvedintentresult.md)
  A type-safe result from performing an app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/resolvedvaluequeryresult)*