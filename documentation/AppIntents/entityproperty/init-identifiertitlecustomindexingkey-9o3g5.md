# init(identifier:title:customIndexingKey:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey) where Entity : AppEntity, Value.ValueType == EntityCollection<Entity>
```

## Parameters

- `identifier`: The identifier of the property
- `title`: A word or short phrase summarizing this property.
- `customIndexingKey`: A custom Spotlight attribute set key for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:title:customindexingkey:)-9o3g5)*