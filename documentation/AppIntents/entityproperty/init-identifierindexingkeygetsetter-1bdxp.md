# init(identifier:indexingKey:getSetter:)

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
convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>) where Entity : AppEntity
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:indexingkey:getsetter:)-1bdxp)*