# init(identifier:customIndexingKey:asyncGetter:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent entity property.  Do not call this directly, use @Property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: @escaping @Sendable (Entity) async throws -> Value) where Entity : AppEntity
```

## Parameters

- `identifier`: The identifier of the property
- `customIndexingKey`: A custom Spotlight attribute set key for this property.
- `asyncGetter`: The getter reference for the property


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:customindexingkey:asyncgetter:)-5wwp6)*