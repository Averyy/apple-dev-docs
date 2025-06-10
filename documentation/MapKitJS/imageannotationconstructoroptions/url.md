# url

**Framework**: MapKit JS  
**Kind**: property

An object containing URLs for the image assets in multiple resolutions.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute Object url;
```

#### Discussion

This property is an object literal containing absolute or relative URLs to standard, 2×, and 3× Retina assets. MapKit JS requires at least one image URL.

```javascript
{
    url: {
        1: "example.png",
        2: "example_2x.png",
        3: "example_3x.png"
    }
}
```

If you choose not to provide standard and Retina resolution assets, you have two options:

- Set “1” to a URL to a standard resolution image. This results in blurry images on Retina displays.
- Set “1” to a URL to a Retina image. Set the size to the desired size. This results in crisp images on Retina displays and good images on standard displays, but it’s less optimal than custom, pixel-fitted images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imageannotationconstructoroptions/url)*