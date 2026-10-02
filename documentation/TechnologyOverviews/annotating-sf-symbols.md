# Annotating custom symbols

**Framework**: Technology Overviews

Use the SF Symbols app to annotate your custom symbols and adjust the way they render and animate.

The SF Symbols app writes annotation data to your symbol’s SVG file when you export it for distribution. Most annotations apply to individual shape objects in the form of a CSS style, using class names with the prefix `<rendering mode>-<layer index>`. Multicolor has the suffix `:<color name>`, hierarchical uses `:<hierarchy level>`, and monochrome has no suffix. The following shows an abbreviated example of what these styles might look like for a symbol with three or more layers and how `<path/>` uses them:

```xml
<style>
.monochrome-0 { ... }
.monochrome-1 { ... }
.monochrome-2 { ... }

.multicolor-0:tintColor { ... }
.multicolor-1:systemBlueColor { ... }
.multicolor-2:custom { fill:#437B48; opacity:1.0; ... }

.hierarchical-0:primary { ... }
.hierarchical-1:secondary { ... }
.hierarchical-2:tertiary { ... }
</style>

<g id="Regular-S" transform="matrix(1 0 0 1 1394.89 696)">
   <path class="monochrome-0 multicolor-0:tintColor hierarchical-0:primary" d="..."/>
   <path class="monochrome-1 multicolor-1:systemBlueColor hierarchical-1:secondary" d="..."/>
   <path class="monochrome-2 multicolor-2:custom hierarchical-2:tertiary" d="..."/>
</g>
```

#### Configure Rendering Modes

To adjust your symbol’s appearance in rendering modes other than monochrome, select your symbol and enter the gallery view by choosing View > As Gallery. Open the rendering inspector by choosing View > Inspectors > Rendering Inspector, and then select the rendering mode to start annotating.

To annotate, use the individual paths that make up your symbol as your building blocks and create a set of layers for each rendering mode. SF Symbols assigns a color to layers in multicolor mode, and assigns a hierarchy group to layers in hierarchical mode. Layers have an explicit Z-order where the layers on top block the layers below them.

The center preview lets you interact with all the paths and assign them to layers. Use a path in any number of layers. In hierarchical mode, assign groups from primary to tertiary. SF Symbols uses the same data for hierarchical and palette rendering modes.

> 💡 **Tip**:  When using system-provided or fully defined asset catalog colors, your symbols adapt to changes in the system’s appearance — light, dark, and high-contrast modes — and in different vibrancy contexts.

#### Add Animations to Your Symbol

Define custom animation behaviors for the Rotate, Pulse, Draw On, and Draw Off effects. With your custom symbol selected in the gallery view, switch to the animation inspector by choosing View > Inspectors > Animation Inspector.

