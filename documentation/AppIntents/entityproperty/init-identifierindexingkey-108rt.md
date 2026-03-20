# init(identifier:indexingKey:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst ?+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)
```

## Parameters

- `identifier`: The identifier of the property
- `indexingKey`: A Spotlight attribute set key mapping for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:indexingkey:)-108rt)*