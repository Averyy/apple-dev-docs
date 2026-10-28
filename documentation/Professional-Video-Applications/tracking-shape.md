# tracking-shape

**Framework**: Professional-Video-Applications  
**Role**: Article

Define a shape that the object-tracker uses to match the movement of an object.

## Overview

In Final Cut Pro, users can track the shape-mask of a video effect such as a blur, highlight, or color effect to a moving object in a video clip.

Use the `tracking-shape` element to define the shape that the [object-tracker](./object-tracker.md) element uses to match the movement of a moving object in a video clip. Each object-tracker element consists of one or more tracking shapes.

### Tracking-Shape Elements Attributes

- **`id`**: Specifies a local identifier to use within the FCPXML document.
- **`name`**: Specifies the name of the shape.
- **`offsetEnabled`**: Enables the offset of an effect, graphic, or title from the face or other object that Final Cut Pro tracks.
- **`analysisMethod`**: Specifies the method that Final Cut Pro uses to analyze the motion of a face or other object.
- **`dataLocator`**: References a locator resource that Final Cut Pro uses to store the shape’s analysis data.

For information about the locator element and how Final Cut Pro uses it to describe a resource and location using a URL, see the [locator](./locator.md) element.

## See Also

### Shared Resources and Reference Elements
- [asset](./asset.md)
  Define file-based media managed in a Final Cut Pro library.
- [media](./media.md)
  Describe a compound clip or a multi-camera media definition.
- [format](./format.md)
  Reference a video-format definition.
- [effect](./effect.md)
  Reference visual, audio, or custom effects.
- [locator](./locator.md)
  Describe a URL-based resource.
- [object-tracker](./object-tracker.md)
  Describe a tracked object such as a face or other moving object in a video clip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/tracking-shape)*