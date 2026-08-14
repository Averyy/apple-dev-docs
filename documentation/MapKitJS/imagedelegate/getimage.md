# getImage(ratio)

**Framework**: MapKit JS  
**Kind**: method

Returns an image for the specified scale.

**Availability**:
- MapKit JS 6.0+

## Declaration

```swift
getImage?(ratio: number): Promise<string | ImageSource | undefined>;
```

## Mentions

- [MapKit JS 6](mapkit-js-6.md)
- [Migrating from Version 5 to Version 6](migrating-from-version-5-to-version-6.md)

#### Discussion

Implement this method to return a `Promise` that resolves to a URL string, an [`ImageSource`](imagesource.md), or `undefined` if no image is available. MapKit JS calls this method with a pixel ratio value that your function uses to provide an appropriately scaled image.

When both [`getImage()`](imagedelegate/getimage.md) and [`getImageUrl()`](imagedelegate/getimageurl.md) are present, the framework uses [`getImage()`](imagedelegate/getimage.md).

```javascript
const imageDelegate = {
    async getImage(scale) {
        const response = await fetch(`https://example.com/images/marker?scale=${scale}`, {
            headers: { "Authorization": "Bearer " + token }
        });
        if (!response.ok) return undefined;
        const blob = await response.blob();
        return createImageBitmap(blob);
    }
};

const annotation = new mapkit.ImageAnnotation(
    new mapkit.Coordinate(10, 10),
    { image: imageDelegate }
);
```

## See Also

- [getImageUrl(ratio, callback)](imagedelegate/getimageurl.md)
  Returns the URL to an image of the specified scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imagedelegate/getimage)*