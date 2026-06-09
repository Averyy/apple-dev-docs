# phonePerson

**Framework**: App Intents  
**Kind**: property

An entity schema for a phone person.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var phonePerson: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `phone` domain and its content matches the `phonePerson` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .phone.phonePerson)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `phonePerson` schema:

```swift
@AppEntity(schema: .phone.phonePerson)
struct PhonePerson {
    // MARK: Static

    static let defaultQuery = PhonePersonQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var person: IntentPerson

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct PhonePersonQuery: EntityQuery {
        func entities(for identifiers: [PhonePerson.ID]) async throws -> [PhonePerson] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [AppSchema.PhoneEntity](appschema/phoneentity.md)
  Identifies entity schemas in the phone domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/phoneentity/phoneperson)*