# init(identifier:title:indexingKey:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)
```

## Parameters

- `identifier`: The identifier of the property
- `title`: A word or short phrase summarizing this property.
- `indexingKey`: A Spotlight attribute set key mapping for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:title:indexingkey:)-1p0ni)*