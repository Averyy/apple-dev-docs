# text-style

**Framework**: Professional-Video-Applications

Describes text style for a segment of text.

#### Overview

Use a `text-style` element to describe text styles to apply to the content of an element. Or use `text-style` in combination with a `text-style-def` element to define a shared text style that multiple `text-style` elements reference.

Use the `ref` attribute to reference a text-style definition. If a text-style definition is referenced, any attributes specified in this element override the values in the text-style definition.

Refer to the [Document Type Definition](./document-type-definition.md) for other attributes of the `text-style` element to specify the text style settings.

You use the `text` element to create a series of text segments in a title or caption. For each segment you can apply different text styles using the `text-style` element.

The following example XML uses text-style definitions to create a text effect:

```swift
<title offset="0s" ref="r2" name="Continuous: Title with styles, including font and size." duration="10s" start="0s">
   <text>
      <text-style ref="ts1">Title with styles, including</text-style>
      <text-style ref="ts2">font</text-style>
      <text-style ref="ts1">and</text-style>
      <text-style ref="ts3">size</text-style>
      <text-style ref="ts1">.</text-style>
   </text>
   <text-style-def id="ts1">
      <text-style font="Helvetica" fontSize="72" fontFace="Regular" fontColor="1 1 1 1" strokeColor="1 0 0 1" strokeWidth="1" alignment="center" />
   </text-style-def>
   <text-style-def id="ts2">
      <text-style font="Capitals" fontSize="72" fontFace="Regular" fontColor="1 1 1 1" bold="1" strokeColor="1 0 0 1" strokeWidth="1" alignment="center" />
   </text-style-def>
   <text-style-def id="ts3">
      <text-style font="Helvetica" fontSize="120" fontFace="Regular" fontColor="1 1 1 1" strokeColor="1 0 0 1" strokeWidth="1" alignment="center" />
   </text-style-def>
</title>
```

3D text geometry and appearance are described with one or more `param` elements as children of the `text-style` element, each specifying a respective parameter.

```swift
<text-style-def id="ts1">
   <text-style font="Helvetica" fontSize="63" fontFace="Regular" fontColor="1 0.999974 0.999991 1" alignment="center">
      <param name="Lighting" key="527">
         <param name="Environment" key="512">
            <param name="Intensity" key="514" value="0.8" />
            <param name="Rotation" key="516" value="0 247 0 0 (Use Rotation)" />
            <param name="Contrast" key="517" value="62" />
            <param name="Saturation" key="525" value="47" />
         </param>
      </param>
      <param name="Material" key="material:Basic">
         <param name="Layer" key="layer:Finish:1 (Enamel)">
            <param name="Highlight Color" key="127" value="0.838246 0.965254 0.503887" />
         </param>
         <param name="Layer" key="layer:Substance:3 (Plastic)">
            <param name="Type" key="4" value="0 (Shiny)" />
            <param name="Color" key="106" value="0.813144 0.729297 0.994205" />
         </param>
      </param>
   </text-style>
</text-style-def>
```

The following example XML represents a caption in CEA-608 format:

```swift
<caption name="CEA-608 English caption with color and underline." lane="1" offset="2225223/24000s" duration="48048/24000s" start="3600s" role="CEA-608?captionFormat=CEA608.en-US">
   <text position="4 1" display-style="pop-on" alignment="left">
      <text-style ref="ts1">CEA-608 English caption with</text-style>
      <text-style ref="ts3">color</text-style>
      <text-style ref="ts1">and</text-style>
      <text-style ref="ts4">underline</text-style>
      <text-style ref="ts1">.</text-style>
   </text>
   <text-style-def id="ts1">
      <text-style fontFace="Regular" fontColor="1 1 1 1" backgroundColor="0 0 0 1" />
   </text-style-def>
   <text-style-def id="ts3">
      <text-style fontFace="Regular" fontColor="0 0 1 1" backgroundColor="0 0 0 1" />
   </text-style-def>
   <text-style-def id="ts4">
      <text-style fontFace="Regular" fontColor="1 1 1 1" backgroundColor="0 0 0 1" underline="1" />
   </text-style-def>
</caption>
```

The following example XML represents an ITT subtitle:

```swift
<caption name="Belgian French subtitle with color and bold style." lane="1" offset="29029/300s" duration="48048/24000s" start="3600s" role="My ITT?captionFormat=ITT.fr-BE">
   <text placement="bottom">
      <text-style ref="ts5">Belgian French subtitle with</text-style>
      <text-style ref="ts6">color</text-style>
      <text-style ref="ts5">and</text-style>
      <text-style ref="ts7">bold style</text-style>
      <text-style ref="ts5">.</text-style>
   </text>
   <text-style-def id="ts5">
      <text-style fontFace="Regular" fontColor="1 1 1 1" backgroundColor="0 0 0 1" />
   </text-style-def>
   <text-style-def id="ts6">
      <text-style fontFace="Regular" fontColor="1 0.684918 0.63397 1" backgroundColor="0 0 0 1" />
   </text-style-def>
   <text-style-def id="ts7">
      <text-style fontColor="1 1 1 1" bold="1" backgroundColor="0 0 0 1" />
   </text-style-def>
</caption>
```

## Topics

### Text Style Definition
- [text-style-def](./text-style-def.md)
  Defines a set of text style attributes that can be shared with (referenced by) multiple `text-style` elements.

## See Also

### Text and Style Elements
- [text](./text.md)
  Describes a block of text that appears in a title or caption on a timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/text-style)*