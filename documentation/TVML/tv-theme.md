# tv-theme

**Framework**: TVML

Sets an element’s appearance according to the specified theme.

#### Overview

Use the tv-theme query to change the appearance of a template based on the theme specified in UIUserInterfaceStyle in the info.plist or by a theme set by the theme attribute. Here’s an example that sets styles for light and dark themes.

```xml
<style>
   @media tv-template and (tv-theme:light) {
      .foo { color:rgb(0, 0, 0); }
   }
   @media tv-template and (tv-theme:dark) {
      .foo { color:rgb(255, 255, 255); }
   }
</style>
```

##### Values for Tv Theme

## See Also

- [layout-direction](layout-direction.md)
  Sets the text direction based on the user’s language preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/tv-theme)*