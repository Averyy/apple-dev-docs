# init(identifier:title:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
convenience init(identifier: String, title: LocalizedStringResource)
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` conforms to `_SystemIntentValue`.

## Parameters

- `identifier`: The identifier of the property
- `title`: A word or short phrase summarizing this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:title:)-2uf8c)*