# getImageUrl(ratio, callback)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Interface Method

Returns the URL to an image of the specified scale.

**Availability**:
- MapKit JS 5.74+ - Deprecated in 6.0

> **Deprecated**: Use [`getImage()`](./getimage.md) instead, which supports both URLs and [`ImageSource`](../imagesource.md) objects.

## Declaration

```
getImageUrl?(ratio: number, callback: (url: string | null) => void): void;
```

## Mentions

- [MapKit JS 6](../mapkit-js-6.md)

## See Also

### Returning an image
- [getImage(ratio)](./getimage.md)
  Returns an image for the specified scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imagedelegate/getimageurl)*