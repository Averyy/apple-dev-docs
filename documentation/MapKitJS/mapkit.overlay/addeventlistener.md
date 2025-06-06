# addEventListener

**Framework**: MapKit JS  
**Kind**: method

Starts listening for the specified type of event.

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

Adds `listener` as an event listener for an event of `type`. Throws an error if `type` is invalid.

|  |  |
| --- | --- |
| `select` | The overlay’s `selected` property is `true`. |
| `deselect` | The overlay’s `selected` property is `false`. |

## Parameters

- `type`: A required string that represents the event type, such as  .
- `listener`: The required event listener (function or object that implements the   interface) to invoke.
- `thisObject`: An optional object set as the   keyword on the   function.

## See Also

- [removeEventListener](mapkit.overlay/removeeventlistener.md)
  Stops listening for the specified type of event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.overlay/addeventlistener)*