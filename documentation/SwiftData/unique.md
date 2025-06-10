# Unique(_:)

**Framework**: SwiftData  
**Kind**: macro

Specifies the key-paths that SwiftData uses to enforce the uniqueness of model instances.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
@freestanding
(declaration) macro Unique<T>(_ constraints: [PartialKeyPath<T>]...) where T : PersistentModel
```

#### Overview

If a model class contains attributes that you require to be unique across all persisted instances of that model, add the `Unique` macro to that model’s definition. You can specify a constraint on a single attribute, a compound constraint across multiple attributes, or any combination of the two.

> ❗ **Important**: For relationship attributes, SwiftData only supports unique constraints on those that reference a single persistent model, rather than an array of persistent models.

The following example declares that every instance of `Person` has a unique `id`, and that no two instances of `Person` have the same `givenName` and `familyName`:

```swift
@Model
final class Person {
   // Declare any unique constraints as part of the model definition.
   #Unique<Person>([\.id], [\.givenName, \.familyName])

   var id: UUID
   var givenName: String
   var familyName: String

   init(id: UUID, givenName: String, familyName: String) {
       self.id = id
       self.givenName = givenName
       self.familyName = familyName
   }
}
```

## Parameters

- `constraints`: Arrays of model key-paths that form the unique constraints to apply to the enclosing   model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/unique(_:))*