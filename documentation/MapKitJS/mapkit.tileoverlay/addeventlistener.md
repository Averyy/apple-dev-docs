# addEventListener

**Framework**: MapKit JS  
**Kind**: method

Listens for events of the specified type.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
void addEventListener(
	string type,
	function listener,
	optional Object thisObject
);
```

#### Discussion

Adds `listener` as a callback for an event of type `type`. Throws an error if `type` is invalid.

|  |  |
| --- | --- |
| `tile-error` | For each tile load failure, MapKit JS dispatches a `tile-error` event with two properties: ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 	•	`tileOverlay`: the tile overlay containing the failing tile. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 	•	`tileUrl`: the specific tile URL string that failed. |

## Parameters

- `type`: The required event type, such as  .
- `listener`: The required event listener function or delegate object to invoke.
- `thisObject`: An optional object set as the   keyword on the   function.

## See Also

- [removeEventListener](mapkit.tileoverlay/removeeventlistener.md)
  Stops listening for events of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.tileoverlay/addeventlistener)*