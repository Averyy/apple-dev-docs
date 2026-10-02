# init(importing:)

**Framework**: App Intents  
**Kind**: init

Creates a value representation that imports an `IntentPerson` into an entity.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
init(importing: @escaping @Sendable (IntentValue) async throws -> Item)
```

#### Discussion

Use this initializer when your entity can be created from an `IntentPerson`, but has no meaningful representation to export back out. The entity’s metadata declares `IntentPerson` as importable only, and the entity is never offered for export as a person.

#### Example

```swift
struct ContactEntity: AppEntity, Transferable {
    static var transferRepresentation: some TransferRepresentation {
        ValueRepresentation(
            importing: { person in
                guard case let .applicationDefined(id) = person.identifier?.value else {
                    throw ImportError.missingIdentifier
                }
                return ContactEntity(
                    id: id,
                    name: person.name.displayString,
                    email: person.handle?.value ?? ""
                )
            }
        )
    }
}
```

## Parameters

- `importing`: A closure that converts an IntentPerson to an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvaluerepresentation/init(importing:)-6jio8)*