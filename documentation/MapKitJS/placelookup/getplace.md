# getPlace(id, callback, options)

**Framework**: MapKit JS  
**Kind**: method

Obtains a place using its identifier.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```swift
getPlace(
        id: string,
        callback: (error: Error | null, result?: Place) => void,
        options?: ServiceConstructorOptions,
    ): number;
```

#### Discussion

For information about Places, see [`Identifying unique locations with Place IDs`](https://developer.apple.com/documentation/MapKit/identifying-unique-locations-with-place-ids).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/placelookup/getplace)*