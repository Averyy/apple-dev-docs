# fetchPlace(callback)

**Framework**: MapKit JS  
**Kind**: method

Fetches the place object associated with the map feature.

**Availability**:
- MapKit JS 5.74.1+

## Declaration

```swift
fetchPlace(callback: (error: Error | null, result?: Place) => void): number;
```

## Parameters

- `callback`: Required. The framework invokes the callback function with two arguments, `error` and `data,` on success or failure: - error — Contains an error code and a message that describes the error.
- data — A data object that contains an array with one [`Place`](place.md) object associated with the map feature, or an empty array if the server can’t return the specified place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapfeatureannotation/fetchplace)*