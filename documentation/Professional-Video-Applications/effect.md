# effect

**Framework**: Professional-Video-Applications

Reference visual, audio, or custom effects.

#### Overview

Use the `effect` element to reference an effect that can be a Motion template, a FxPlug, an Audio Unit, or an audio effect bundle. Use a `filter-video`, `filter-video-mask`, or `filter-audio` element to apply the effect to a story element.

##### Attributes of effect Element

| Attribute | Description |
| --- | --- |
| `uid` | A string that identifies the effect.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For a Motion template, it’s a relative path under the location where Final Cut Pro manages the templates. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For an FxPlug, it’s a unique identifier you assign to the FxPlug.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For an Audio Units (AU), it’s a unique identifier of the Audio Units.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For an audio effect bundle, it’s the name of the bundle. |
| `src` | For an effect that is a customized Motion template, it’s a URL that points to the file. |

## Topics

### Resource Element Attributes
- [id](./id.md)
  Specifies a local identifier to use within the FCPXML document.
- [name](./name.md)
  Specifies the name of the resource.

## See Also

### Shared Resources and Reference Elements
- [asset](./asset.md)
  Define file-based media managed in a Final Cut Pro library.
- [media](./media.md)
  Describe a compound clip or a multi-camera media definition.
- [format](./format.md)
  Reference a video-format definition.
- [locator](./locator.md)
  Describe a URL-based resource.
- [object-tracker](./object-tracker.md)
  Describe a tracked object such as a face or other moving object in a video clip.
- [tracking-shape](./tracking-shape.md)
  Define a shape that the object-tracker uses to match the movement of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/effect)*