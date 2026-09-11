# init(identifier:title:indexingKey:asyncGetter:)

**Framework**: App Intents  
**Kind**: init

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: @escaping @Sendable (Entity) async throws -> Value) where Entity : AppEntity
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:title:indexingkey:asyncgetter:)-6jp2s)*