# FetchDelegate

**Framework**: MapKit JS  
**Kind**: class

An object to pass to a map feature annotation to fetch place objects instead of a callback function.

**Availability**:
- MapKit JS 5.74+

## Declaration

```swift
interface FetchDelegate
```

#### Overview

You can pass a `FetchDelegate` [`fetchPlace`](mapkit.mapfeatureannotation/fetchplace.md) instead of a callback function. If you provide a delegate object, it needs to have the following methods:

- `fetchDidComplete(data)` — MapKit JS calls this method on successful completion of a fetch request. The data object is the same as the one that passes to the fetch callback function.
- `fetchDidError(error)` — MapKit JS calls this method when the fetch request fails.

## Topics

### Callback methods
- [fetchDidComplete](fetchdelegate/fetchdidcomplete.md)
  Tells the receiver when the fetch request succeeds.
- [fetchDidError](fetchdelegate/fetchdiderror.md)
  Tells the receiver when the fetch request fails.

## See Also

- [ImageDelegate](imagedelegate.md)
  An object you use to specify image URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/fetchdelegate)*