# AppShortcutOptionsCollectionSpecification

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
protocol AppShortcutOptionsCollectionSpecification<Value> : Sendable, Sequence where Self.Element == any AppShortcutOptionsCollectionProtocol
```

## Topics

### Associated Types
- [associatedtype Value : _IntentValue](./appshortcutoptionscollectionspecification/value.md)

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### App Shortcut options
- [struct AppShortcutOptionsCollection](./appshortcutoptionscollection.md)
  Represents a collection of options for parameters of an App Shortcut.
- [protocol AppShortcutOptionsCollectionProtocol](./appshortcutoptionscollectionprotocol.md)
- [enum AppShortcutOptionsCollectionSpecificationBuilder](./appshortcutoptionscollectionspecificationbuilder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutoptionscollectionspecification)*