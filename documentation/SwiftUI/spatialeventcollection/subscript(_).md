# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript

Retrieves an event using its unique identifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
subscript(index: SpatialEventCollection.Event.ID) -> SpatialEventCollection.Event? { get }
```

#### Overview

Returns `nil` if the `Event` no longer exists in the collection.

## See Also

- [SpatialEventCollection.Event](spatialeventcollection/event.md)
  A spatial event generated from an input like a touch or click that can drive gestures in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/subscript(_:))*