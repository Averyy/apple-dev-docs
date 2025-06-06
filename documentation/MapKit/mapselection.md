# MapSelection

**Framework**: MapKit  
**Kind**: struct

A value representing a selected feature on a map.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct MapSelection<SelectionValue> where SelectionValue : Hashable
```

## Topics

### Creating a map selection
- [init(SelectionValue)](mapselection/init(_:).md)
  Creates a map selection with a tag.
### Getting the properties
- [var value: SelectionValue?](mapselection/value.md)
  The selection of the given tag value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MapSelectable](mapselectable.md)

## See Also

- [struct MapFeature](mapfeature.md)
  A tappable map feature.
- [protocol MapSelectable](mapselectable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapselection)*