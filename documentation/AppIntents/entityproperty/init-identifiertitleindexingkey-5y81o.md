# init(identifier:title:indexingKey:)

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
convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)
```

## Parameters

- `identifier`: The identifier of the property
- `title`: A word or short phrase summarizing this property.
- `indexingKey`: A Spotlight attribute set key mapping for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:title:indexingkey:)-5y81o)*