# SupportedUnits

**Framework**: AppleNewsFormat  
**Kind**: typealias  
**Role**: Type

The units of measurement Apple News Format supports.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
string SupportedUnits
```

## Discussion

You can define units for setting dimensions in Apple News Format. If you don’t define the units to use, Apple News Format interprets the dimensions in points (`pt`).

The following are the supported units in Apple News Format:

- `vw`. Defines a size or margin based on the viewport width.
- `vh`. Defines a size or margin based on the viewport height.
- `vmin`. Defines a size or margin based on the shortest side of the viewport (height or width, whichever is shorter).
- `vmax`. Defines a size or margin based on the longest side of the viewport (height or width, whichever is longer).
- `dg`. Defines a size or margin based on the document gutter. See [`Layout`](./layout.md).
- `dm`. Defines a size or margin based on the document margin. See [`Layout`](./layout.md).
- `cw`. Defines a size based on the component’s width. Note that you can only use this unit for sizing the component itself.
- `pw`. Defines the component width based on the parent component width.
- `pt`. Defines a unit of measure in points (the default).

For more information, see [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

## See Also

### Component Measurements and Media Guidelines
- [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md)
  Specify the units of measure to use for margins, minimum heights, and other dimensions.
- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)
  Add media assets to your article.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/supportedunits)*