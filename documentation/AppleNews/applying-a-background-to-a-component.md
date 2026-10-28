# Applying a Background to a Component

**Framework**: Apple News  
**Role**: Article

Change the appearance of the backgrounds in your article.

## Overview

You can specify a background, or `fill`, that Apple News Format applies on top of a componentʼs background color. The fill can be an image, a repeatable image, a linear gradient, or a video. For each of these options, you can set properties that determine how Apple News Format displays the background and how the background behaves.

To set a background for a component, use the `fill` property in the [`ComponentStyle`](../AppleNewsFormat/componentstyle.md) object the component uses. Apple News Format lets you choose from these types of fills for your backgrounds:

- [`ImageFill`](../AppleNewsFormat/imagefill.md). Use an image as your background.
- [`RepeatableImageFill`](../AppleNewsFormat/repeatableimagefill.md). Use an image that can be repeated as your background.
- [`VideoFill`](../AppleNewsFormat/videofill.md). Use a video that starts automatically as your background.
- [`LinearGradientFill`](../AppleNewsFormat/lineargradientfill.md). Transition from one color at the top of the component to another color at the bottom. You can set the colors (and percentages) as well as the angle of the gradient fill. An angle of 90 degrees transitions from left to right instead of top to bottom.

## See Also

### Backgrounds for Components
- [object ImageFill](../AppleNewsFormat/imagefill.md)
  The object for adding an image background fill to a component.
- [object RepeatableImageFill](../AppleNewsFormat/repeatableimagefill.md)
  The object for adding a background image that Apple News can repeat.
- [object VideoFill](../AppleNewsFormat/videofill.md)
  The object for adding a video background fill to a component.
- [object LinearGradientFill](../AppleNewsFormat/lineargradientfill.md)
  The object for displaying a linear gradient as a component background.
- [object GradientFill](../AppleNewsFormat/gradientfill.md)
  The properties all gradient fill types share.
- [object Fill](../AppleNewsFormat/fill.md)
  The object for setting a fill type and attachment for a component’s background fill.
- [object ColorStop](../AppleNewsFormat/colorstop.md)
  The object for specifying the color and location for a color stop in a gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/applying-a-background-to-a-component)*