# new Map(parent, options)

**Framework**: MapKit JS  
**Kind**: init

Creates a map you embed on a webpage and initializes it with the constructor options you choose.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(
        parent?: string | HTMLElement | null,
        options?: MapConstructorOptions,
    );
```

#### Return Value

A [`Map`](map.md) instance.

#### Discussion

The map’s constructor takes an optional `parent` argument and an optional `options` argument. If you specify the `parent` argument, MapKit JS inserts the map element into the DOM as a descendant of `parent` that it styles to fill the size of its enclosing element. A map defaults to showing the entire world.

The following example demonstrates how to add a map to a `DIV` element using HTML:

```other
<body>
	<div id="mapContainer"></div>
</body>
```

The following example demonstrates how to add a map to a `DIV` element using JavaScript:

```javascript
const map = new mapkit.Map('mapContainer', { center: new mapkit.Coordinate(37.334883, -122.008977) });
```

## Parameters

- `parent`: A DOM element, or the ID of a DOM element, to use as your map’s container.
- `options`: Options that   defines for initializing the properties of your map.

## See Also

- [interface MapConstructorOptions](mapconstructoroptions.md)
  An object that contains options for creating a map’s features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/mapconstructor)*