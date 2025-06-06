# Adding Resource Icons

**Framework**: TVML

Add Apple-provided icons to buttons and as independent images.

#### Overview

Apple TV contains several icons that are available when you set the `src` attribute on a `badge` element to `resource://<resourcename>`. Here’s an example that sets the preview icon on a button:

```xml
<buttonLockup>
    <badge src="resource://button-preview" />
    <title>Preview</title>
</buttonLockup>
```

Resource icons do not have different variants for dark and light themes. Use the `tv-tint-color` style to change the color of black and white resource icons. Select the appropriate tint for dark and light themes by wrapping the `tv-tint-color` style inside of a media query.

## See Also

- [Button Icons](button-icons.md)
  Icons that indicate the function of a button.
- [Movie Rating Icons (United States)](movie-rating-icons-united-states.md)
  Icons that pertain to United States movie ratings.
- [Television Rating Icons (United States)](television-rating-icons-united-states.md)
  Icons that pertain to United States television ratings.
- [Rating Icons (New Zealand)](rating-icons-new-zealand.md)
  Icons that pertain to New Zealand movie ratings.
- [Rating Icons (United Kingdom)](rating-icons-united-kingdom.md)
  Icons that pertain to United Kingdom movie ratings.
- [Rating Icons (Brazil)](rating-icons-brazil.md)
  Icons that pertain to Brazil movie ratings.
- [Rotten Tomatoes Rating Icons](rotten-tomatoes-rating-icons.md)
  Icons pertaining to the Rotten Tomatoes rating system.
- [Miscellaneous Icons](miscellaneous-icons.md)
  Miscellaneous icons that don’t fall into a specific category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/adding-resource-icons)*