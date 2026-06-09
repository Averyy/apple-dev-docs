# init(identifier:asyncGetter:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
convenience init<Entity>(identifier: String, asyncGetter: @escaping @Sendable (Entity) async throws -> Value) where Entity : AppEntity
```

## Parameters

- `identifier`: The identifier of the property
- `asyncGetter`: The getter reference for the property


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:asyncgetter:)-7z385)*