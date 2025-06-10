# init(identifier:customIndexingKey:getter:)

**Framework**: App Intents  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>) where Entity : AppEntity
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:customindexingkey:getter:)-570s4)*