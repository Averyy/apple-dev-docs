# IntentValueQuery

**Framework**: App Intents  
**Kind**: protocol

A query that provides entity values to the system; for example, for visual intelligence search.

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
protocol IntentValueQuery : PersistentlyIdentifiable, _SupportsAppDependencies, Sendable
```

## Topics

### Associated Types
- [associatedtype Input : _IntentValue](intentvaluequery/input.md)
- [associatedtype Result : ResultsCollection = [Self.ResultValue]](intentvaluequery/result.md)
- [associatedtype ResultValue = Self.Result.Result.ValueType](intentvaluequery/resultvalue.md)
### Initializers
- [init()](intentvaluequery/init.md)
### Instance Methods
- [func values(for: Self.Input) async throws -> Self.Result](intentvaluequery/values(for:).md)

## Relationships

### Inherits From
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Integrating your app with visual intelligence](../VisualIntelligence/integrating-your-app-with-visual-intelligence.md)
  Enable people to find app content that matches their surroundings or objects onscreen with visual intelligence.
- [Visual Intelligence](../VisualIntelligence/VisualIntelligence.md)
  Include your app’s content in search results that visual intelligence provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvaluequery)*