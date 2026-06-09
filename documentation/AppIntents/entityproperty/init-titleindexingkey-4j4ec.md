# init(title:indexingKey:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent entity property.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)
```

## Parameters

- `title`: A word or short phrase summarizing this property.
- `indexingKey`: A Spotlight attribute set key mapping for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(title:indexingkey:)-4j4ec)*