# init(identifier:title:customIndexingKey:asyncGetter:)

**Framework**: App Intents  
**Kind**: init

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: @escaping @Sendable (Entity) async throws -> Value) where Entity : AppEntity
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:title:customindexingkey:asyncgetter:)-6sbmw)*