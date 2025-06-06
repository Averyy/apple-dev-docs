# getImageUrl

**Framework**: MapKit JS  
**Kind**: method

Returns the image URL of the map feature.

**Availability**:
- MapKit JS 5.74+

## Declaration

```swift
void getImageUrl(
	number scale,
	function callback
);
```

#### Discussion

The method returns the URL as the first argument of `callback`. The URL is a `blob:` URL. To avoid a memory leak, you need to revoke it with [`revokeObjectURL`](https://developer.apple.com/documentation/webkitjs/domurl/1630984-revokeobjecturl) when you no longer need it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.mapfeatureannotationglyphimage/getimageurl)*