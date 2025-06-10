# src

**Framework**: TVML

Specifies the URL for an image.

#### Overview

The URL can point to an image on a server or to the resource scheme in your app. For a list of resource images provide by Apple, see the Resource Icons section of [`TVML`](TVML.md). Here’s an example that displays the United States general admission movie rating icon.

```xml
<img src="resource://mpaa-g" />
```

> **Note**: When this attribute loads an image using an HTTP URL, you must add `height` and `width` attributes to the element.

##### Values for Src

##### Elements That Use Src

- [`badge`](badge.md)
- [`decorationImage`](decorationimage.md)
- [`fullscreenImg`](fullscreenimg.md)
- [`heroImg`](heroimg.md)
- [`img`](img.md)

## See Also

- [srcset](srcset.md)
  Specifies multiple URLs for an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/src)*