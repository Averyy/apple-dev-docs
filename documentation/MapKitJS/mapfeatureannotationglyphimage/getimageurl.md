# getImageUrl(scale, callback)

**Framework**: MapKit JS  
**Kind**: method

Returns the image URL of the map feature.

**Availability**:
- MapKit JS 5.74.1+

## Declaration

```swift
getImageUrl(
        scale: number | undefined,
        callback: (url?: string) => void,
    ): void;
```

#### Discussion

The method returns the URL as the first argument of `callback`. The URL is a `blob:` URL. To avoid a memory leak, you need to revoke it with `URL.revokeObjectURL()` when you no longer need it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapfeatureannotationglyphimage/getimageurl)*