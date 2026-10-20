# codable

**Framework**: SwiftData  
**Kind**: property  
**Role**: Type Property

Uses the property’s codable representation to store the property.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Swift 5.9+

## Declaration

```swift
static var codable: Schema.Attribute.Option { get }
```

## See Also

### Accessing property options
- [static var allowsCloudEncryption: Schema.Attribute.Option](./allowscloudencryption.md)
  Stores the property’s value in an encrypted form.
- [static var externalStorage: Schema.Attribute.Option](./externalstorage.md)
  Stores the property’s value as binary data adjacent to the model storage.
- [static var preserveValueOnDeletion: Schema.Attribute.Option](./preservevalueondeletion.md)
  Preserves the property’s value in the persistent history when the context deletes the owning model.
- [static var spotlight: Schema.Attribute.Option](./spotlight.md)
  Indexes the property’s value so it can appear in Spotlight search results.
- [static var unique: Schema.Attribute.Option](./unique.md)
  Ensures the property’s value is unique across all models of the same type.
- [static func transformable(by: ValueTransformer.Type) -> Schema.Attribute.Option](./transformable%28by%29-9d4xh.md)
  Transforms the property’s value between an in-memory form and a persisted form.
- [static func transformable(by: String) -> Schema.Attribute.Option](./transformable%28by%29-lunz.md)
- [static var ephemeral: Schema.Attribute.Option](./ephemeral.md)
  Track changes to this property but do not persist


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/attribute/option/codable)*