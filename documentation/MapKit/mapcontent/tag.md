# tag(_:)

**Framework**: MapKit  
**Kind**: method

Sets the unique tag value of this piece of map content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func tag<V>(_ tag: V) -> some MapContent where V : Hashable
```

#### Return Value

Map content with the specified tag set.

#### Discussion

Use this modifier to differentiate between selectable content in the map. When the map’s selection binding has the same value as the tag applied to a piece of map content, that content is considered selected.

A `ForEach` automatically applies a default tag to each enumerated view using the `id` parameter of the corresponding element. If the element’s `id` parameter and the the map’s selection input have the same type, you can omit the explicit tag modifier.

## Parameters

- `tag`: A    value to use as the map content’s tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/tag(_:))*