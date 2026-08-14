# AnyAppIntent

**Framework**: App Intents Testing  
**Kind**: struct

A type-erased, intermediate representation of an app intent for testing purposes.

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
struct AnyAppIntent
```

#### Overview

The [`AnyAppIntent`](anyappintent.md) structure resolves to your actual app intent type and gives you access to its parameters and results at runtime, enabling you to test your app intent code as shown in the following example:

```swift
// Getting an intent definition and creating an instance.
let definitions = IntentDefinitions(
    bundleIdentifier: "com.example.app"
)
var intent = definitions.intents["CreateNote"]
    .makeIntent()

// Setting any intent parameters.
intent.title = "Meeting Notes"
intent.priority = 5
intent.isUrgent = true

// Reading parameters, when needed.
let title: String? = try intent.title

// Performing the intent.
let result = try await intent.run()

// Adding your verification code.
// ...
```

## Topics

### Identifying the intent
- [let bundleIdentifier: String](anyappintent/bundleidentifier.md)
  The bundle identifier of the app that contains this intent.
- [let identifier: String](anyappintent/identifier.md)
  The unique identifier for the intent type.
### Performing the intent
- [func run() async throws -> ResolvedIntentResult](anyappintent/run.md)
  Performs the intent in the current test session.
### Subscripts
- [subscript<T>(dynamicMember _: String) -> T](anyappintent/subscript(dynamicmember:)-127ab.md)
  Accesses an intent parameter by name, for comparison with a known value.
- [subscript(dynamicMember _: String) -> DynamicPropertyPath](anyappintent/subscript(dynamicmember:)-7agfn.md)
  Accesses a nested entity property by name.
- [subscript(dynamicMember _: String) -> (any IntentValueExpressing)?](anyappintent/subscript(dynamicmember:)-8l8h0.md)
  Accesses an intent parameter by name, without casting.
### Default Implementations
- [CustomStringConvertible Implementations](anyappintent/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AnyAppEntity](anyappentity.md)
  A type-erased, intermediate representation of your app entity for testing purposes.
- [struct AnyEntityQuery](anyentityquery.md)
  A type-erased, intermediate representation of your entity query for testing purposes.
- [struct AnyAppEnum](anyappenum.md)
  A type-erased representation of an app enumeration that provides dynamic enumeration value access.
- [struct AnyTransientAppEntity](anytransientappentity.md)
  A type-erased representation of a transient app entity that provides dynamic property access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/anyappintent)*