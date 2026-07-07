# init(exporting:importing:)

**Framework**: App Intents  
**Kind**: init

an entity and an `IntentPerson`.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
init(exporting: @escaping @Sendable (Item) async throws -> IntentValue, importing: @escaping @Sendable (IntentValue) async throws -> Item)
```

#### Example

```swift
struct ContactEntity: AppEntity, Transferable {
    static var transferRepresentation: some TransferRepresentation {
        ValueRepresentation(
            exporting: { contact in
                IntentPerson(
                    identifier: .applicationDefined(contact.id),
                    name: .displayName(contact.name),
                    handle: .init(emailAddress: contact.email)
                )
            },
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

- `exporting`: A closure that converts an entity to an IntentPerson.
- `importing`: A closure that converts an IntentPerson back to an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvaluerepresentation/init(exporting:importing:)-550j7)*