# Specifying Measurements for Components

**Framework**: Apple News

Specify the units of measure to use for margins, minimum heights, and other dimensions.

#### Overview

In Apple News Format, you can use variable sizing for component margins, minimum component height, and other measurements. Sizes can be a percentage of the width or height of the viewport, the document margins and gutters, or the component’s height (the part of the document visible to the user).

> **Note**:  By default, values are set in points (pt). You can set the points value as a number, or as a string that includes the `pt` abbreviation.

 By default, values are set in points (pt). You can set the points value as a number, or as a string that includes the `pt` abbreviation.

This example sets the margin to 10 points, as a string value.

```json
"margin": {
  "top": "10pt"
}
```

This example also sets the margin to 10 points, because an integer is specified and the default unit is points.

```json
"margin": {
  "top": 10
}
```

##### Set Component Measurements Based on the Viewport

You can set the size of a margin or the minimum height for a component based on a percentage of the width or height of the viewport. The viewport includes the portion of the screen that is sometimes covered by the toolbar.

###### Set Measurements Based on Viewport Height

This example results in a component height of at least 50 percent of the viewport height (vh).

```json
"minimumHeight": "50vh"
```

###### Set Measurements Based on Viewport Width

In this example, the component’s margin is set to 20 percent of the viewport width (vw).

```json
"margin": {
  "bottom": "20vw"
}
```

###### Set Measurements Based on the Viewports Shortest Side

If you base a component’s minimum height on the shortest side of the viewport, remember that the minimum height varies depending on your device orientation. If your article is being viewed in portrait orientation, the calculation is based on the width of the viewport; in landscape, the calculation is based on the height of the viewport.

For example, if the viewport is narrow and tall (portrait), a value of `150vmin` is calculated as 150 percent of the width. This example sets the component’s minimum height to 25 percent of the shortest side of the viewport.

```json
"minimumHeight": "25vmin"
```

###### Set Measurements Based on the Viewports Longest Side

If you base a component’s minimum height on the longest side of the viewport, remember that the minimum height varies depending on your device orientation. If your article is being viewed in portrait orientation, the calculation is based on the height of the viewport; in landscape, the calculation is based on the width of the viewport.

For example, if the viewport is narrow and tall (portrait), a value of `150vmax` is calculated as 150 percent of the height. The following example sets the component’s minimum height to 25 percent of the longest side of the viewport.

```json
"minimumHeight": "25vmax"
```

##### Set Component Height Based on Component Width

Use the component width (`cw`) unit to set a component’s height as a percentage of the component’s width, which guarantees a specific aspect ratio. This example calculates the value.

```json
height ÷ width * 100 
```

For example, for a landscape image with a 9:16 aspect ratio, you calculate `9 ÷ 16 * 100`, for a value of `56.25cw`. This example sets the component’s height to 50 percent of its width.

```json
"minimumHeight": "50cw"
```

##### Set Component Width Based on Parent Component Width

Use the parent width (`pw`) unit to set `minimumWidth` or `maximumWidth` in relation to the width of the parent component. If you use the `pw` unit on a top-level component inside a document that doesn’t have a parent, Apple News Format uses the viewport width (`vw`).

```json
"minimumWidth": "30pw", "maximumWidth": "50pw"
```

##### Set Component Margins Based on Gutter Size

Use the `gut` unit to base a component’s margin on the column gutter size. This example sets the component’s margin to the full width of the gutter.

```json
"margin": {
  "bottom": "100gut"
}
```

Use the `dg` unit to base a component’s margin on the column gutter size. This example sets the component’s margin to the full width of the gutter.

```json
"margin": {
  "bottom": "100dg"
}
```

This example sets the component’s margin to half the width of the gutter.

```json
"margin": {
  "bottom": "50dg"
}
```

##### Set Vertical Margins for a Component

The `margin` property in the `layout` object provides the spacing for the outer left and right sides of the document and can change depending on the device size. To apply that same spacing vertically, use the `dm` unit in the `margin` property in the component layout object.

This example creates a vertical margin between components that’s 100 percent of the left margin of the document.

```json
"margin": "100dm"
```

This example creates a vertical margin that’s 50 percent of the left margin of the document.

```json
"margin": "50dm"
```

> **Note**:  A value such as `100dm` in versions of iOS earlier than iOS 11 is interpreted as a left-right margin of 100 points.

 A value such as `100dm` in versions of iOS earlier than iOS 11 is interpreted as a left-right margin of 100 points.

## See Also

- [Creating a Layered Header](creating-a-layered-header.md)
  Create a header with a caption that’s layered in front of an image.
- [Adding a Fixed Image Fill](adding-a-fixed-image-fill.md)
  Add an image that remains stationary when the user scrolls.
- [type SupportedUnits](../applenewsformat/supportedunits.md)
  The units of measurement Apple News Format supports.
- [Preparing Image, Video, Audio, Music, and ARKit Assets](preparing-image-video-audio-music-and-arkit-assets.md)
  Add media assets to your article.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/specifying-measurements-for-components)*