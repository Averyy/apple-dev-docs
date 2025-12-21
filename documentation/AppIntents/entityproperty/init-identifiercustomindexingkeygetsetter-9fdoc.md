# init(identifier:customIndexingKey:getSetter:)

**Framework**: App Intents  
**Kind**: init

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>) where Entity : AppEntity
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:customindexingkey:getsetter:)-9fdoc)*