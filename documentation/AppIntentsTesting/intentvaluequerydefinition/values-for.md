# values(for:)

**Framework**: App Intents Testing  
**Kind**: method

Performs the value query with the given input and returns matching results.

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
func values(for input: some IntentValueConvertible) async throws -> ResolvedValueQueryResult
```

#### Return Value

Results matching the query.

#### Discussion

Use this function to verify that the system can query your app for app entities as shown in the following example:

```swift
let searchQuery = definitions.valueQueries[
    "LandmarkIntentValueQuery"
]
let result = try await searchQuery.values(
    for: "Arizona"
)
let name: String = try result.items[0].name
```

## Parameters

- `input`: The value to use in this query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentvaluequerydefinition/values(for:))*