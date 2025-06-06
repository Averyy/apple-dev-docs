# transformable(by:)

**Framework**: SwiftData  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
static func transformable(by transformerName: String) -> Schema.Attribute.Option
```

## See Also

- [static var allowsCloudEncryption: Schema.Attribute.Option](schema/attribute/option/allowscloudencryption.md)
  Stores the property’s value in an encrypted form.
- [static var externalStorage: Schema.Attribute.Option](schema/attribute/option/externalstorage.md)
  Stores the property’s value as binary data adjacent to the model storage.
- [static var preserveValueOnDeletion: Schema.Attribute.Option](schema/attribute/option/preservevalueondeletion.md)
  Preserves the property’s value in the persistent history when the context deletes the owning model.
- [static var spotlight: Schema.Attribute.Option](schema/attribute/option/spotlight.md)
  Indexes the property’s value so it can appear in Spotlight search results.
- [static var unique: Schema.Attribute.Option](schema/attribute/option/unique.md)
  Ensures the property’s value is unique across all models of the same type.
- [static func transformable(by: ValueTransformer.Type) -> Schema.Attribute.Option](schema/attribute/option/transformable(by:)-9d4xh.md)
  Transforms the property’s value between an in-memory form and a persisted form.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/attribute/option/transformable(by:)-lunz)*