# AnyMapContent

**Framework**: MapKit  
**Kind**: struct

A type-erased map content.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst ?+
- macOS 14.5+
- tvOS 17.5+
- visionOS 1.2+
- watchOS 10.5+

## Declaration

```swift
@MainActor
@preconcurrency struct AnyMapContent
```

#### Overview

An `AnyMapContent` allows changing the type of content used in a given map view.

## Topics

### Initializers
- [init<Content>(Content)](anymapcontent/init(_:).md)
  Create an instance that type-erases `base`.

## Relationships

### Conforms To
- [MapContent](mapcontent.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/anymapcontent)*