# init(indexingKey:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent entity property.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
convenience init<Entity>(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>) where Entity : AppEntity, Value.ValueType == EntityCollection<Entity>
```

## Parameters

- `indexingKey`: A Spotlight attribute set key mapping for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(indexingkey:)-9nke3)*