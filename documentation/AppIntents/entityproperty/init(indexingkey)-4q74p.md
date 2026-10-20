# init(indexingKey:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Creates an app intent entity property.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitPower>`.

## Parameters

- `indexingKey`: A Spotlight attribute set key mapping for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(indexingkey:)-4q74p)*