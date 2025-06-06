# width

**Framework**: Tvml

Specifies the maximum width for an image element.

#### Overview

The image is shrunk to fit the bounding box if the image is bigger than the size specified for the `width` attribute. You must declare either a `width` style or attribute for an image. Declaring a style overwrites an attribute declaration. Here’s an example that sets the width for an image to 200 points.

```xml
<img src="resource://mpaa-g" width="200">
```

##### Values for Width

##### Elements That Use Width

- [`decorationLabel`](decorationlabel.md)
- [`fullscreenImg`](fullscreenimg.md)
- [`heroImg`](heroimg.md)
- [`img`](img.md)

> **Note**: When an image is a child of a `lockup` element, the longest dimension of the image must be 70 points longer than the corresponding bounding box dimension.

## See Also

- [height](image-attributes-height.md)
  Specifies the maximum height for an image.
- [aspectRatio](aspectratio.md)
  Specifies the aspect ratio of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TVML/image-attributes-width)*