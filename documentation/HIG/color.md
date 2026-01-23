---
url: https://developer.apple.com/design/human-interface-guidelines/color
framework: HIG
---

# Color

**Type:** article

**Platforms:** ios, ipados, macos, tvos, visionos, watchos

> **Updated 2025-12-16:** Updated guidance for Liquid Glass.

Judicious use of color can enhance communication, evoke your brand, provide visual continuity, communicate status and feedback, and help people understand information.

![A sketch of a paint palette, suggesting the use of color. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/399ee993cc15dc067a0cd53257163ac3/foundations-color-intro~dark%402x.png)
The system defines colors that look good on various backgrounds and appearance modes, and can automatically adapt to vibrancy and accessibility settings. Using system colors is a convenient way to make your experience feel at home on the device.
You may also want to use custom colors to enhance the visual experience of your app or game and express its unique personality. The following guidelines can help you use color in ways that people appreciate, regardless of whether you use system-defined or custom colors.

## Best practices
**Avoid using the same color to mean different things.** Use color consistently throughout your interface, especially when you use it to help communicate information like status or interactivity. For example, if you use your brand color to indicate that a borderless button is interactive, using the same or similar color to stylize noninteractive text is confusing.
**Make sure all your app’s colors work well in light, dark, and increased contrast contexts.** iOS, iPadOS, macOS, and tvOS offer both light and [Dark Mode](dark-mode.md) appearance settings. [System colors](color.md#System-colors) vary subtly depending on the system appearance, adjusting to ensure proper color differentiation and contrast for text, symbols, and other elements. With the Increase Contrast setting turned on, the color differences become far more apparent. When possible, use system colors, which already define variants for all these contexts. If you define a custom color, make sure to supply light and dark variants, and an increased contrast option for each variant that provides a significantly higher amount of visual differentiation. Even if your app ships in a single appearance mode, provide both light and dark colors to support Liquid Glass adaptivity in these contexts.
![A screenshot of the Notes app in iOS with the light system appearance and default contrast. The Notes app is open to a note with the text 'Note'. The text is selected, which shows a yellow selection highlight and text editing menu. The Done button appears in the upper-right corner. The Liquid Glass background of the button is yellow, and its label, which shows a checkmark, is white. The shade of yellow is vibrant.](https://docs-assets.developer.apple.com/published/033f3f6540cc36385bc5993e2152895b/color-context-light-mode%402x.png)
![A screenshot of the Notes app in iOS with the light system appearance and increased contrast. The Notes app is open to a note with the text 'Note'. The text is selected, which shows a yellow selection highlight and text editing menu. The Done button appears in the upper-right corner. The Liquid Glass background of the button is yellow, and its label, which shows a checkmark, is black. The shade of yellow is darker to provide more contrast and differentiation against the note's white background.](https://docs-assets.developer.apple.com/published/9fa4e239f30421b0f00ee77dcace0c14/color-context-light-mode-high-contrast%402x.png)
![A screenshot of the Notes app in iOS with the dark system appearance and default contrast. The Notes app is open to a note with the text 'Note'. The text is selected, which shows a yellow selection highlight and text editing menu. The Done button appears in the upper-right corner. The Liquid Glass background of the button is yellow, and its label, which shows a checkmark, is white.](https://docs-assets.developer.apple.com/published/dc3523da3cba1dd53d3501c763335e6c/color-context-dark-mode%402x.png)
![A screenshot of the Notes app in iOS with the dark system appearance and increased contrast. The Notes app is open to a note with the text 'Note'. The text is selected, which shows a yellow selection highlight and text editing menu. The Done button appears in the upper-right corner. The Liquid Glass background of the button is yellow, and its label, which shows a checkmark, is black.](https://docs-assets.developer.apple.com/published/95af2bc7dece914a5f870f38edac2998/color-context-dark-mode-high-contrast%402x.png)
**Test your app’s color scheme under a variety of lighting conditions.** Colors can look different when you view your app outside on a sunny day or in dim light. In bright surroundings, colors look darker and more muted. In dark environments, colors appear bright and saturated. In visionOS, colors can look different depending on the colors of a wall or object in a person’s physical surroundings and how it reflects light. Adjust app colors to provide an optimal viewing experience in the majority of use cases.
**Test your app on different devices.** For example, the True Tone display — available on certain iPhone, iPad, and Mac models — uses ambient light sensors to automatically adjust the white point of the display to adapt to the lighting conditions of the current environment. Apps that primarily support reading, photos, video, and gaming can strengthen or weaken this effect by specifying a white point adaptivity style (for developer guidance, see [UIWhitePointAdaptivityStyle](../BundleResources/Information-Property-List/UIWhitePointAdaptivityStyle.md)). Test tvOS apps on multiple brands of HD and 4K TVs, and with different display settings. You can also test the appearance of your app using different color profiles on a Mac — such as P3 and Standard RGB (sRGB) — by choosing a profile in System Settings > Displays. For guidance, see [Color management](color.md#Color-management).
**Consider how artwork and translucency affect nearby colors.** Variations in artwork sometimes warrant changes to nearby colors to maintain visual continuity and prevent interface elements from becoming overpowering or underwhelming. Maps, for example, displays a light color scheme when in map mode but switches to a dark color scheme when in satellite mode. Colors can also appear different when placed behind or applied to a translucent element like a toolbar.
**If your app lets people choose colors, prefer system-provided color controls where available.** Using built-in color pickers provides a consistent user experience, in addition to letting people save a set of colors they can access from any app. For developer guidance, see [ColorPicker](../SwiftUI/ColorPicker.md).

## Inclusive color
**Avoid relying solely on color to differentiate between objects, indicate interactivity, or communicate essential information.** When you use color to convey information, be sure to provide the same information in alternative ways so people with color blindness or other visual disabilities can understand it. For example, you can use text labels or glyph shapes to identify objects or states.
**Avoid using colors that make it hard to perceive content in your app.** For example,  insufficient contrast can cause icons and text to blend with the background and make content hard to read, and people who are color blind might not be able to distinguish some color combinations. For guidance, see [Accessibility](accessibility.md).
**Consider how the colors you use might be perceived in other countries and cultures.** For example, red communicates danger in some cultures, but has positive connotations in other cultures. Make sure the colors in your app send the message you intend.
![An illustration of an upward-trending stock chart in the Stocks app in English. The line of the graph is green to indicate the rising value of the stock during the selected time period.](https://docs-assets.developer.apple.com/published/5969ae10a6eaca6879fb43df4f651e4d/color-inclusive-color-charts-english%402x.png)
![An illustration of an upward-trending stock chart in the Stocks app in Chinese. The line of the graph is red to indicate the rising value of the stock during the selected time period.](https://docs-assets.developer.apple.com/published/e84b6e7089f1fb8f73712da462d66164/color-inclusive-color-charts-chinese%402x.png)

## System colors
**Avoid hard-coding system color values in your app.** Documented color values are for your reference during the app design process. The actual color values may fluctuate from release to release, based on a variety of environmental variables. Use APIs like [Color](../SwiftUI/Color.md) to apply system colors.
iOS, iPadOS, macOS, and visionOS also define sets of *dynamic system colors* that match the color schemes of standard UI components and automatically adapt to both light and dark contexts. Each dynamic color is semantically defined by its purpose, rather than its appearance or color values. For example, some colors represent view backgrounds at different levels of hierarchy and other colors represent foreground content, such as labels, links, and separators.
**Avoid redefining the semantic meanings of dynamic system colors.** To ensure a consistent experience and ensure your interface looks great when the appearance of the platform changes, use dynamic system colors as intended. For example, don’t use the [separator](https://developer.apple.com/documentation/uikit/uicolor/separator) color as a text color, or [secondary text label](https://developer.apple.com/documentation/uikit/uicolor/secondarylabel) color as a background color.

## Liquid Glass color
By default, [Liquid Glass](materials.md#Liquid-Glass) has no inherent color, and instead takes on colors from the content directly behind it. You can apply color to some Liquid Glass elements, giving them the appearance of colored or stained glass. This is useful for drawing emphasis to a specific control, like a primary call to action, and is the approach the system uses for prominent button styling. Symbols or text labels on Liquid Glass controls can also have color.
![A screenshot of the Done button in iOS, which appears as a checkmark on a blue Liquid Glass background.](https://docs-assets.developer.apple.com/published/1ae8b1e928a24bed7f651dfc1241fe3a/color-liquid-glass-overview-tinted~dark%402x.png)
![A screenshot of a tab bar in iOS, with the first tab selected. The symbol and text label of the selected tab bar item are blue.](https://docs-assets.developer.apple.com/published/e310b9cbc58ec3049d84140f24b5b41b/color-liquid-glass-overview-color-over-tab-bar~dark%402x.png)
![A screenshot of the Share button in iOS over a colorful image. The colors from the background image infuse the Liquid Glass in the button, affecting its color.](https://docs-assets.developer.apple.com/published/9cf610d972c97dee46b9e206525b2ae7/color-liquid-glass-overview-clear%402x.png)
For smaller elements like toolbars and tab bars, the system can adapt Liquid Glass between a light and dark appearance in response to the underlying content. By default, symbols and text on these elements follow a monochromatic color scheme, becoming darker when the underlying content is light, and lighter when it’s dark. Liquid Glass appears more opaque in larger elements like sidebars to preserve legibility over complex backgrounds and accommodate richer content on the material’s surface.
**Apply color sparingly to the Liquid Glass material, and to symbols or text on the material.** If you apply color, reserve it for elements that truly benefit from emphasis, such as status indicators or primary actions. To emphasize primary actions, apply color to the background rather than to symbols or text. For example, the system applies the app accent color to the background in prominent buttons — such as the Done button — to draw attention and elevate their visual prominence. Refrain from adding color to the background of multiple controls.
![A screenshot of the top half of an iPhone app that shows a toolbar with several buttons. All of the buttons in the toolbar use a blue accent color for their Liquid Glass background.](https://docs-assets.developer.apple.com/published/4e004dcdc21210876c8797dad3202533/colors-liquid-glass-usage-incorrect~dark%402x.png)
![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)
![A screenshot of the top half of an iPhone app that shows a toolbar with several buttons. Only the Done button in the toolbar uses a blue accent color for its Liquid Glass background.](https://docs-assets.developer.apple.com/published/6b65773d247e416e5c784fd9223cc5ac/colors-liquid-glass-usage-correct~dark%402x.png)
![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)
**Avoid using similar colors in control labels if your app has a colorful background.** While color can make apps more visually appealing, playful, or reflective of your brand, too much color can be overwhelming and make control labels more difficult to read. If your app features colorful backgrounds or visually rich content, prefer a monochromatic appearance for toolbars and tab bars, or choose an accent color with sufficient visual differentiation. By contrast, in apps with primarily monochromatic content or backgrounds, choosing your brand color as the app accent color can be an effective way to tailor your app experience and reflect your company’s identity.
**Be aware of the placement of color in the content layer.** Make sure your interface maintains sufficient contrast by avoiding overlap of similar colors in the content layer and controls when possible. Although colorful content might intermittently scroll underneath controls, make sure its default or resting state — like the top of a screen of scrollable content — maintains clear legibility.

## Color management
A *color space* represents the colors in a *color model* like RGB or CMYK. Common color spaces — sometimes called *gamuts* — are sRGB and Display P3.
![Diagram showing the colors included in the sRGB space, compared to the larger number of colors included in the P3 color space.](https://docs-assets.developer.apple.com/published/149433f818fd3b7afbda1949040aad43/color-graphic-wide-color~dark%402x.png)
A *color profile* describes the colors in a color space using, for example, mathematical formulas or tables of data that map colors to numerical representations. An image embeds its color profile so that a device can interpret the image’s colors correctly and reproduce them on a display.
**Apply color profiles to your images.** Color profiles help ensure that your app’s colors appear as intended on different displays. The sRGB color space produces accurate colors on most displays.
**Use wide color to enhance the visual experience on compatible displays.** Wide color displays support a P3 color space, which can produce richer, more saturated colors than sRGB. As a result, photos and videos that use wide color are more lifelike, and visual data and status indicators that use wide color can be more meaningful. When appropriate, use the Display P3 color profile at 16 bits per pixel (per channel) and export images in PNG format. Note that you need to use a wide color display to design wide color images and select P3 colors.
**Provide color space–specific image and color variations if necessary.** In general, P3 colors and images appear fine on sRGB displays. Occasionally, it may be hard to distinguish two very similar P3 colors when viewing them on an sRGB display. Gradients that use P3 colors can also sometimes appear clipped on sRGB displays. To avoid these issues and to ensure visual fidelity on both wide color and sRGB displays, you can use the asset catalog of your Xcode project to provide different versions of images and colors for each color space.

## Platform considerations

### iOS, iPadOS
iOS defines two sets of dynamic background colors — *system* and *grouped* — each of which contains primary, secondary, and tertiary variants that help you convey a hierarchy of information. In general, use the grouped background colors ([systemGroupedBackground](../UIKit/UIColor/systemGroupedBackground.md), [secondarySystemGroupedBackground](../UIKit/UIColor/secondarySystemGroupedBackground.md), and [tertiarySystemGroupedBackground](../UIKit/UIColor/tertiarySystemGroupedBackground.md)) when you have a grouped table view; otherwise, use the system set of background colors ([systemBackground](../UIKit/UIColor/systemBackground.md), [secondarySystemBackground](../UIKit/UIColor/secondarySystemBackground.md), and [tertiarySystemBackground](../UIKit/UIColor/tertiarySystemBackground.md)).
With both sets of background colors, you generally use the variants to indicate hierarchy in the following ways:
- Primary for the overall view
- Secondary for grouping content or elements within the overall view
- Tertiary for grouping content or elements within secondary elements
For foreground content, iOS defines the following dynamic colors:
| Color | Use for… | UIKit API |
| --- | --- | --- |
| Label | A text label that contains primary content. | [label](../UIKit/UIColor/label.md) |
| Secondary label | A text label that contains secondary content. | [secondaryLabel](../UIKit/UIColor/secondaryLabel.md) |
| Tertiary label | A text label that contains tertiary content. | [tertiaryLabel](../UIKit/UIColor/tertiaryLabel.md) |
| Quaternary label | A text label that contains quaternary content. | [quaternaryLabel](../UIKit/UIColor/quaternaryLabel.md) |
| Placeholder text | Placeholder text in controls or text views. | [placeholderText](../UIKit/UIColor/placeholderText.md) |
| Separator | A separator that allows some underlying content to be visible. | [separator](../UIKit/UIColor/separator.md) |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | [opaqueSeparator](../UIKit/UIColor/opaqueSeparator.md) |
| Link | Text that functions as a link. | [link](../UIKit/UIColor/link.md) |


### macOS
macOS defines the following dynamic system colors (you can also view them in the Developer palette of the standard Color panel):
| Color | Use for… | AppKit API |
| --- | --- | --- |
| Alternate selected control text color | The text on a selected surface in a list or table. | [alternateSelectedControlTextColor](../AppKit/NSColor/alternateSelectedControlTextColor.md) |
| Alternating content background colors | The backgrounds of alternating rows or columns in a list, table, or collection view. | [alternatingContentBackgroundColors](../AppKit/NSColor/alternatingContentBackgroundColors.md) |
| Control accent | The accent color people select in System Settings. | [controlAccentColor](../AppKit/NSColor/controlAccentColor.md) |
| Control background color | The background of a large interface element, such as a browser or table. | [controlBackgroundColor](../AppKit/NSColor/controlBackgroundColor.md) |
| Control color | The surface of a control. | [controlColor](../AppKit/NSColor/controlColor.md) |
| Control text color | The text of a control that is available. | [controlTextColor](../AppKit/NSColor/controlTextColor.md) |
| Current control tint | The system-defined control tint. | [currentControlTint](../AppKit/NSColor/currentControlTint.md) |
| Unavailable control text color | The text of a control that’s unavailable. | [disabledControlTextColor](../AppKit/NSColor/disabledControlTextColor.md) |
| Find highlight color | The color of a find indicator. | [findHighlightColor](../AppKit/NSColor/findHighlightColor.md) |
| Grid color | The gridlines of an interface element, such as a table. | [gridColor](../AppKit/NSColor/gridColor.md) |
| Header text color | The text of a header cell in a table. | [headerTextColor](../AppKit/NSColor/headerTextColor.md) |
| Highlight color | The virtual light source onscreen. | [highlightColor](../AppKit/NSColor/highlightColor.md) |
| Keyboard focus indicator color | The ring that appears around the currently focused control when using the keyboard for interface navigation. | [keyboardFocusIndicatorColor](../AppKit/NSColor/keyboardFocusIndicatorColor.md) |
| Label color | The text of a label containing primary content. | [labelColor](../AppKit/NSColor/labelColor.md) |
| Link color | A link to other content. | [linkColor](../AppKit/NSColor/linkColor.md) |
| Placeholder text color | A placeholder string in a control or text view. | [placeholderTextColor](../AppKit/NSColor/placeholderTextColor.md) |
| Quaternary label color | The text of a label of lesser importance than a tertiary label, such as watermark text. | [quaternaryLabelColor](../AppKit/NSColor/quaternaryLabelColor.md) |
| Secondary label color | The text of a label of lesser importance than a primary label, such as a label used to represent a subheading or additional information. | [secondaryLabelColor](../AppKit/NSColor/secondaryLabelColor.md) |
| Selected content background color | The background for selected content in a key window or view. | [selectedContentBackgroundColor](../AppKit/NSColor/selectedContentBackgroundColor.md) |
| Selected control color | The surface of a selected control. | [selectedControlColor](../AppKit/NSColor/selectedControlColor.md) |
| Selected control text color | The text of a selected control. | [selectedControlTextColor](../AppKit/NSColor/selectedControlTextColor.md) |
| Selected menu item text color | The text of a selected menu. | [selectedMenuItemTextColor](../AppKit/NSColor/selectedMenuItemTextColor.md) |
| Selected text background color | The background of selected text. | [selectedTextBackgroundColor](../AppKit/NSColor/selectedTextBackgroundColor.md) |
| Selected text color | The color for selected text. | [selectedTextColor](../AppKit/NSColor/selectedTextColor.md) |
| Separator color | A separator between different sections of content. | [separatorColor](../AppKit/NSColor/separatorColor.md) |
| Shadow color | The virtual shadow cast by a raised object onscreen. | [shadowColor](../AppKit/NSColor/shadowColor.md) |
| Tertiary label color | The text of a label of lesser importance than a secondary label. | [tertiaryLabelColor](../AppKit/NSColor/tertiaryLabelColor.md) |
| Text background color | The background color behind text. | [textBackgroundColor](../AppKit/NSColor/textBackgroundColor.md) |
| Text color | The text in a document. | [textColor](../AppKit/NSColor/textColor.md) |
| Under page background color | The background behind a document’s content. | [underPageBackgroundColor](../AppKit/NSColor/underPageBackgroundColor.md) |
| Unemphasized selected content background color | The selected content in a non-key window or view. | [unemphasizedSelectedContentBackgroundColor](../AppKit/NSColor/unemphasizedSelectedContentBackgroundColor.md) |
| Unemphasized selected text background color | A background for selected text in a non-key window or view. | [unemphasizedSelectedTextBackgroundColor](../AppKit/NSColor/unemphasizedSelectedTextBackgroundColor.md) |
| Unemphasized selected text color | Selected text in a non-key window or view. | [unemphasizedSelectedTextColor](../AppKit/NSColor/unemphasizedSelectedTextColor.md) |
| Window background color | The background of a window. | [windowBackgroundColor](../AppKit/NSColor/windowBackgroundColor.md) |
| Window frame text color | The text in the window’s title bar area. | [windowFrameTextColor](../AppKit/NSColor/windowFrameTextColor.md) |


#### App accent colors
Beginning in macOS 11, you can specify an *accent color* to customize the appearance of your app’s buttons, selection highlighting, and sidebar icons. The system applies your accent color when the current value in General > Accent color settings is *multicolor*.
![A screenshot of the accent color picker in the System Settings app.](https://docs-assets.developer.apple.com/published/9904b9acd3c43cc6cbda49bdb4473299/colors-accent-colors-picker-multicolor~dark%402x.png)
If people set their accent color setting to a value other than multicolor, the system applies their chosen color to the relevant items throughout your app, replacing your accent color. The exception is a sidebar icon that uses a fixed color you specify. Because a fixed-color sidebar icon uses a specific color to provide meaning, the system doesn’t override its color when people change the value of accent color settings. For guidance, see [Sidebars](sidebars.md).

### tvOS
**Consider choosing a limited color palette that coordinates with your app logo.** Subtle use of color can help you communicate your brand while deferring to the content.
**Avoid using only color to indicate focus.** Subtle scaling and responsive animation are the primary ways to denote interactivity when an element is in focus.

### visionOS
**Use color sparingly, especially on glass.** Standard visionOS windows typically use the system-defined glass [Materials](materials.md), which lets light and objects from people’s physical surroundings and their space show through. Because the colors in these physical and virtual objects are visible through the glass, they can affect the legibility of colorful app content in the window. Prefer using color in places where it can help call attention to important information or show the relationship between parts of the interface.
**Prefer using color in bold text and large areas.** Color in lightweight text or small areas can make them harder to see and understand.
**In a fully immersive experience, help people maintain visual comfort by keeping brightness levels balanced.** Although using high contrast can help direct people’s attention to important content, it can also cause visual discomfort if people’s eyes have adjusted to low light or darkness. Consider making content fully bright only when the rest of the visual context is also bright. For example, avoid displaying a bright object on a very dark or black background, especially if the object flashes or moves.

### watchOS
**Use background color to support existing content or supply additional information.** Background color can establish a sense of place and help people recognize key content. For example, in Activity, each infographic view for the Move, Exercise, and Stand Activity rings has a background that matches the color of the ring. Use background color when you have something to communicate, rather than as a solely visual flourish. Avoid using full-screen background color in views that are likely to remain onscreen for long periods of time, such as in a workout or audio-playing app.
**Recognize that people might prefer graphic complications to use tinted mode instead of full color.** The system can use a single color that’s based on the wearer’s selected color in a graphic complication’s images, gauges, and text. For guidance, see [Complications](complications.md).

## Specifications

### System colors
| Name | SwiftUI API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
| --- | --- | --- | --- | --- | --- |
| Red | [red](../SwiftUI/Color/red.md) | ![R-255,G-56,B-60](https://docs-assets.developer.apple.com/published/ea915f0b2fae9ecabba29a63e90d25c4/colors-unified-red-light~dark%402x.png) | ![R-255,G-66,B-69](https://docs-assets.developer.apple.com/published/42db18c65807e9d9d705478ff2da168a/colors-unified-red-dark~dark%402x.png) | ![R-233,G-21,B-45](https://docs-assets.developer.apple.com/published/550b81ae10dc76869bf3bda9812ace09/colors-unified-accessible-red-light~dark%402x.png) | ![R-255,G-97,B-101](https://docs-assets.developer.apple.com/published/c9231fb3d221047819f4646aaee4b2de/colors-unified-accessible-red-dark~dark%402x.png) |
| Orange | [orange](../SwiftUI/Color/orange.md) | ![R-255,G-141,B-40](https://docs-assets.developer.apple.com/published/9f113bce48fc72dc6ca466ad9cdf0f05/colors-unified-orange-light~dark%402x.png) | ![R-255,G-146,B-48](https://docs-assets.developer.apple.com/published/43486a6f9094ca1bd7076a9e707c87f7/colors-unified-orange-dark~dark%402x.png) | ![R-197,G-83,B-0](https://docs-assets.developer.apple.com/published/9204f66a0bb0fe3b2120c0db26b4635b/colors-unified-accessible-orange-light~dark%402x.png) | ![R-255,G-160,B-86](https://docs-assets.developer.apple.com/published/5b36b0f8fab6a36ffa0944d6faf216cc/colors-unified-accessible-orange-dark~dark%402x.png) |
| Yellow | [yellow](../SwiftUI/Color/yellow.md) | ![R-255,G-204,B-0](https://docs-assets.developer.apple.com/published/197fb92a719822d951c8069c1e9f59c3/colors-unified-yellow-light~dark%402x.png) | ![R-255,G-214,B-0](https://docs-assets.developer.apple.com/published/52cccc30652d2fbb806ff41d88bdd56f/colors-unified-yellow-dark~dark%402x.png) | ![R-161,G-106,B-0](https://docs-assets.developer.apple.com/published/69a05ae18e1f69e1d3f2c54275182a7f/colors-unified-accessible-yellow-light~dark%402x.png) | ![R-254,G-223,B-67](https://docs-assets.developer.apple.com/published/6bb1f4620afc521953556213cb891487/colors-unified-accessible-yellow-dark~dark%402x.png) |
| Green | [green](../SwiftUI/Color/green.md) | ![R-52,G-199,B-89](https://docs-assets.developer.apple.com/published/b7fa96f649da33c239d3b825d5c6fd42/colors-unified-green-light~dark%402x.png) | ![R-48,G-209,B-88](https://docs-assets.developer.apple.com/published/f8a83fc5d825c4a9e4f1d9813520053e/colors-unified-green-dark~dark%402x.png) | ![R-0,G-137,B-50](https://docs-assets.developer.apple.com/published/b90190fdd5be94345d7501933ba44e68/colors-unified-accessible-green-light~dark%402x.png) | ![R-74,G-217,B-104](https://docs-assets.developer.apple.com/published/4147a24638f1d3e22f25dde5b20bb548/colors-unified-accessible-green-dark~dark%402x.png) |
| Mint | [mint](../SwiftUI/Color/mint.md) | ![R-0,G-200,B-179](https://docs-assets.developer.apple.com/published/fb878152db5857031038f175540f05ac/colors-unified-mint-light~dark%402x.png) | ![R-0,G-218,B-195](https://docs-assets.developer.apple.com/published/1b118b84eab4b15eee2579ea63c40ffc/colors-unified-mint-dark~dark%402x.png) | ![R-0,G-133,B-117](https://docs-assets.developer.apple.com/published/1040c03509c4025ee26a0bf9791e3b1e/colors-unified-accessible-mint-light~dark%402x.png) | ![R-84,G-223,B-203](https://docs-assets.developer.apple.com/published/03d932a81c8c8a36f5bf02fd77aceb20/colors-unified-accessible-mint-dark~dark%402x.png) |
| Teal | [teal](../SwiftUI/Color/teal.md) | ![R-0,G-195,B-208](https://docs-assets.developer.apple.com/published/48fcae45068a0fe4c2a2d63f5c351970/colors-unified-teal-light~dark%402x.png) | ![R-0,G-210,B-224](https://docs-assets.developer.apple.com/published/86c0f6289b89d95575543329e6ed4e6a/colors-unified-teal-dark~dark%402x.png) | ![R-0,G-129,B-152](https://docs-assets.developer.apple.com/published/bec0729dd11729d4824251e4216c6f48/colors-unified-accessible-teal-light~dark%402x.png) | ![R-59,G-221,B-236](https://docs-assets.developer.apple.com/published/2363a49f5d3548979348e0912820d723/colors-unified-accessible-teal-dark~dark%402x.png) |
| Cyan | [cyan](../SwiftUI/Color/cyan.md) | ![R-0,G-192,B-232](https://docs-assets.developer.apple.com/published/9de8bc6d14b46c36591b618762c2c641/colors-unified-cyan-light~dark%402x.png) | ![R-60,G-211,B-254](https://docs-assets.developer.apple.com/published/788402cbafa6f1644a3a092b0bc32fbd/colors-unified-cyan-dark~dark%402x.png) | ![R-0,G-126,B-174](https://docs-assets.developer.apple.com/published/0bbe8e2745424395e5d541426c12ca5a/colors-unified-accessible-cyan-light~dark%402x.png) | ![R-109,G-217,B-255](https://docs-assets.developer.apple.com/published/e7b37c5c344729946728c72a412fa7c4/colors-unified-accessible-cyan-dark~dark%402x.png) |
| Blue | [blue](../SwiftUI/Color/blue.md) | ![R-0,G-136,B-255](https://docs-assets.developer.apple.com/published/351df342c9792a9924ca098f796fc82a/colors-unified-blue-light~dark%402x.png) | ![R-0,G-145,B-255](https://docs-assets.developer.apple.com/published/0f789f1355e3f6ba1199a17211c35f5c/colors-unified-blue-dark~dark%402x.png) | ![R-30,G-110,B-244](https://docs-assets.developer.apple.com/published/f5dff3297aeb38f035421ff2860cae15/colors-unified-accessible-blue-light~dark%402x.png) | ![R-92,G-184,B-255](https://docs-assets.developer.apple.com/published/f28b5b18d9fc9e1ae8c4930a8dd1b055/colors-unified-accessible-blue-dark~dark%402x.png) |
| Indigo | [indigo](../SwiftUI/Color/indigo.md) | ![R-97,G-85,B-245](https://docs-assets.developer.apple.com/published/e62f44b7aeed4482e99d58791fc8a0e9/colors-unified-indigo-light~dark%402x.png) | ![R-109,G-124,B-255](https://docs-assets.developer.apple.com/published/688208e7e3f0fdeae4e9c7b6b07320ff/colors-unified-indigo-dark~dark%402x.png) | ![R-86,G-74,B-222](https://docs-assets.developer.apple.com/published/6377c830715ed85a8028ad086c9dd51f/colors-unified-accessible-indigo-light~dark%402x.png) | ![R-167,G-170,B-255](https://docs-assets.developer.apple.com/published/e0bce8448f5cfabacd6791c29d41fd59/colors-unified-accessible-indigo-dark~dark%402x.png) |
| Purple | [purple](../SwiftUI/Color/purple.md) | ![R-203,G-48,B-224](https://docs-assets.developer.apple.com/published/d595b3ac24b517a72ddb5c3e1770c9e9/colors-unified-purple-light~dark%402x.png) | ![R-219,G-52,B-242](https://docs-assets.developer.apple.com/published/c1b4feb3ba2bd5479aade16f9b5da50e/colors-unified-purple-dark~dark%402x.png) | ![R-176,G-47,B-194](https://docs-assets.developer.apple.com/published/dbd065673a485eeb3312c29c354b4591/colors-unified-accessible-purple-light~dark%402x.png) | ![R-234,G-141,B-255](https://docs-assets.developer.apple.com/published/8bfeeea59c5f9f0e74d14ad655ff2463/colors-unified-accessible-purple-dark~dark%402x.png) |
| Pink | [pink](../SwiftUI/Color/pink.md) | ![R-255,G-45,B-85](https://docs-assets.developer.apple.com/published/6e0dc7bacc17efdc3563a4737198cf54/colors-unified-pink-light~dark%402x.png) | ![R-255,G-55,B-95](https://docs-assets.developer.apple.com/published/1de8e3f5c64309c96dc31a2121b602ad/colors-unified-pink-dark~dark%402x.png) | ![R-231,G-18,B-77](https://docs-assets.developer.apple.com/published/75c97d6808fde0ccb33248928f843baa/colors-unified-accessible-pink-light~dark%402x.png) | ![R-255,G-138,B-196](https://docs-assets.developer.apple.com/published/5a7e04460249ff709a1dd179409167b0/colors-unified-accessible-pink-dark~dark%402x.png) |
| Brown | [brown](../SwiftUI/Color/brown.md) | ![R-172,G-127,B-94](https://docs-assets.developer.apple.com/published/089f77c7005b1e4753fbdb15c7fbb2ba/colors-unified-brown-light~dark%402x.png) | ![R-183,G-138,B-102](https://docs-assets.developer.apple.com/published/87118d9fb0b8d5fdf2db300fa917946d/colors-unified-brown-dark~dark%402x.png) | ![R-149,G-109,B-81](https://docs-assets.developer.apple.com/published/f97f34fd81b3a8277030d77ffc3a92cd/colors-unified-accessible-brown-light~dark%402x.png) | ![R-219,G-166,B-121](https://docs-assets.developer.apple.com/published/50575ab81511a462d18bc4b9e70a6d4e/colors-unified-accessible-brown-dark~dark%402x.png) |

visionOS system colors use the default dark color values.

### iOS, iPadOS system gray colors
| Name | UIKit API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
| --- | --- | --- | --- | --- | --- |
| Gray | [systemGray](../UIKit/UIColor/systemGray.md) | ![R-142,G-142,B-147](https://docs-assets.developer.apple.com/published/fc7844da63dca3eb793031b3fcad009c/ios-default-systemgray~dark%402x.png) | ![R-142,G-142,B-147](https://docs-assets.developer.apple.com/published/fc7844da63dca3eb793031b3fcad009c/ios-default-systemgraydark~dark%402x.png) | ![R-108,G-108,B-112](https://docs-assets.developer.apple.com/published/e625223100131f5dee931632de898184/ios-accessible-systemgray~dark%402x.png) | ![R-174,G-174,B-178](https://docs-assets.developer.apple.com/published/58db62a1037f1c6b1fa2b0bd93a6c8c8/ios-accessible-systemgraydark~dark%402x.png) |
| Gray (2) | [systemGray2](../UIKit/UIColor/systemGray2.md) | ![R-174,G-174,B-178](https://docs-assets.developer.apple.com/published/58db62a1037f1c6b1fa2b0bd93a6c8c8/ios-default-systemgray2~dark%402x.png) | ![R-99,G-99,B-102](https://docs-assets.developer.apple.com/published/3ec071e8436fcb86681d7d5c8ea70828/ios-default-systemgray2dark~dark%402x.png) | ![R-142,G-142,B-147](https://docs-assets.developer.apple.com/published/fc7844da63dca3eb793031b3fcad009c/ios-accessible-systemgray2~dark%402x.png) | ![R-124,G-124,B-128](https://docs-assets.developer.apple.com/published/a09607f8382407bbfa160033b10133ba/ios-accessible-systemgray2dark~dark%402x.png) |
| Gray (3) | [systemGray3](../UIKit/UIColor/systemGray3.md) | ![R-199,G-199,B-204](https://docs-assets.developer.apple.com/published/73ae5824564aef7887735b9ca4dd7ff4/ios-default-systemgray3~dark%402x.png) | ![R-72,G-72,B-74](https://docs-assets.developer.apple.com/published/0311ff0cb2b3fd13297ba44f8322e16e/ios-default-systemgray3dark~dark%402x.png) | ![R-174,G-174,B-178](https://docs-assets.developer.apple.com/published/58db62a1037f1c6b1fa2b0bd93a6c8c8/ios-accessible-systemgray3~dark%402x.png) | ![R-84,G-84,B-86](https://docs-assets.developer.apple.com/published/3396810a24c448d953260f9ca4350a31/ios-accessible-systemgray3dark~dark%402x.png) |
| Gray (4) | [systemGray4](../UIKit/UIColor/systemGray4.md) | ![R-209,G-209,B-214](https://docs-assets.developer.apple.com/published/578fb5c8fe0ce897d2284cecf48c44f1/ios-default-systemgray4~dark%402x.png) | ![R-58,G-58,B-60](https://docs-assets.developer.apple.com/published/7005ec8bc69614738d9e3049492345ae/ios-default-systemgray4dark~dark%402x.png) | ![R-188,G-188,B-192](https://docs-assets.developer.apple.com/published/4dd6e0fd91458cf508ac840976927f08/ios-accessible-systemgray4~dark%402x.png) | ![R-68,G-68,B-70](https://docs-assets.developer.apple.com/published/4ef8ddfba543d3508a474f75f7b85ee0/ios-accessible-systemgray4dark~dark%402x.png) |
| Gray (5) | [systemGray5](../UIKit/UIColor/systemGray5.md) | ![R-229,G-229,B-234](https://docs-assets.developer.apple.com/published/b7229e6eceb56a0b58d8c415a2c1b22e/ios-default-systemgray5~dark%402x.png) | ![R-44,G-44,B-46](https://docs-assets.developer.apple.com/published/673d4e275b24a1d655d6f7c653e2038a/ios-default-systemgray5dark~dark%402x.png) | ![R-216,G-216,B-220](https://docs-assets.developer.apple.com/published/244c642510d598463d0c2394ff419c30/ios-accessible-systemgray5~dark%402x.png) | ![R-54,G-54,B-56](https://docs-assets.developer.apple.com/published/e211241a8701e439e6bdc4915789e6b2/ios-accessible-systemgray5dark~dark%402x.png) |
| Gray (6) | [systemGray6](../UIKit/UIColor/systemGray6.md) | ![R-242,G-242,B-247](https://docs-assets.developer.apple.com/published/d23b10d7843ba47642c1497003d8fbe1/ios-default-systemgray6~dark%402x.png) | ![R-28,G-28,B-30](https://docs-assets.developer.apple.com/published/484fbf15a627fbf729a7400f0d07b7c4/ios-default-systemgray6dark~dark%402x.png) | ![R-235,G-235,B-240](https://docs-assets.developer.apple.com/published/0fad10fc530d0760746e46bf164028c8/ios-accessible-systemgray6~dark%402x.png) | ![R-36,G-36,B-38](https://docs-assets.developer.apple.com/published/abcc9796e953856c4c11b0ff83f470b8/ios-accessible-systemgray6dark~dark%402x.png) |

In SwiftUI, the equivalent of `systemGray` is [gray](../SwiftUI/Color/gray.md).

## Resources

#### Related
[Dark Mode](dark-mode.md)
[Accessibility](accessibility.md)
[Materials](materials.md)
[Apple Design Resources](https://developer.apple.com/design/resources/)

#### Developer documentation
[Color](../SwiftUI/Color.md) — SwiftUI
[UIColor](../UIKit/UIColor.md) — UIKit
[Color](../AppKit/color.md) — AppKit

#### Videos
- [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219) - Liquid Glass unifies Apple platform design language while providing a more dynamic and expressive user experience. Get to know the design principles of Liquid Glass, explore its core optical and physical properties, and learn where to use it and why.

## Change log
| Date | Changes |
| --- | --- |
| December 16, 2025 | Updated guidance for Liquid Glass. |
| June 9, 2025 | Updated system color values, and added guidance for Liquid Glass. |
| February 2, 2024 | Distinguished UIKit and SwiftUI gray colors in iOS and iPadOS, and added guidance for balancing brightness levels in visionOS apps. |
| September 12, 2023 | Enhanced guidance for using background color in watchOS views, and added color swatches for tvOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using background color in watchOS. |
| December 19, 2022 | Corrected RGB values for system mint color (Dark Mode) in iOS and iPadOS. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/color](https://developer.apple.com/design/human-interface-guidelines/color)*
