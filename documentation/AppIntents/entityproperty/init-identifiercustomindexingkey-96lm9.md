# init(identifier:customIndexingKey:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst ?+
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)
```

## Parameters

- `identifier`: The identifier of the property
- `customIndexingKey`: A custom Spotlight attribute set key for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:customindexingkey:)-96lm9)*