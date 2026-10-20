# background

**Framework**: TVML

Displays an image or plays audio in the background of a channel app page.

#### Overview

Here’s an example that shows adding an image and audio to a `background` element.

```xml
<background>
   <img src="" />
   <audio>
      <asset id="" src="" keyDelivery="" />
   </audio>
</background>
```

> **Note**: Audio does not work in the background when the `background` element is contained in a `banner` element.

##### Subelements of background

- [audio](./audio.md)
- [mediaContent](./mediacontent.md)

##### Elements that Use background

- [alertTemplate](./alerttemplate.md)
- [banner](./banner.md)
- [compilationTemplate](./compilationtemplate.md)
- [descriptiveAlertTemplate](./descriptivealerttemplate.md)
- [listTemplate](./listtemplate.md)
- [mainTemplate](./maintemplate.md)
- [organizer](./organizer.md)
- [productBundleTemplate](./productbundletemplate.md)
- [productTemplate](./producttemplate.md)
- [showcaseTemplate](./showcasetemplate.md)

## Topics

### Valid TVML Styles
- [background-color](./background-color.md)
  Changes the background color of an element.
- [color](./color.md)
  Changes the color of an element.
### Valid TVML Attributes
- [aspectFill](./aspectfill.md)
  Stretches an image to fill the containing bounding box.

## See Also

### Background Elements
- [audio](./audio.md)
  Plays background audio for a full-page template when the template is the top-most document in the navigation stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/background)*