For animation demonstrations, see [`Human Interface Guidelines > SF Symbols > Animations`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/sf-symbols#Animations).

> **Note**:  This article doesn’t cover every animation effect, because many don’t require annotations.

#### Adjust Rotation Behavior

If a symbol doesn’t define rotation behavior by layer, the entire symbol rotates over the center point of the defined guidelines. To customize this, adjust which layers rotate, as well as the point they rotate around. Choose the Rotate animation, and in the Animate section, choose By Layer. In the Layers pane below, locate the layer that you want to rotate, click the ellipsis button, and turn on Can Rotate.

Once you define the layers that can rotate, preview the animation by clicking the play button. To adjust the rotation center, click the Scope button at the top right of the gallery view to show or hide the anchor icon.

Adjust the anchor in three ways: select a layer and Control-click it, then choose Center Rotation Anchor on Layer; drag the anchor icon into position; or double-click the anchor icon to type a position.

The `-sfsymbols-always-rotates:true` attribute in a layer’s style for each rendering mode marks that layer as Can Rotate. The following shows that the second layer rotates:

```xml
<style>
.monochrome-0 { ... }
.monochrome-1 {-sfsymbols-always-rotates:true; ... }
.monochrome-2 { ... }
</style>
```

#### Configure Which Layers Pulse

If individual layers aren’t set to pulse, the Pulse effect applies to the entire symbol. Define which layers pulse in the animation inspector. In the Layers pane, locate the layer that you want to pulse, click the ellipsis button, and turn on Can Pulse. The annotation for pulse appears as the `-sfsymbols-always-pulses:true` attribute in the layer’s style.

```xml
<style>
.monochrome-0 { ... }
.monochrome-1 {-sfsymbols-always-pulses:true; ... }
.monochrome-2 { ... }
</style>
```

#### Define Guide Points for Draw on and Draw Off

The Draw On and Draw Off effects use the same set of annotation data; defining one defines the other. The draw effect allows a symbol to appear incrementally along its defined paths. Given a simple line, annotate the symbol to draw from left to right, right to left, or start from an interior point and draw in both directions. Draw On is the inverse of Draw Off.

To annotate, select a custom symbol, and in the animation inspector, set the animation to Draw On. Next, in the Layers pane, select a layer. At the top right of the gallery, the Draw toolbar consists of three icons. The leftmost play-like triangle button enables the annotation tool to add, remove, or edit guide points. If no guide points are present, the system marks the first point you add as the starting point. When you add a second point, an arrow between the two points indicates the draw direction. On a simple path, you may only need a start and end point. Add intermediate guide points on more complex paths.

To learn more about guide points, see [`What’s new in SF Symbols 7 > Custom Symbols`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/337/?time=482).

The annotation data for guide points appears as the `data-clipstroke-keyframes` attribute on each variant’s path.

```xml
<g id="Symbols">
  <g id="Black-S" transform="matrix(1 0 0 1 2891.99 696)">
   <path class="monochrome-0 multicolor-0:tintColor hierarchical-0:primary SFSymbolsPreviewWireframe" d="..." data-clipstroke-keyframes="..."/>
   </g>
</g>
```

#### Configure Variable Color Rendering

Variable relates to both color and drawing. When a symbol provides variable color mode, it can define the order in which layers dim and become fully visible. A symbol must have multiple layers defined for variable color to work. To add these annotations, start by selecting a custom multilayer symbol and viewing it in gallery view.

Switch to the rendering inspector by choosing View > Inspectors > Rendering Inspector. In the lower-right corner of the app, click the button with three sliders to turn on Variable Rendering. Each layer in the Layers pane now has two buttons next to it. Toggling the button with an empty and filled box above a slider includes that layer for variable color. To preview how the symbol renders at different variable levels, turn on Variable (below the Rendering Mode selection) and pick Color next to the slider that appears. Drag the slider from 100% to 0% to see the effect.

The symbol dims and lightens layers in the order you arrange them in the Layers pane, at certain thresholds. For a symbol with four variable color layers, the active layer count varies by percentage as follows:

| 0% | >0% | >=26% | >=51% | >=76% |
| --- | --- | --- | --- | --- |
| None | 1 | 2 | 3 | All |

> **Note**:  When the number of layers doesn’t divide evenly, the system rounds to the nearest percentage point.

The annotation data for variable color appears as the `-sfsymbols-variable-threshold` attribute on each rendering mode’s style. This attribute includes a suffix that defines the threshold value at which the layer activates.

```xml
<style>
.monochrome-0 {-sfsymbols-variable-threshold:0.76; ... }
.monochrome-1 {-sfsymbols-variable-threshold:0.51; ... }
.monochrome-2 {-sfsymbols-variable-threshold:0.26; ... }
.monochrome-3 {-sfsymbols-variable-threshold:0.0; ... }

.multicolor-0:tintColor {-sfsymbols-variable-threshold:0.76; ... }
.multicolor-1:tintColor {-sfsymbols-variable-threshold:0.51; ... }
.multicolor-2:tintColor {-sfsymbols-variable-threshold:0.26; ... }
.multicolor-3:tintColor {-sfsymbols-variable-threshold:0.0; ... }

.hierarchical-0:secondary {-sfsymbols-variable-threshold:0.76; ... }
.hierarchical-1:secondary {-sfsymbols-variable-threshold:0.51; ... }
.hierarchical-2:secondary {-sfsymbols-variable-threshold:0.26; ... }
.hierarchical-3:primary {-sfsymbols-variable-threshold:0.0; ... }
</style>
```

#### Configure Variable Draw

When a symbol provides variable draw, it defines which layers incrementally draw. As you increase the variable value, layers incrementally draw on; as you decrease it, they draw off. To add these annotations, select a custom symbol that’s configured for Draw On and Draw Off.

After you turn on Variable Rendering for the symbol, a button with a scribble above a slider appears next to each layer. Click this button to include the layers you want in variable draw. Preview how the symbol renders by turning on Variable and picking Draw next to the slider that appears. Drag the slider to see the effect. To make adjustments to the way the layer draws, edit the guide points for the Draw On and Draw Off effect.

When multiple layers participate in variable draw, they draw in sequential order as arranged in the Layers pane. The annotation for variable draw appears as the `-sfsymbols-variable-draw` attribute. This attribute includes a suffix that defines the threshold at which the layer begins to draw and its span. In the following example, the first layer starts drawing when the variable value exceeds 0, and finishes after a span of 0.33 — so the layer finishes drawing by 0.33.

```xml
<style>
.monochrome-0 {-sfsymbols-variable-draw:0 0.33; ...}
.monochrome-1 {-sfsymbols-variable-draw:0.33 0.33; ...}
.monochrome-2 {-sfsymbols-variable-draw:0.67 0.33; ...}

.multicolor-0:tintColor {-sfsymbols-variable-draw:0 0.33; ...}
.multicolor-1:tintColor {-sfsymbols-variable-draw:0.33 0.33; ...}
.multicolor-2:tintColor {-sfsymbols-variable-draw:0.67 0.33; ...}

.hierarchical-0:primary {-sfsymbols-variable-draw:0 0.33; ...}
.hierarchical-1:primary {-sfsymbols-variable-draw:0.33 0.33; ...}
.hierarchical-2:primary {-sfsymbols-variable-draw:0.67 0.33; ...}
</style>
```

> **Note**:  A symbol can support both variable color and draw, but can’t perform both at the same time.

#### Define Animation Defaults

Define defaults for many of the animation effects used by custom symbols. By providing defaults, you don’t need to specify certain parameters in code when you use the symbol. Define defaults by clicking the button with three sliders in the lower-right corner of the app while an inspector view is visible.

These defaults appear in the `<style>` tag as follows:

```xml
<style>.defaults {-sfsymbols-wiggle-style:linear;-sfsymbols-wiggle-angle:0;-sfsymbols-rotates-clockwise:false;-sfsymbols-variable-value-mode:draw;-sfsymbols-draw-reverses-motion-groups:false}
    <!-- styles omitted -->
</style>
```

#### Distribute Your Custom Symbol

After you annotate your custom symbol and are ready to distribute it, export it for use in your app. Use File > Export Symbol to produce an SVG file with all of the annotations. The export window provides a preview and an option to change Xcode compatibility. Some annotation features may not be available in the Xcode versions not selected by default. Xcode produces build errors when using an incompatible version.

When you use File > Export Template, the exported SVG doesn’t include the annotation data. This is the option to choose when you plan to edit the symbol in your vector-drawing app. The SF Symbols app stores your symbol’s annotation data separately from the template itself. To retain the annotations, drag an edited template SVG onto the existing symbol.

> ❗ **Important**:  Annotation data requires the same number of paths across designs. To retain annotation data when modifying the paths of an annotated symbol, you can add, remove, and adjust points, but removing or reordering whole paths makes your designs go out of sync. In these cases, reannotate the symbol to account for its new path structure.

#### Use Your Custom Symbol Images

Open your app’s Xcode project and select its asset catalog. In the Xcode menu bar, select Editor > Add New Asset > Symbol Image Set, and drag your exported SVG file into the Symbol SVG section of the Symbol pane. Xcode validates the SVG file, and displays error messages if the file doesn’t fulfill the requirements. To use the symbol image in your app, follow [`Configuring and displaying symbol images in your UI`](https://developer.apple.com/documentation/uikit/configuring-and-displaying-symbol-images-in-your-ui).


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/annotating-sf-symbols)*