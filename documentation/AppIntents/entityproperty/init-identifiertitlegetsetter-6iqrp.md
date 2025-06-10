# init(identifier:title:getSetter:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>) where Entity : AppEntity
```

## Parameters

- `identifier`: The identifier of the property
- `title`: A word or short phrase summarizing this property.
- `getSetter`: The getter reference for the property


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:title:getsetter:)-6iqrp)*