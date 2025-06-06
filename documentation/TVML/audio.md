# audio

**Framework**: TVML

Plays background audio for a full-page template when the template is the top-most document in the navigation stack.

#### Overview

Each document page that plays audio in the background must have its own `audio` element. If the same URL is used between pages, audio will continue to play when the new page is displayed. The `audio` element only supports unencrypted audio.

```xml
<audio>
    <asset />
</audio>
```

##### Subelements of Audio

- [`asset`](asset.md)

##### Elements That Use Audio

- [`background`](background.md)

## Topics

### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [background](background.md)
  Displays an image or plays audio in the background of a channel app page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/audio)*