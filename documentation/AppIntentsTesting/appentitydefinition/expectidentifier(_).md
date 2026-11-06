# expectIdentifier(_:)

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Instance Method

Creates an expectation that an app entity is the instance with the specified identifier.

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
func expectIdentifier(_ identifier: String) -> AppEntityIdentifierExpectation
```

## Return Value

An expectation that compares an entity’s identifier to `identifier`.

## Discussion

Use the returned expectation for an intent parameter, an intent result, or a property that holds an entity. Call [`expect`](../appentityidentifierexpectation/expect.md) on it to also check the instance’s properties. For example:

```swift
let workCalendarExpectation = createEventIntentDefinition.expect(
    calendar: calendarEntityDefinition.expectIdentifier(
        "edea53fb-90b7-4481-afc7-d86e2dd0d27d"
    )
)
```

## Parameters

- `identifier`: The identifier of the entity instance to expect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/expectidentifier(_:))*