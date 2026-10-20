# init(identifier:getSetter:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>) where Entity : AppEntity
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitConcentrationMass>`.

## Parameters

- `identifier`: The identifier of the property
- `getSetter`: The getter reference for the property


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:getsetter:)-6aix5)*