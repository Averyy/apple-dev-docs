---
url: https://developer.apple.com/design/human-interface-guidelines/materials
framework: HIG
---

# Materials

**Type:** article

**Platforms:** ios, ipados, macos, tvos, visionos, watchos

> **Updated 2025-09-09:** Updated guidance for Liquid Glass.

A material is a visual effect that creates a sense of depth, layering, and hierarchy between foreground and background elements.

![A sketch of a capsule shape overlapping a square. A subtle bend in the edges of the square that are beneath the capsule suggests the layering of the Liquid Glass material over background content. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](/images/com.apple.HIG/foundations-materials-intro~dark@2x.png)
Materials help visually separate foreground elements, such as text and controls, from background elements, such as content and solid colors. By allowing color to pass through from background to foreground, a material establishes visual hierarchy to help people more easily retain a sense of place.
Apple platforms feature two types of materials: Liquid Glass, and standard materials. [Liquid Glass](materials.md#Liquid-Glass) is a dynamic material that unifies the design language across Apple platforms, allowing you to present controls and navigation without obscuring underlying content. In contrast to Liquid Glass, the [Standard materials](materials.md#Standard-materials) help with visual differentiation within the content layer.

## Liquid Glass
Liquid Glass forms a distinct functional layer for controls and navigation elements — like tab bars and sidebars — that floats above the content layer, establishing a clear visual hierarchy between functional elements and content. Liquid Glass allows content to scroll and peek through from beneath these elements to give the interface a sense of dynamism and depth, all while maintaining legibility for controls and navigation.
**Don’t use Liquid Glass in the content layer.** Liquid Glass works best when it provides a clear distinction between interactive elements and content, and including it in the content layer can result in unnecessary complexity and a confusing visual hierarchy. Instead, use [Standard materials](materials.md#Standard-materials) for elements in the content layer, such as app backgrounds. An exception to this is for controls in the content layer with a transient interactive element like [Sliders](sliders.md) and [Toggles](toggles.md); in these cases, the element takes on a Liquid Glass appearance to emphasize its interactivity when a person activates it.
**Use Liquid Glass effects sparingly.** Standard components from system frameworks pick up the appearance and behavior of this material automatically. If you apply Liquid Glass effects to a custom control, do so sparingly. Liquid Glass seeks to bring attention to the underlying content, and overusing this material in multiple custom controls can provide a subpar user experience by distracting from that content. Limit these effects to the most important functional elements in your app. For developer guidance, see [Applying Liquid Glass to custom views](../swiftui/applying-liquid-glass-to-custom-views.md).
**Only use clear Liquid Glass for components that appear over visually rich backgrounds.** Liquid Glass provides two variants — [regular](../swiftui/glass/regular.md) and [clear](../swiftui/glass/clear.md) — that you can choose when building custom components or styling some system components. The appearance of these variants can differ in response to certain system settings, like if people choose a preferred look for Liquid Glass in their device’s settings, or turn on accessibility settings that reduce transparency or increase contrast in the interface.
The *regular* variant blurs and adjusts the luminosity of background content to maintain legibility of text and other foreground elements. Scroll edge effects further enhance legibility by blurring and reducing the opacity of background content. Most system components use this variant. Use the regular variant when background content might create legibility issues, or when components have a significant amount of text, such as alerts, sidebars, or popovers.
![A visual example of the regular variant of Liquid Glass, which appears darker when there is a dark background beneath it.](/images/com.apple.HIG/materials-ios-liquid-glass-over-dark@2x.png)
![A visual example of the regular variant of Liquid Glass, which appears lighter when there is a light background beneath it.](/images/com.apple.HIG/materials-ios-liquid-glass-over-light@2x.png)
The *clear* variant is highly translucent, which is ideal for prioritizing the visibility of the underlying content and ensuring visually rich background elements remain prominent. Use this variant for components that float above media backgrounds — such as photos and videos — to create a more immersive content experience.
![A visual example of the clear variant of Liquid Glass, which allows the visual detail of the background beneath it to show through.](/images/com.apple.HIG/materials-ios-liquid-glass-clear@2x.png)
For optimal contrast and legibility, determine whether to add a dimming layer behind components with clear Liquid Glass:
- If the underlying content is bright, consider adding a dark dimming layer of 35% opacity. For developer guidance, see [clear](../swiftui/glass/clear.md).
- If the underlying content is sufficiently dark, or if you use standard media playback controls from AVKit that provide their own dimming layer, you don’t need to apply a dimming layer.
For guidance about the use of color, see [Liquid Glass color](color.md#Liquid-Glass-color).

## Standard materials
Use standard materials and effects — such as [UIBlurEffect](../uikit/uiblureffect.md), [UIVibrancyEffect](../uikit/uivibrancyeffect.md), and [NSVisualEffectView.BlendingMode](../appkit/nsvisualeffectview/blendingmode-swift.enum.md) — to convey a sense of structure in the content beneath Liquid Glass.
**Choose materials and effects based on semantic meaning and recommended usage.** Avoid selecting a material or effect based on the apparent color it imparts to your interface, because system settings can change its appearance and behavior. Instead, match the material or vibrancy style to your specific use case.
**Help ensure legibility by using vibrant colors on top of materials.** When you use system-defined vibrant colors, you don’t need to worry about colors seeming too dark, bright, saturated, or low contrast in different contexts. Regardless of the material you choose, use vibrant colors on top of it. For guidance, see [System colors](color.md#System-colors).
![An illustration of a Share button with a translucent background material and a symbol. The symbol uses the systemGray3 color and is difficult to see against the background material.](/images/com.apple.HIG/materials-legibility-non-vibrant-label~dark@2x.png)
![An X in a circle to indicate incorrect usage](/images/com.apple.HIG/crossout@2x.png)
![An illustration of a Share button with a translucent background material and a symbol. The symbol uses vibrant color and is clearly visible against the background material.](/images/com.apple.HIG/materials-legibility-primary-label~dark@2x.png)
![A checkmark in a circle to indicate correct usage](/images/com.apple.HIG/checkmark@2x.png)
**Consider contrast and visual separation when choosing a material to combine with blur and vibrancy effects.** For example, consider that:
- Thicker materials, which are more opaque, can provide better contrast for text and other elements with fine features.
- Thinner materials, which are more translucent, can help people retain their context by providing a visible reminder of the content that’s in the background.
For developer guidance, see [Material](../swiftui/material.md).

## Platform considerations

### iOS, iPadOS
In addition to Liquid Glass, iOS and iPadOS continue to provide four standard materials — ultra-thin, thin, regular (default), and thick — which you can use in the content layer to help create visual distinction.
![An illustration of the iOS and iPadOS ultraThin material above a colorful background. Where the material overlaps the background, it provides a diffuse gradient of the background colors.](/images/com.apple.HIG/materials-ios-material-background-ultrathin~dark@2x.png)
![An illustration of the iOS and iPadOS thin material above a colorful background. Where the material overlaps the background, it provides a diffuse and slightly darkened gradient of the background colors.](/images/com.apple.HIG/materials-ios-material-background-thin~dark@2x.png)
![An illustration of the iOS and iPadOS regular material above a colorful background. Where the material overlaps the background, it provides a diffuse and darkened gradient of the background colors.](/images/com.apple.HIG/materials-ios-material-background-regular~dark@2x.png)
![An illustration of the iOS and iPadOS thick material above a colorful background. Where the material overlaps the background, it provides a dark, muted gradient of the background colors.](/images/com.apple.HIG/materials-ios-material-background-thick~dark@2x.png)
iOS and iPadOS also define vibrant colors for labels, fills, and separators that are specifically designed to work with each material. Labels and fills both have several levels of vibrancy; separators have one level. The name of a level indicates the relative amount of contrast between an element and the background: The default level has the highest contrast, whereas quaternary (when it exists) has the lowest contrast.
Except for quaternary, you can use the following vibrancy values for labels on any material. In general, avoid using quaternary on top of the [thin](../swiftui/material/thin.md) and [ultraThin](../swiftui/material/ultrathin.md) materials, because the contrast is too low.
- [UIVibrancyEffectStyle.label](../uikit/uivibrancyeffectstyle/label.md) (default)
- [UIVibrancyEffectStyle.secondaryLabel](../uikit/uivibrancyeffectstyle/secondarylabel.md)
- [UIVibrancyEffectStyle.tertiaryLabel](../uikit/uivibrancyeffectstyle/tertiarylabel.md)
- [UIVibrancyEffectStyle.quaternaryLabel](../uikit/uivibrancyeffectstyle/quaternarylabel.md)
You can use the following vibrancy values for fills on all materials.
- [UIVibrancyEffectStyle.fill](../uikit/uivibrancyeffectstyle/fill.md) (default)
- [UIVibrancyEffectStyle.secondaryFill](../uikit/uivibrancyeffectstyle/secondaryfill.md)
- [UIVibrancyEffectStyle.tertiaryFill](../uikit/uivibrancyeffectstyle/tertiaryfill.md)
The system provides a single, default vibrancy value for a [UIVibrancyEffectStyle.separator](../uikit/uivibrancyeffectstyle/separator.md), which works well on all materials.

### macOS
macOS provides several standard materials with designated purposes, and vibrant versions of all [Specifications](color.md#Specifications). For developer guidance, see [NSVisualEffectView.Material](../appkit/nsvisualeffectview/material-swift.enum.md).
**Choose when to allow vibrancy in custom views and controls.** Depending on configuration and system settings, system views and controls use vibrancy to make foreground content stand out against any background. Test your interface in a variety of contexts to discover when vibrancy enhances the appearance and improves communication.
**Choose a background blending mode that complements your interface design.** macOS defines two modes that blend background content: behind window and within window. For developer guidance, see [NSVisualEffectView.BlendingMode](../appkit/nsvisualeffectview/blendingmode-swift.enum.md).

### tvOS
In tvOS, Liquid Glass appears throughout navigation elements and system experiences such as Top Shelf and Control Center. Certain interface elements, like image views and buttons, adopt Liquid Glass when they gain focus.
![A screenshot of the Destination Video app running in tvOS. The app shows a screen with details about a video called A BOT-anist Adventure. The background is a colorful image of the main character in a scene from the video. The interface elements floating above the background adopt a Liquid Glass appearance to allow background color to show through and create a more immersive media experience.](/images/com.apple.HIG/materials-tvos-media-player@2x.png)
In addition to Liquid Glass, tvOS continues to provide standard materials, which you can use to help define structure in the content layer. The thickness of a standard material affects how prominently the underlying content shows through. For example, consider using standard materials in the following ways:
| Material | Recommended for |
| --- | --- |
| [ultraThin](../swiftui/material/ultrathin.md) | Full-screen views that require a light color scheme |
| [thin](../swiftui/material/thin.md) | Overlay views that partially obscure onscreen content and require a light color scheme |
| [regular](../swiftui/material/regular.md) | Overlay views that partially obscure onscreen content |
| [thick](../swiftui/material/thick.md) | Overlay views that partially obscure onscreen content and require a dark color scheme |


### visionOS
In visionOS, windows generally use an unmodifiable system-defined material called *glass* that helps people stay grounded by letting light, the current Environment, virtual content, and objects in people’s surroundings show through. Glass is an adaptive material that limits the range of background color information so a window can continue to provide contrast for app content while becoming brighter or darker depending on people’s physical surroundings and other virtual content.

[Video: visionos-glass-material-transition.mp4](/videos/com.apple.HIG/visionos-glass-material-transition.mp4)

> **Note:** visionOS doesn’t have a distinct Dark Mode setting. Instead, glass automatically adapts to the luminance of the objects and colors behind it.
**Prefer translucency to opaque colors in windows.** Areas of opacity can block people’s view, making them feel constricted and reducing their awareness of the virtual and physical objects around them.
![An illustration of a field of view in visionOS with a window in the center. The window has an opaque background that obstructs its surroundings.](/images/com.apple.HIG/materials-visionos-opaque-window-incorrect@2x.png)
![An X in a circle to indicate incorrect usage](/images/com.apple.HIG/crossout@2x.png)
![An illustration of a field of view in visionOS with a window in the center. The window has a translucent material background that allows its surroundings to pass through.](/images/com.apple.HIG/materials-visionos-glass-window@2x.png)
![A checkmark in a circle to indicate correct usage](/images/com.apple.HIG/checkmark@2x.png)
**If necessary, choose materials that help you create visual separations or indicate interactivity in your app.** If you need to create a custom component, you may need to specify a system material for it. Use the following examples for guidance.
- The [thin](../swiftui/material/thin.md) material brings attention to interactive elements like buttons and selected items.
- The [regular](../swiftui/material/regular.md) material can help you visually separate sections of your app, like a sidebar or a grouped table view.
- The [thick](../swiftui/material/thick.md) material lets you create a dark element that remains visually distinct when it’s on top of an area that uses a `regular` background.
![An illustration of a field of view in visionOS with a window in the center. The window is composed of a sidebar on the left and a content area on the right, with a text field at the top and a button in the lower-right corner. The sidebar uses regular material, while the text field uses thick material and the button uses thin material.](/images/com.apple.HIG/visionos-materials-window-example~dark@2x.png)
To ensure foreground content remains legible when it displays on top of a material, visionOS applies vibrancy to text, symbols, and fills. Vibrancy enhances the sense of depth by pulling light and color forward from both virtual and physical surroundings.
visionOS defines three vibrancy values that help you communicate a hierarchy of text, symbols, and fills.
- Use [UIVibrancyEffectStyle.label](../uikit/uivibrancyeffectstyle/label.md) for standard text.
- Use [UIVibrancyEffectStyle.secondaryLabel](../uikit/uivibrancyeffectstyle/secondarylabel.md) for descriptive text like footnotes and subtitles.
- Use [UIVibrancyEffectStyle.tertiaryLabel](../uikit/uivibrancyeffectstyle/tertiarylabel.md) for inactive elements, and only when text doesn’t need high legibility.
![An illustration of a Share button with a translucent background material and a symbol. The symbol uses the default vibrant label color and has very high contrast against the background material.](/images/com.apple.HIG/materials-visionos-label-vibrant-primary@2x.png)
![An illustration of a Share button with a translucent background material and a symbol. The symbol uses the secondary vibrant label color and has high contrast against the background material.](/images/com.apple.HIG/materials-visionos-label-vibrant-secondary@2x.png)
![An illustration of a Share button with a translucent background material and a symbol. The symbol uses the tertiary vibrant label color and has muted contrast against the background material.](/images/com.apple.HIG/materials-visionos-label-vibrant-tertiary@2x.png)

### watchOS
**Use materials to provide context in a full-screen modal view.** Because full-screen modal views are common in watchOS, the contrast provided by material layers can help orient people in your app and distinguish controls and system elements from other content. Avoid removing or replacing material backgrounds for modal sheets when they’re provided by default.
![An illustration of a modal view in watchOS with an example title, descriptive text, and a single action button. The modal completely covers the screen with a transparent material, and uses a thinner material for the button along with vibrant label text.](/images/com.apple.HIG/watchos-modal-view-material-background@2x.png)

## Resources

#### Related
[Color](color.md)
[Accessibility](accessibility.md)
[Dark Mode](dark-mode.md)

#### Developer documentation
[Adopting Liquid Glass](../technologyoverviews/adopting-liquid-glass.md)
[glassEffect(_:in:)](../swiftui/view/glasseffect(_:in:).md) — SwiftUI
[Material](../swiftui/material.md) — SwiftUI
[UIVisualEffectView](../uikit/uivisualeffectview.md) — UIKit
[NSVisualEffectView](../appkit/nsvisualeffectview.md) — AppKit

#### Videos
- [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219) - Liquid Glass unifies Apple platform design language while providing a more dynamic and expressive user experience. Get to know the design principles of Liquid Glass, explore its core optical and physical properties, and learn where to use it and why.
- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356) - Dive deeper into the new design system to explore key changes to visual design, information architecture, and core system components. Learn how the system reshapes the relationship between interface and content, enabling you to create designs that are dynamic, harmonious, and consistent across devices, screen sizes, and input modes.

## Change log
| Date | Changes |
| --- | --- |
| September 9, 2025 | Updated guidance for Liquid Glass. |
| June 9, 2025 | Added guidance for Liquid Glass. |
| August 6, 2024 | Added platform-specific art. |
| December 5, 2023 | Updated descriptions of the various material types, and clarified terms related to vibrancy and material thickness. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Added guidance on using materials to provide context and orientation in watchOS apps. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/materials](https://developer.apple.com/design/human-interface-guidelines/materials)*
