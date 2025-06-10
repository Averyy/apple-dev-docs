# init(identifier:asyncGetter:)

**Framework**: App Intents  
**Kind**: init

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
convenience init<Entity>(identifier: String, asyncGetter: @escaping (Entity) async throws -> Value) where Entity : AppEntity
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:asyncgetter:)-5fs2j)*