# data

**Framework**: MapKit JS  
**Kind**: property

A dictionary of custom properties to use with the URL template.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get data(): {
        [key: string]: any;
    };
set data(data: { [key: string]: any });
```

#### Discussion

The `data` object holds a dictionary of custom properties to fill the [`urlTemplate`](tileoverlay/urltemplate.md).

- If the [`urlTemplate`](tileoverlay/urltemplate.md) is a callback, MapKit JS passes the entire data object as a parameter.
- If the [`urlTemplate`](tileoverlay/urltemplate.md) is a string, `data` key names should match up with the custom placeholder names. MapKit JS ignores the keys that don’t exist in the URL template string.

The default value is `{}`.

This example shows adding a customized tile overlay to a map.

```javascript
const customOverlay = new mapkit.TileOverlay("https://{subdomain}.customtileserver.com/{z}/{x}/{y}?scale={scale}&lang={lang}&imageFormat=jpg");
customOverlay.data = {
    subdomain: "staging",
    lang: mapkit.language
};
map.addTileOverlay(customOverlay);
```

## See Also

- [urlTemplate](tileoverlay/urltemplate.md)
  A string, or callback function that returns a string, with a URL that provides the requested tile.
- [reload()](tileoverlay/reload.md)
  Reloads the tile overlay for the displayed map region with the latest data values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/tileoverlay/data)*