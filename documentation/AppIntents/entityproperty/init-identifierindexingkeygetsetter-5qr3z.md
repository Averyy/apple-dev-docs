# init(identifier:indexingKey:getSetter:)

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
convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>) where Entity : AppEntity, Value.ValueType == EntityCollection<Entity>
```

## Parameters

- `identifier`: The identifier of the property
- `indexingKey`: A Spotlight attribute set key mapping for this property.
- `getSetter`: The getter reference for the property


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:indexingkey:getsetter:)-5qr3z)*