---
url: https://developer.apple.com/design/human-interface-guidelines/icons
framework: HIG
---

# Icons

**Type:** article

**Platforms:** ios, ipados, macos, tvos, visionos, watchos

> **Updated 2025-06-09:** Added a table of SF Symbols that represent common actions.

An effective icon is a graphic asset that expresses a single concept in ways people instantly understand.

![A sketch of the Command key icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](/images/com.apple.HIG/foundations-icons-intro~dark@2x.png)
Apps and games use a variety of simple icons to help people understand the items, actions, and modes they can choose. Unlike [App icons](app-icons.md), which can use rich visual details like shading, texturing, and highlighting to evoke the app’s personality, an *interface icon* typically uses streamlined shapes and touches of color to communicate a straightforward idea.
You can design interface icons — also called *glyphs* — or you can choose symbols from the SF Symbols app, using them as-is or customizing them to suit your needs. Both interface icons and symbols use black and clear colors to define their shapes; the system can apply other colors to the black areas in each image. For guidance, see [SF Symbols](sf-symbols.md).

## Best practices
**Create a recognizable, highly simplified design.** Too many details can make an interface icon confusing or unreadable. Strive for a simple, universal design that most people will recognize quickly. In general, icons work best when they use familiar visual metaphors that are directly related to the actions they initiate or content they represent.
**Maintain visual consistency across all interface icons in your app.** Whether you use only custom icons or mix custom and system-provided ones, all interface icons in your app need to use a consistent size, level of detail, stroke thickness (or weight), and perspective. Depending on the visual weight of an icon, you may need to adjust its dimensions to ensure that it appears visually consistent with other icons.
![Diagram of four glyphs in a row. From the left, the glyphs are a camera, a heart, an envelope, and an alarm clock. Two horizontal dashed lines show the bottom and top boundaries of the row and a horizontal red line shows the midpoint. All four glyphs are solid black; some include interior detail lines in white. Parts of the alarm clock extend above the top dashed line because its lighter visual weight requires greater height to achieve balance with the other glyphs.](/images/com.apple.HIG/custom-icon-sizes~dark@2x.png)
![Diagram of the same four glyphs shown above and the same horizontal dashed lines at top and bottom and horizontal red line through the middle. In this diagram, all four glyphs are solid gray; the interior detail lines are black to emphasize that all lines use the same weight.](/images/com.apple.HIG/custom-icon-line-weights~dark@2x.png)
**In general, match the weights of interface icons and adjacent text.** Unless you want to emphasize either the icons or the text, using the same weight for both gives your content a consistent appearance and level of emphasis.
**If necessary, add padding to a custom interface icon to achieve optical alignment.** Some icons — especially asymmetric ones — can look unbalanced when you center them geometrically instead of optically. For example, the download icon shown below has more visual weight on the bottom than on the top, which can make it look too low if it’s geometrically centered.
![Two images of a white arrow that points down to a white horizontal line segment within a black disk. The image on the right includes two horizontal pink bars — one between the top of the glyph and the top of the disk and the other between the bottom of the glyph and the bottom of the disk — that show the glyph is geometrically centered within the disk.](/images/com.apple.HIG/asymmetric-glyph~dark@2x.png)
In such cases, you can slightly adjust the position of the icon until it’s optically centered. When you create an asset that includes your adjustments as padding around an interface icon (as shown below on the right), you can optically center the icon by geometrically centering the asset.
![Two images of a white arrow that points down to a white horizontal line segment within a black disk. The image on the left includes the two horizontal pink bars in the same locations as in the previous illustration, but the glyph has been moved up by a few pixels. The image on the right includes a pink rectangle overlaid on top of the glyph to represent a padding area, which includes the extra pixels below the glyph.](/images/com.apple.HIG/asymmetric-glyph-optically-centered~dark@2x.png)
Adjustments for optical centering are typically very small, but they can have a big impact on your app’s appearance.
![Two images of a white arrow that points down to a white horizontal line segment within a black disk. The glyph on the left is geometrically centered and the one on the right is optically centered.](/images/com.apple.HIG/asymmetric-glyph-before-and-after~dark@2x.png)
**Provide a selected-state version of an interface icon only if necessary.** You don’t need to provide selected and unselected appearances for an icon that’s used in standard system components such as toolbars, tab bars, and buttons. The system updates the visual appearance of the selected state automatically.
![An image of two toolbar buttons that share a background. The left button shows the Filter icon in a selected state, using a blue tint color for its background. The right button shows the More icon in an unselected state, using the default appearance for toolbar buttons.](/images/com.apple.HIG/icons-selection-correct~dark@2x.png)
**Use inclusive images.** Consider how your icons can be understandable and welcoming to everyone. Prefer depicting gender-neutral human figures and avoid images that might be hard to recognize across different cultures or languages. For guidance, see [Inclusion](inclusion.md).
**Include text in your design only when it’s essential for conveying meaning.** For example, using a character in an interface icon that represents text formatting can be the most direct way to communicate the concept. If you need to display individual characters in your icon, be sure to localize them. If you need to suggest a passage of text, design an abstract representation of it, and include a flipped version of the icon to use when the context is right-to-left. For guidance, see [Right to left](right-to-left.md).
![A partial screenshot of the SF Symbols app showing the info panel for the character symbol, which looks like the capital letter A. Below the image, the following eight localized versions of the symbol are listed: Latin, Arabic, Hebrew, Hindi, Japanese, Korean, Thai, and Chinese.](/images/com.apple.HIG/character-in-glyph~dark@2x.png)
![A partial screenshot of the SF Symbols app showing the info panel for the text dot page symbol, which looks like three left-aligned horizontal lines inside a rounded rectangle. Below the image, the left-to-right and right-to-left localized versions are shown.](/images/com.apple.HIG/abstract-text-in-glyph~dark@2x.png)
**If you create a custom interface icon, use a vector format like PDF or SVG.** The system automatically scales a vector-based interface icon for high-resolution displays, so you don’t need to provide high-resolution versions of it. In contrast, PNG — used for app icons and other images that include effects like shading, textures, and highlighting — doesn’t support scaling, so you have to supply multiple versions for each PNG-based interface icon. Alternatively, you can create a custom SF Symbol and specify a scale that ensures the symbol’s emphasis matches adjacent text. For guidance, see [SF Symbols](sf-symbols.md).
**Provide alternative text labels for custom interface icons.** Alternative text labels — or accessibility descriptions — aren’t visible, but they let VoiceOver audibly describe what’s onscreen, simplifying navigation for people with visual disabilities. For guidance, see [VoiceOver](voiceover.md).
**Avoid using replicas of Apple hardware products.** Hardware designs tend to change frequently and can make your interface icons and other content appear dated. If you must display Apple hardware, use only the images available in [Apple Design Resources](https://developer.apple.com/design/resources/) or the SF Symbols that represent various Apple products.

## Standard icons
For icons to represent common actions in [Menus](menus.md), [Toolbars](toolbars.md), [Buttons](buttons.md), and other places in interfaces across Apple platforms, you can use these [SF Symbols](sf-symbols.md).

### Editing
| Action | Icon | Symbol name |
| --- | --- | --- |
| Cut | ![An icon showing a pair of scissors.](/images/com.apple.HIG/icons-symbols-meaning-cut~dark@2x.png) | `scissors` |
| Copy | ![An icon showing two copies of a document.](/images/com.apple.HIG/icons-symbols-meaning-copy~dark@2x.png) | `document.on.document` |
| Paste | ![An icon showing a document in front of a clipboard.](/images/com.apple.HIG/icons-symbols-meaning-paste~dark@2x.png) | `document.on.clipboard` |
| Done | ![An icon showing a checkmark.](/images/com.apple.HIG/icons-symbols-meaning-done-save~dark@2x.png) | `checkmark ` |
| Save |  |  |
| Cancel | ![An icon showing an X.](/images/com.apple.HIG/icons-symbols-meaning-close-cancel~dark@2x.png) | `xmark` |
| Close |  |  |
| Delete | ![An icon showing a trash can.](/images/com.apple.HIG/icons-symbols-meaning-delete~dark@2x.png) | `trash` |
| Undo | ![An icon showing an arrow curving toward the top left.](/images/com.apple.HIG/icons-symbols-meaning-undo~dark@2x.png) | `arrow.uturn.backward` |
| Redo | ![An icon showing an arrow curving toward the top right.](/images/com.apple.HIG/icons-symbols-meaning-redo~dark@2x.png) | `arrow.uturn.forward` |
| Compose | ![An icon showing a pencil positioned over a square.](/images/com.apple.HIG/icons-symbols-meaning-compose~dark@2x.png) | `square.and.pencil` |
| Duplicate | ![An icon showing a square with a plus sign on top of another square.](/images/com.apple.HIG/icons-symbols-meaning-duplicate~dark@2x.png) | `plus.square.on.square` |
| Rename | ![An icon showing a pencil.](/images/com.apple.HIG/icons-symbols-meaning-rename~dark@2x.png) | `pencil` |
| Move to | ![An icon showing a folder.](/images/com.apple.HIG/icons-symbols-meaning-move-to-folder~dark@2x.png) | `folder` |
| Folder |  |  |
| Attach | ![An icon showing a paperclip.](/images/com.apple.HIG/icons-symbols-meaning-attach~dark@2x.png) | `paperclip` |
| Add | ![An icon showing a plus sign.](/images/com.apple.HIG/icons-symbols-meaning-add~dark@2x.png) | `plus` |
| More | ![An icon showing an ellipsis.](/images/com.apple.HIG/icons-symbols-meaning-more~dark@2x.png) | `ellipsis` |


### Selection
| Action | Icon | Symbol name |
| --- | --- | --- |
| Select | ![An icon showing a checkmark in a circle.](/images/com.apple.HIG/icons-symbols-meaning-select-all~dark@2x.png) | `checkmark.circle` |
| Deselect | ![An icon showing an X.](/images/com.apple.HIG/icons-symbols-meaning-deselect-close~dark@2x.png) | `xmark` |
| Close |  |  |
| Delete | ![An icon showing a trash can.](/images/com.apple.HIG/icons-symbols-meaning-delete~dark@2x.png) | `trash` |


### Text formatting
| Action | Icon | Symbol name |
| --- | --- | --- |
| Superscript | ![An icon showing the capital letter A with the number 1 in the upper right corner.](/images/com.apple.HIG/icons-symbols-meaning-superscript~dark@2x.png) | `textformat.superscript` |
| Subscript | ![An icon showing the capital letter A with the number 1 in the lower right corner.](/images/com.apple.HIG/icons-symbols-meaning-subscript~dark@2x.png) | `textformat.subscript` |
| Bold | ![An icon showing the capital letter B in bold.](/images/com.apple.HIG/icons-symbols-meaning-bold~dark@2x.png) | `bold` |
| Italic | ![An icon showing the capital letter I in italics.](/images/com.apple.HIG/icons-symbols-meaning-italic~dark@2x.png) | `italic` |
| Underline | ![An icon showing the capital letter U with an underline.](/images/com.apple.HIG/icons-symbols-meaning-underline~dark@2x.png) | `underline` |
| ​​Align Left | ![An icon showing a stack of four horizontal lines of varying widths that align at the left edge.](/images/com.apple.HIG/icons-symbols-meaning-align-left~dark@2x.png) | `text.alignleft` |
| Center | ![An icon showing a stack of four horizontal lines of varying widths that align in the center.](/images/com.apple.HIG/icons-symbols-meaning-align-center~dark@2x.png) | `text.aligncenter` |
| Justified | ![An icon showing a stack of four horizontal lines of identical widths.](/images/com.apple.HIG/icons-symbols-meaning-align-justified~dark@2x.png) | `text.justify` |
| Align Right | ![An icon showing a stack of four horizontal lines of varying widths that align at the right edge.](/images/com.apple.HIG/icons-symbols-meaning-align-right~dark@2x.png) | `text.alignright` |


### Search
| Action | Icon | Symbol name |
| --- | --- | --- |
| Search | ![An icon showing a magnifying glass.](/images/com.apple.HIG/icons-symbols-meaning-search~dark@2x.png) | `magnifyingglass` |
| Find | ![An icon showing a magnifying glass above a document.](/images/com.apple.HIG/icons-symbols-meaning-find~dark@2x.png) | `text.page.badge.magnifyingglass` |
| Find and Replace |  |  |
| Find Next |  |  |
| Find Previous |  |  |
| Use Selection for Find |  |  |
| Filter | ![An icon showing a stack of three horizontal lines decreasing in width from top to bottom.](/images/com.apple.HIG/icons-symbols-meaning-filter~dark@2x.png) | `line.3.horizontal.decrease` |


### Sharing and exporting
| Action | Icon | Symbol name |
| --- | --- | --- |
| Share | ![An icon showing an arrow pointing up from the middle of square.](/images/com.apple.HIG/icons-symbols-meaning-sharing~dark@2x.png) | `square.and.arrow.up` |
| Export |  |  |
| Print | ![An icon showing a printer.](/images/com.apple.HIG/icons-symbols-meaning-print~dark@2x.png) | `printer` |


### Users and accounts
| Action | Icon | Symbol name |
| --- | --- | --- |
| Account | ![An icon showing an abstract representation of a person’s head and shoulders in a circular outline.](/images/com.apple.HIG/icons-symbols-meaning-account-user~dark@2x.png) | `person.crop.circle` |
| User |  |  |
| Profile |  |  |


### Ratings
| Action | Icon | Symbol name |
| --- | --- | --- |
| Dislike | ![An icon showing a hand giving a thumbs down gesture.](/images/com.apple.HIG/icons-symbols-meaning-dislike~dark@2x.png) | `hand.thumbsdown` |
| Like | ![An icon showing a hand giving a thumbs up gesture.](/images/com.apple.HIG/icons-symbols-meaning-like~dark@2x.png) | `hand.thumbsup` |


### Layer ordering
| Action | Icon | Symbol name |
| --- | --- | --- |
| Bring to Front | ![An icon showing a stack of three squares overlapping each other, with the top square using a solid fill style while the other squares are outlines.](/images/com.apple.HIG/icons-symbols-meaning-bring-to-front~dark@2x.png) | `square.3.layers.3d.top.filled` |
| Send to Back | ![An icon showing a stack of three squares overlapping each other, with the bottom square using a solid fill style while the other squares are outlines.](/images/com.apple.HIG/icons-symbols-meaning-send-to-back~dark@2x.png) | `square.3.layers.3d.bottom.filled` |
| Bring Forward | ![An icon showing a stack of two squares overlapping each other, with the top square using a solid fill style while the other square is an outline.](/images/com.apple.HIG/icons-symbols-meaning-bring-forward~dark@2x.png) | `square.2.layers.3d.top.filled` |
| Send Backward | ![An icon showing a stack of two squares overlapping each other, with the bottom square using a solid fill style while the other square is an outline.](/images/com.apple.HIG/icons-symbols-meaning-send-backwards~dark@2x.png) | `square.2.layers.3d.bottom.filled` |


### Other
| Action | Icon | Symbol name |
| --- | --- | --- |
| Alarm | ![An icon showing an alarm clock.](/images/com.apple.HIG/icons-symbols-meaning-alarm~dark@2x.png) | `alarm` |
| Archive | ![An icon showing a file box.](/images/com.apple.HIG/icons-symbols-meaning-archive~dark@2x.png) | `archivebox` |
| Calendar | ![An icon showing a calendar.](/images/com.apple.HIG/icons-symbols-meaning-calendar~dark@2x.png) | `calendar` |


## Platform considerations
*No additional considerations for iOS, iPadOS, tvOS, visionOS, or watchOS.*

### macOS

#### Document icons
If your macOS app can use a custom document type, you can create a document icon to represent it. Traditionally, a document icon looks like a piece of paper with its top-right corner folded down. This distinctive appearance helps people distinguish documents from apps and other content, even when icon sizes are small.
If you don’t supply a document icon for a file type you support, macOS creates one for you by compositing your app icon and the file’s extension onto the canvas. For example, Preview uses a system-generated document icon to represent JPG files.
![An image of the Preview document icon for a JPG file.](/images/com.apple.HIG/doc-icon-generated@2x.png)
In some cases, it can make sense to create a set of document icons to represent a range of file types your app handles. For example, Xcode uses custom document icons to help people distinguish projects, AR objects, and Swift code files.
![Image of an Xcode project document icon.](/images/com.apple.HIG/doc-icon-custom-1@2x.png)
![Image of a document icon for an AR object.](/images/com.apple.HIG/doc-icon-custom-2@2x.png)
![Image of a document icon for a Swift file.](/images/com.apple.HIG/doc-icon-custom-3@2x.png)
To create a custom document icon, you can supply any combination of background fill, center image, and text. The system layers, positions, and masks these elements as needed and composites them onto the familiar folded-corner icon shape.
![A square canvas that contains a grid of pink lines and a jagged white EKG line that runs horizontally across the middle. The pink grid gets lighter in color toward the bottom edge.](/images/com.apple.HIG/doc-icon-parts-background-fill@2x.png)
![A solid pink heart.](/images/com.apple.HIG/doc-icon-parts-center-image@2x.png)
![The word heart in all caps.](/images/com.apple.HIG/doc-icon-parts-text~dark@2x.png)
![A custom document icon that displays the pink heart and the word heart on top of the pink grid and white EKG line.](/images/com.apple.HIG/doc-icon-parts@2x.png)
[Apple Design Resources](https://developer.apple.com/design/resources/#macos-apps) provides a template you can use to create a custom background fill and center image for a document icon. As you use this template, follow the guidelines below.
**Design simple images that clearly communicate the document type.** Whether you use a background fill, a center image, or both, prefer uncomplicated shapes and a reduced palette of distinct colors. Your document icon can display as small as 16x16 px, so you want to create designs that remain recognizable at every size.
**Designing a single, expressive image for the background fill can be a great way to help people understand and recognize a document type.** For example, Xcode and TextEdit both use rich background images that don’t include a center image.
![Image of an Xcode project document icon.](/images/com.apple.HIG/doc-icon-custom-1@2x.png)
![Image of a TextEdit rich text document icon.](/images/com.apple.HIG/doc-icon-fill-only@2x.png)
**Consider reducing complexity in the small versions of your document icon.** Icon details that are clear in large versions can look blurry and be hard to recognize in small versions. For example, to ensure that the grid lines in the custom heart document icon remain clear in intermediate sizes, you might use fewer lines and thicken them by aligning them to the reduced pixel grid. In the 16x16 px size, you might remove the lines altogether.
![Pixelated image of the heart document icon. The grid, the EKG line, the heart shape, and the word heart are visible but blurry.](/images/com.apple.HIG/doc-icon-fewer-details-1@2x.png)
![Pixelated image of the heart document icon, in which only the blurry heart shape and EKG line are visible.](/images/com.apple.HIG/doc-icon-fewer-details-2@2x.png)
![Pixelated image of the heart document icon, in which only the blurry heart shape is visible.](/images/com.apple.HIG/doc-icon-fewer-details-3@2x.png)
**Avoid placing important content in the top-right corner of your background fill.** The system automatically masks your image to fit the document icon shape and draws the white folded corner on top of the fill. Create a set of background images in the sizes listed below.
- 512x512 px @1x, 1024x1024 px @2x
- 256x256 px @1x, 512x512 px @2x
- 128x128 px @1x, 256x256 px @2x
- 32x32 px @1x, 64x64 px @2x
- 16x16 px @1x, 32x32 px @2x
**If a familiar object can convey a document’s type or its connection with your app, consider creating a center image that depicts it.** Design a simple, unambiguous image that’s clear and recognizable at every size. The center image measures half the size of the overall document icon canvas. For example, to create a center image for a 32x32 px document icon, use an image canvas that measures 16x16 px. You can provide center images in the following sizes:
- 256x256 px @1x, 512x512 px @2x
- 128x128 px @1x, 256x256 px @2x
- 32x32 px @1x, 64x64 px @2x
- 16x16 px @1x, 32x32 px @2x
**Define a margin that measures about 10% of the image canvas and keep most of the image within it.** Although parts of the image can extend into this margin for optical alignment, it’s best when the image occupies about 80% of the image canvas. For example, most of the center image in a 256x256 px canvas would fit in an area that measures 205x205 px.
![Diagram of the solid pink heart shape within blue margins that measure 10 percent of the canvas width.](/images/com.apple.HIG/doc-icon-parts-margins~dark@2x.png)
**Specify a succinct term if it helps people understand your document type.** By default, the system displays a document’s extension at the bottom edge of the document icon, but if the extension is unfamiliar you can supply a more descriptive term. For example, the document icon for a SceneKit scene file uses the term *scene* instead of the file extension *scn*. The system automatically scales the extension text to fit in the document icon, so be sure to use a term that’s short enough to be legible at small sizes. By default, the system capitalizes every letter in the text.
![Image of a SceneKit scene document icon.](/images/com.apple.HIG/doc-icon-custom-extension@2x.png)

## Resources

#### Related
[App icons](app-icons.md)
[SF Symbols](sf-symbols.md)

#### Videos
- [Designing Glyphs](https://developer.apple.com/videos/play/wwdc2017/823) - Glyphs are a powerful communication tool and a fundamental element of your app’s design language. Learn about important considerations when conceptualizing glyphs and key design principles of crafting effective glyph sets for spaces inside and outside of your app.

## Change log
| Date | Changes |
| --- | --- |
| June 9, 2025 | Added a table of SF Symbols that represent common actions. |
| June 21, 2023 | Updated to include guidance for visionOS. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/icons](https://developer.apple.com/design/human-interface-guidelines/icons)*
