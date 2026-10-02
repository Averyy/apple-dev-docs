# Creating custom symbols

**Framework**: Technology Overviews

Design a symbol image with the same behavior as system-provided symbols.

SF Symbols offers a comprehensive set of consistent, highly configurable symbol images that you can use in your app. You can apply stylistic traits typically associated with text, such as color, text style, weight, and scale. Symbols contain additional traits that allow them to integrate seamlessly with surrounding text, and adapt to platform features like Dynamic Type and Dark Mode.

Export an SVG file from the [`SF Symbols`](https://developer.apple.comhttps://developer.apple.com/sf-symbols/) app, edit it in a vector-drawing app, and export it again as an SVG file. Validate the file by importing it into SF Symbols. If needed, add annotations to support rendering modes or animations, then export the symbol file for distribution.

Base your symbol on an existing symbol in the SF Symbols app. For example, the circle symbol is a great reference point for an initial design.

For design guidance, see [`Human Interface Guidelines > SF Symbols`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/sf-symbols/).

#### Export a Custom Symbol Template File

After you locate a symbol image to use as a base for your design, choose File > Duplicate as Custom Symbol. The app creates a new category at the bottom of the categories sidebar where you find your custom symbols. To create an SVG file for your custom symbol, export a symbol template file for design customization by selecting the symbol and choosing File > Export Template.

Choose between static or variable when exporting a template. Use a static setup if you’re targeting a particular weight and scale, or only plan to design one or two variants of your symbol. The setup contains 27 sets of paths and one set of explicit margins. A variable template setup contains three sets of paths and three sets of margins. If you plan on supporting all design variants, this gives you the minimum number of variants necessary for the system to generate the other 24.

> **Note**:  By using three sources — `Ultralight-S`, `Regular-S`, and `Black-S` — SF Symbols can dynamically generate the full range of weights and scales you don’t specify through vector interpolation.

After you export a template file, you use a vector-drawing app, such as Adobe Illustrator or Sketch, to begin modifying it.

#### Manage Symbol Image Variants

The Symbols layer contains up to 27 sublayers, each representing a symbol image variant. Identifiers of symbol variants have the form `<weight>-<{S, M, L}>`, where `weight` corresponds to a weight of the San Francisco system font and `S`, `M`, or `L` matches the small, medium, or large symbol scale.

```xml
<g id="Symbols">
    <g id="Regular-M" transform="matrix(1 0 0 1 2855.62 1556)">
        <!-- Path and style details for the Regular-M image variant. -->
    </g>
</g>
```

SF Symbols treats a symbol as path-based, rather than stroke-based, if all the shapes within it have solid color fills, and don’t have strokes or other graphical features. Interpolation allows the system to generate variants between compatible paths. A template is interpolatable when:

- It contains the interpolation sources `Ultralight-S`, `Regular-S`, and `Black-S`.
- The three interpolation sources are path-based.
- The three interpolation sources contain the same number of paths and the same number of control points.

A template doesn’t need to contain all 27 variants. You can add as many variants to your template as you want, and if they’re present, the system uses them instead of interpolation. You can delete the variants you don’t need, so you can produce as many weights and scales as your app requires.

#### Organize the Guides Layer

The system uses guides to align your custom symbol image with surrounding text. For example, it uses the provided baseline and cap height information for each of the three font scales to compute the symbol image’s baseline offset and cap height.

The Guides layer contains an uppercase letter *A* in outline form for each scale in the San Francisco system font as a reference glyph. Use the reference glyphs in the template as guides for how a symbol image looks next to text.

Each image variant of a symbol can have its own margin guides. This allows the margins to vary slightly by weight and scale instead of using a fixed margin for all variants. The explicit margin guides have the form `left-margin-<variant-specifier>` or `right-margin-<variant-specifier>`. The following example represents the left and right guides of the `Regular-S` symbol variant:

```xml
<g id="Guides">
    <line id="left-margin-Regular-S" style="fill:none;stroke:#00AEEF;stroke-width:0.5;opacity:1.0;" x1="1403.33" x2="1403.33" y1="600.784" y2="720.121"/>
    <line id="right-margin-Regular-S" style="fill:none;stroke:#00AEEF;stroke-width:0.5;opacity:1.0;" x1="1496.36" x2="1496.36" y1="600.784" y2="720.121"/>
</g>
```

Symbols can contain negative margins to aid with horizontal alignment. If you don’t specify explicit margin guides, the system uses the next available margins it finds — interpolated margins (if the template is interpolatable), `Regular-M`, `Regular-S`, and, finally, any available margins the system can use.

#### Create Your Custom Symbol Image

Start creating your custom symbol image by modifying the symbol in the template file you export. If you export a variable template, modify all three symbol configurations so the system can generate the other variants.

When you finish your base variant, copy the existing drawing to the desired layer and adjust from there. This helps you keep the same number of paths across your design variants, which is a requirement if you want to produce a symbol with multicolor or hierarchical data.

Use the following scale factors when designing your variants:

|  | `<weight>-S` | `<weight>-M` | `<weight>-L` |
| --- | --- | --- | --- |
| Scale factor | 0.783 | 1.0 | 1.29 |

The system automatically centers symbols vertically to San Francisco’s cap height in all the different scales and weights. Position your custom symbol using the specified guides to make sure it appears correctly in text. When the symbol image appears in text, the system positions it vertically so that the bottom edge of the symbol image is the same distance, scaled by point size, that the symbol image is from the baseline guide in the template file.

> ❗ **Important**:  SF Symbols picks up all paths in a variant’s layer — including invisible paths — as part of the symbol outlines. This may lead to unexpected results when working with layers in the SF Symbols app, so don’t use hidden paths.

When you create a symbol, you work on the monochrome representation. To ensure that your symbol supports rendering modes other than monochrome:

- Convert any strokes to paths so the resulting shapes can take on colors or hierarchy groups. Paths make it easier to make minor optical adjustments when a stroke isn’t precise enough.
- Use standard flat color fills with no additional effects such as drop shadows. If these are present, they override any multicolor or hierarchical data you create for your symbol.
- Check that all shapes in your design have a defined fill area with start and end points that connect.

Image variants adapt automatically according to a person’s device language, including right-to-left writing systems. If you’re designing for left-to-right and right-to-left writing systems, consider the directionality and overall look of both localized variants. Some symbols don’t have the intended look when you mirror them. For design guidance, see [`Human Interface Guidelines > Right to left`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/right-to-left/).

#### Preserve Annotations and Meta Information in the Notes Layer

The Notes layer contains optional annotations and meta information about the template file that can help you understand its contents. The `template-version` layer contains a required version string that indicates the template format version, so don’t remove it, or SF Symbols can’t read the file. The `artboard` layer makes sure design tools display the template with a convenient canvas size and legible symbols.

> **Note**:  You don’t need to modify the contents of the Notes layer. Lock the `artboard` layer in your vector-drawing app before making any modifications to the file to avoid accidentally moving the artboard layer.

#### Export Your Custom Symbol and Preserve All Names

When you finish designing your symbol, export it from your vector-drawing app as an SVG file with maximum precision. Some vector-drawing apps export SVGs at low precision by default, so export your SVG by changing the default decimal place value to 7 or greater. Confirm that the SVG file preserves all of the identifiers for your symbol variants and guides.

Use any of the following methods to validate that your SVG file conforms to the requirements of SF Symbols:

- Use the SF Symbols app and choose File > Validate Templates.
- Add it to an asset catalog in your Xcode project. Xcode verifies the SVG file and displays error messages if it doesn’t conform to the requirements.
- Inspect the SVG file to manually review the XML source code. Understanding the template layout helps you debug validation issues, so keep the original template you import into your vector-drawing app for a reference to compare against.

When you have a valid template file, you’re ready to begin annotating it. Import your symbol back into the SF Symbols app by dropping it onto your custom symbol. For more information about annotating your symbol, see [`Annotating custom symbols`](annotating-sf-symbols.md).

## See Also

- [Annotating custom symbols](annotating-sf-symbols.md)
  Use the SF Symbols app to annotate your custom symbols and adjust the way they render and animate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/custom-sf-symbols)*