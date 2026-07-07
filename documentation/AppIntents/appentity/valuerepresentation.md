# AppEntity.ValueRepresentation

**Framework**: App Intents  
**Kind**: typealias

A type alias for `IntentValueRepresentation`, providing a convenient way to define transfer representations that convert between app entities and system intent values.

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
typealias ValueRepresentation = IntentValueRepresentation
```

#### Discussion

Use `ValueRepresentation` in your entity’s `transferRepresentation` to enable bidirectional conversion with system types like `IntentPerson`, `PlaceDescriptor`, and other `_SystemIntentValue` types.

#### Example

```swift
struct ContactEntity: AppEntity, Transferable {
    static var transferRepresentation: some TransferRepresentation {
        ValueRepresentation(
            exporting: { entity in
                IntentPerson(
                    name: .displayName(entity.name),
                    handle: .init(emailAddress: entity.email)
                )
            },
            importing: { person in
                ContactEntity(
                    name: person.name.displayString,
                    email: person.handle?.value ?? ""
                )
            }
        )
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentity/valuerepresentation)*