# init(identifier:title:customIndexingKey:getter:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>) where Entity : AppEntity
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, `Value.ValueType` conforms to `Decodable`, and `Value.ValueType` conforms to `Encodable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:title:customindexingkey:getter:)-5dmv4)*