# AppShortcutOptionsCollectionSpecification

**Framework**: App Intents  
**Kind**: protocol

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
protocol AppShortcutOptionsCollectionSpecification<Value> : Sendable, Sequence where Self.Element == any AppShortcutOptionsCollectionProtocol
```

## Topics

### Associated Types
- [associatedtype Value : _IntentValue](appshortcutoptionscollectionspecification/value.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct AppShortcutOptionsCollection](appshortcutoptionscollection.md)
  Represents a collection of options for parameters of an App Shortcut.
- [protocol AppShortcutOptionsCollectionProtocol](appshortcutoptionscollectionprotocol.md)
- [enum AppShortcutOptionsCollectionSpecificationBuilder](appshortcutoptionscollectionspecificationbuilder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutoptionscollectionspecification)*