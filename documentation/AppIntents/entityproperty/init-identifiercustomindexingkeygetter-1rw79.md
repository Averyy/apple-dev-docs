# init(identifier:customIndexingKey:getter:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>) where Entity : AppEntity
```

## Parameters

- `identifier`: The identifier of the property
- `customIndexingKey`: A custom Spotlight attribute set key for this property.
- `getter`: The getter reference for the property


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:customindexingkey:getter:)-1rw79)*