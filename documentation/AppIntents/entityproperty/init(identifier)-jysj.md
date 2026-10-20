# init(identifier:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
convenience init<Entity>(identifier: String) where Entity : AppEntity, Value.ValueType == EntityCollection<Entity>
```

Available when `Value` conforms to `_IntentValue` and `Sendable`.

## Parameters

- `identifier`: The identifier of the property


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:)-jysj)*