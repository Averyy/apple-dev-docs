# AnyAppEnum

**Framework**: App Intents Testing  
**Kind**: struct

A type-erased representation of an app enumeration that provides dynamic enumeration value access.

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
struct AnyAppEnum
```

#### Overview

Use `AnyAppEnum` to work with enumerations when you don’t know the specific enumeration type at compile time. At compile, the [`AnyAppEnum`](anyappenum.md) structure resolves to your app enum type and gives you access to its value as shown in the following example:

```swift
let definitions = IntentDefinitions(
    bundleIdentifier: "com.apple.example"
)
let colorEnum = definitions.enums["Color"]
let priorityEnum = definitions.enums["Priority"]

// Creating enumeration cases.
let redCase = colorEnum.makeCase("red")
let highPriority = priorityEnum.makeCase("high")

// Accessing enumeration properties.
let rawValue = redCase.rawValue  // "red"

// Converting raw values in a type-safe way.
let colorName = try redCase.as(String.self)
let priorityLevel = try highPriority.as(String.self)
```

## Topics

### Creating an enum
- [init(typeIdentifier: String, rawValue: String)](anyappenum/init(typeidentifier:rawvalue:).md)
  Creates a new instance with the specified enumeration identifier and raw value.
- [init(typeIdentifier: String, value: any LosslessStringConvertible)](anyappenum/init(typeidentifier:value:).md)
  Creates an enumeration with a typed raw value.
- [var typeIdentifier: String](anyappenum/typeidentifier.md)
  The enumeration’s type identifier.
- [var rawValue: String](anyappenum/rawvalue.md)
  The raw value of the selected enumeration option.
### Converting enum values
- [func `as`<T>(T.Type) throws -> T](anyappenum/as(_:).md)
  Casts the raw value to the specified type.
### Default Implementations
- [CustomStringConvertible Implementations](anyappenum/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [IntentValueConvertible](../AppIntents/IntentValueConvertible.md)
- [IntentValueExpressing](../AppIntents/IntentValueExpressing.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AnyAppIntent](anyappintent.md)
  A type-erased, intermediate representation of an app intent for testing purposes.
- [struct AnyAppEntity](anyappentity.md)
  A type-erased, intermediate representation of your app entity for testing purposes.
- [struct AnyEntityQuery](anyentityquery.md)
  A type-erased, intermediate representation of your entity query for testing purposes.
- [struct AnyTransientAppEntity](anytransientappentity.md)
  A type-erased representation of a transient app entity that provides dynamic property access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/anyappenum)*