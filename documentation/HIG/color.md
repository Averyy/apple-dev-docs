---
url: https://developer.apple.com/design/human-interface-guidelines/color
framework: HIG
---

# Color

**Type:** article

**Platforms:** ios, ipados, macos, tvos, visionos, watchos

> **Updated 2025-12-16:** Updated guidance for Liquid Glass.

Judicious use of color can enhance communication, evoke your brand, provide visual continuity, communicate status and feedback, and help people understand information.

![A sketch of a paint palette, suggesting the use of color. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](/images/com.apple.HIG/foundations-color-intro~dark@2x.png)
The system defines colors that look good on various backgrounds and appearance modes, and can automatically adapt to vibrancy and accessibility settings. Using system colors is a convenient way to make your experience feel at home on the device.
You may also want to use custom colors to enhance the visual experience of your app or game and express its unique personality. The following guidelines can help you use color in ways that people appreciate, regardless of whether you use system-defined or custom colors.

## Best practices
**Avoid using the same color to mean different things.** Use color consistently throughout your interface, especially when you use it to help communicate information like status or interactivity. For example, if you use your brand color to indicate that a borderless button is interactive, using the same or similar color to stylize noninteractive text is confusing.
**Make sure all your app’s colors work well in light, dark, and increased contrast contexts.** iOS, iPadOS, macOS, and tvOS offer both light and [Dark Mode](dark-mode.md) appearance settings. [System colors](color.md#System-colors) vary subtly depending on the system appearance, adjusting to ensure proper color differentiation and contrast for text, symbols, and other elements. With the Increase Contrast setting turned on, the color differences become far more apparent. When possible, use system colors, which already define variants for all these contexts. If you define a custom color, make sure to supply light and dark variants, and an increased contrast option for each variant that provides a significantly higher amount of visual differentiation. Even if your app ships in a single appearance mode, provide both light and dark colors to support Liquid Glass adaptivity in these contexts.
![A screenshot of the Notes app in iOS with the light system appearance and default contrast. The Notes app is open to a note with the text 'Note'. The text is selected, which shows a yellow selection highlight and text editing menu. The Done button appears in the upper-right corner. The Liquid Glass background of the button is yellow, and its label, which shows a checkmark, is white. The shade of yellow is vibrant.](/images/com.apple.HIG/color-context-light-mode@2x.png)
![A screenshot of the Notes app in iOS with the light system appearance and increased contrast. The Notes app is open to a note with the text 'Note'. The text is selected, which shows a yellow selection highlight and text editing menu. The Done button appears in the upper-right corner. The Liquid Glass background of the button is yellow, and its label, which shows a checkmark, is black. The shade of yellow is darker to provide more contrast and differentiation against the note's white background.](/images/com.apple.HIG/color-context-light-mode-high-contrast@2x.png)
![A screenshot of the Notes app in iOS with the dark system appearance and default contrast. The Notes app is open to a note with the text 'Note'. The text is selected, which shows a yellow selection highlight and text editing menu. The Done button appears in the upper-right corner. The Liquid Glass background of the button is yellow, and its label, which shows a checkmark, is white.](/images/com.apple.HIG/color-context-dark-mode@2x.png)
![A screenshot of the Notes app in iOS with the dark system appearance and increased contrast. The Notes app is open to a note with the text 'Note'. The text is selected, which shows a yellow selection highlight and text editing menu. The Done button appears in the upper-right corner. The Liquid Glass background of the button is yellow, and its label, which shows a checkmark, is black.](/images/com.apple.HIG/color-context-dark-mode-high-contrast@2x.png)
**Test your app’s color scheme under a variety of lighting conditions.** Colors can look different when you view your app outside on a sunny day or in dim light. In bright surroundings, colors look darker and more muted. In dark environments, colors appear bright and saturated. In visionOS, colors can look different depending on the colors of a wall or object in a person’s physical surroundings and how it reflects light. Adjust app colors to provide an optimal viewing experience in the majority of use cases.
**Test your app on different devices.** For example, the True Tone display — available on certain iPhone, iPad, and Mac models — uses ambient light sensors to automatically adjust the white point of the display to adapt to the lighting conditions of the current environment. Apps that primarily support reading, photos, video, and gaming can strengthen or weaken this effect by specifying a white point adaptivity style (for developer guidance, see [UIWhitePointAdaptivityStyle](../bundleresources/information-property-list/uiwhitepointadaptivitystyle.md)). Test tvOS apps on multiple brands of HD and 4K TVs, and with different display settings. You can also test the appearance of your app using different color profiles on a Mac — such as P3 and Standard RGB (sRGB) — by choosing a profile in System Settings > Displays. For guidance, see [Color management](color.md#Color-management).
**Consider how artwork and translucency affect nearby colors.** Variations in artwork sometimes warrant changes to nearby colors to maintain visual continuity and prevent interface elements from becoming overpowering or underwhelming. Maps, for example, displays a light color scheme when in map mode but switches to a dark color scheme when in satellite mode. Colors can also appear different when placed behind or applied to a translucent element like a toolbar.
**If your app lets people choose colors, prefer system-provided color controls where available.** Using built-in color pickers provides a consistent user experience, in addition to letting people save a set of colors they can access from any app. For developer guidance, see [ColorPicker](../swiftui/colorpicker.md).

## Inclusive color
**Avoid relying solely on color to differentiate between objects, indicate interactivity, or communicate essential information.** When you use color to convey information, be sure to provide the same information in alternative ways so people with color blindness or other visual disabilities can understand it. For example, you can use text labels or glyph shapes to identify objects or states.
**Avoid using colors that make it hard to perceive content in your app.** For example,  insufficient contrast can cause icons and text to blend with the background and make content hard to read, and people who are color blind might not be able to distinguish some color combinations. For guidance, see [Accessibility](accessibility.md).
**Consider how the colors you use might be perceived in other countries and cultures.** For example, red communicates danger in some cultures, but has positive connotations in other cultures. Make sure the colors in your app send the message you intend.
![An illustration of an upward-trending stock chart in the Stocks app in English. The line of the graph is green to indicate the rising value of the stock during the selected time period.](/images/com.apple.HIG/color-inclusive-color-charts-english@2x.png)
![An illustration of an upward-trending stock chart in the Stocks app in Chinese. The line of the graph is red to indicate the rising value of the stock during the selected time period.](/images/com.apple.HIG/color-inclusive-color-charts-chinese@2x.png)

## System colors
**Avoid hard-coding system color values in your app.** Documented color values are for your reference during the app design process. The actual color values may fluctuate from release to release, based on a variety of environmental variables. Use APIs like [Color](../swiftui/color.md) to apply system colors.
iOS, iPadOS, macOS, and visionOS also define sets of *dynamic system colors* that match the color schemes of standard UI components and automatically adapt to both light and dark contexts. Each dynamic color is semantically defined by its purpose, rather than its appearance or color values. For example, some colors represent view backgrounds at different levels of hierarchy and other colors represent foreground content, such as labels, links, and separators.
**Avoid redefining the semantic meanings of dynamic system colors.** To ensure a consistent experience and ensure your interface looks great when the appearance of the platform changes, use dynamic system colors as intended. For example, don’t use the [separator](https://developer.apple.com/documentation/uikit/uicolor/separator) color as a text color, or [secondary text label](https://developer.apple.com/documentation/uikit/uicolor/secondarylabel) color as a background color.

## Liquid Glass color
By default, [Liquid Glass](materials.md#Liquid-Glass) has no inherent color, and instead takes on colors from the content directly behind it. You can apply color to some Liquid Glass elements, giving them the appearance of colored or stained glass. This is useful for drawing emphasis to a specific control, like a primary call to action, and is the approach the system uses for prominent button styling. Symbols or text labels on Liquid Glass controls can also have color.
![A screenshot of the Done button in iOS, which appears as a checkmark on a blue Liquid Glass background.](/images/com.apple.HIG/color-liquid-glass-overview-tinted~dark@2x.png)
![A screenshot of a tab bar in iOS, with the first tab selected. The symbol and text label of the selected tab bar item are blue.](/images/com.apple.HIG/color-liquid-glass-overview-color-over-tab-bar~dark@2x.png)
![A screenshot of the Share button in iOS over a colorful image. The colors from the background image infuse the Liquid Glass in the button, affecting its color.](/images/com.apple.HIG/color-liquid-glass-overview-clear@2x.png)
For smaller elements like toolbars and tab bars, the system can adapt Liquid Glass between a light and dark appearance in response to the underlying content. By default, symbols and text on these elements follow a monochromatic color scheme, becoming darker when the underlying content is light, and lighter when it’s dark. Liquid Glass appears more opaque in larger elements like sidebars to preserve legibility over complex backgrounds and accommodate richer content on the material’s surface.
**Apply color sparingly to the Liquid Glass material, and to symbols or text on the material.** If you apply color, reserve it for elements that truly benefit from emphasis, such as status indicators or primary actions. To emphasize primary actions, apply color to the background rather than to symbols or text. For example, the system applies the app accent color to the background in prominent buttons — such as the Done button — to draw attention and elevate their visual prominence. Refrain from adding color to the background of multiple controls.
![A screenshot of the top half of an iPhone app that shows a toolbar with several buttons. All of the buttons in the toolbar use a blue accent color for their Liquid Glass background.](/images/com.apple.HIG/colors-liquid-glass-usage-incorrect~dark@2x.png)
![An X in a circle to indicate incorrect usage.](/images/com.apple.HIG/crossout@2x.png)
![A screenshot of the top half of an iPhone app that shows a toolbar with several buttons. Only the Done button in the toolbar uses a blue accent color for its Liquid Glass background.](/images/com.apple.HIG/colors-liquid-glass-usage-correct~dark@2x.png)
![A checkmark in a circle to indicate correct usage.](/images/com.apple.HIG/checkmark@2x.png)
**Avoid using similar colors in control labels if your app has a colorful background.** While color can make apps more visually appealing, playful, or reflective of your brand, too much color can be overwhelming and make control labels more difficult to read. If your app features colorful backgrounds or visually rich content, prefer a monochromatic appearance for toolbars and tab bars, or choose an accent color with sufficient visual differentiation. By contrast, in apps with primarily monochromatic content or backgrounds, choosing your brand color as the app accent color can be an effective way to tailor your app experience and reflect your company’s identity.
**Be aware of the placement of color in the content layer.** Make sure your interface maintains sufficient contrast by avoiding overlap of similar colors in the content layer and controls when possible. Although colorful content might intermittently scroll underneath controls, make sure its default or resting state — like the top of a screen of scrollable content — maintains clear legibility.

## Color management
A *color space* represents the colors in a *color model* like RGB or CMYK. Common color spaces — sometimes called *gamuts* — are sRGB and Display P3.
![Diagram showing the colors included in the sRGB space, compared to the larger number of colors included in the P3 color space.](/images/com.apple.HIG/color-graphic-wide-color~dark@2x.png)
A *color profile* describes the colors in a color space using, for example, mathematical formulas or tables of data that map colors to numerical representations. An image embeds its color profile so that a device can interpret the image’s colors correctly and reproduce them on a display.
**Apply color profiles to your images.** Color profiles help ensure that your app’s colors appear as intended on different displays. The sRGB color space produces accurate colors on most displays.
**Use wide color to enhance the visual experience on compatible displays.** Wide color displays support a P3 color space, which can produce richer, more saturated colors than sRGB. As a result, photos and videos that use wide color are more lifelike, and visual data and status indicators that use wide color can be more meaningful. When appropriate, use the Display P3 color profile at 16 bits per pixel (per channel) and export images in PNG format. Note that you need to use a wide color display to design wide color images and select P3 colors.
**Provide color space–specific image and color variations if necessary.** In general, P3 colors and images appear fine on sRGB displays. Occasionally, it may be hard to distinguish two very similar P3 colors when viewing them on an sRGB display. Gradients that use P3 colors can also sometimes appear clipped on sRGB displays. To avoid these issues and to ensure visual fidelity on both wide color and sRGB displays, you can use the asset catalog of your Xcode project to provide different versions of images and colors for each color space.

## Platform considerations

### iOS, iPadOS
iOS defines two sets of dynamic background colors — *system* and *grouped* — each of which contains primary, secondary, and tertiary variants that help you convey a hierarchy of information. In general, use the grouped background colors ([systemGroupedBackground](../uikit/uicolor/systemgroupedbackground.md), [secondarySystemGroupedBackground](../uikit/uicolor/secondarysystemgroupedbackground.md), and [tertiarySystemGroupedBackground](../uikit/uicolor/tertiarysystemgroupedbackground.md)) when you have a grouped table view; otherwise, use the system set of background colors ([systemBackground](../uikit/uicolor/systembackground.md), [secondarySystemBackground](../uikit/uicolor/secondarysystembackground.md), and [tertiarySystemBackground](../uikit/uicolor/tertiarysystembackground.md)).
With both sets of background colors, you generally use the variants to indicate hierarchy in the following ways:
- Primary for the overall view
- Secondary for grouping content or elements within the overall view
- Tertiary for grouping content or elements within secondary elements
For foreground content, iOS defines the following dynamic colors:
| Color | Use for… | UIKit API |
| --- | --- | --- |
| Label | A text label that contains primary content. | [label](../uikit/uicolor/label.md) |
| Secondary label | A text label that contains secondary content. | [secondaryLabel](../uikit/uicolor/secondarylabel.md) |
| Tertiary label | A text label that contains tertiary content. | [tertiaryLabel](../uikit/uicolor/tertiarylabel.md) |
| Quaternary label | A text label that contains quaternary content. | [quaternaryLabel](../uikit/uicolor/quaternarylabel.md) |
| Placeholder text | Placeholder text in controls or text views. | [placeholderText](../uikit/uicolor/placeholdertext.md) |
| Separator | A separator that allows some underlying content to be visible. | [separator](../uikit/uicolor/separator.md) |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | [opaqueSeparator](../uikit/uicolor/opaqueseparator.md) |
| Link | Text that functions as a link. | [link](../uikit/uicolor/link.md) |


### macOS
macOS defines the following dynamic system colors (you can also view them in the Developer palette of the standard Color panel):
| Color | Use for… | AppKit API |
| --- | --- | --- |
| Alternate selected control text color | The text on a selected surface in a list or table. | [alternateSelectedControlTextColor](../appkit/nscolor/alternateselectedcontroltextcolor.md) |
| Alternating content background colors | The backgrounds of alternating rows or columns in a list, table, or collection view. | [alternatingContentBackgroundColors](../appkit/nscolor/alternatingcontentbackgroundcolors.md) |
| Control accent | The accent color people select in System Settings. | [controlAccentColor](../appkit/nscolor/controlaccentcolor.md) |
| Control background color | The background of a large interface element, such as a browser or table. | [controlBackgroundColor](../appkit/nscolor/controlbackgroundcolor.md) |
| Control color | The surface of a control. | [controlColor](../appkit/nscolor/controlcolor.md) |
| Control text color | The text of a control that is available. | [controlTextColor](../appkit/nscolor/controltextcolor.md) |
| Current control tint | The system-defined control tint. | [currentControlTint](../appkit/nscolor/currentcontroltint.md) |
| Unavailable control text color | The text of a control that’s unavailable. | [disabledControlTextColor](../appkit/nscolor/disabledcontroltextcolor.md) |
| Find highlight color | The color of a find indicator. | [findHighlightColor](../appkit/nscolor/findhighlightcolor.md) |
| Grid color | The gridlines of an interface element, such as a table. | [gridColor](../appkit/nscolor/gridcolor.md) |
| Header text color | The text of a header cell in a table. | [headerTextColor](../appkit/nscolor/headertextcolor.md) |
| Highlight color | The virtual light source onscreen. | [highlightColor](../appkit/nscolor/highlightcolor.md) |
| Keyboard focus indicator color | The ring that appears around the currently focused control when using the keyboard for interface navigation. | [keyboardFocusIndicatorColor](../appkit/nscolor/keyboardfocusindicatorcolor.md) |
| Label color | The text of a label containing primary content. | [labelColor](../appkit/nscolor/labelcolor.md) |
| Link color | A link to other content. | [linkColor](../appkit/nscolor/linkcolor.md) |
| Placeholder text color | A placeholder string in a control or text view. | [placeholderTextColor](../appkit/nscolor/placeholdertextcolor.md) |
| Quaternary label color | The text of a label of lesser importance than a tertiary label, such as watermark text. | [quaternaryLabelColor](../appkit/nscolor/quaternarylabelcolor.md) |
| Secondary label color | The text of a label of lesser importance than a primary label, such as a label used to represent a subheading or additional information. | [secondaryLabelColor](../appkit/nscolor/secondarylabelcolor.md) |
| Selected content background color | The background for selected content in a key window or view. | [selectedContentBackgroundColor](../appkit/nscolor/selectedcontentbackgroundcolor.md) |
| Selected control color | The surface of a selected control. | [selectedControlColor](../appkit/nscolor/selectedcontrolcolor.md) |
| Selected control text color | The text of a selected control. | [selectedControlTextColor](../appkit/nscolor/selectedcontroltextcolor.md) |
| Selected menu item text color | The text of a selected menu. | [selectedMenuItemTextColor](../appkit/nscolor/selectedmenuitemtextcolor.md) |
| Selected text background color | The background of selected text. | [selectedTextBackgroundColor](../appkit/nscolor/selectedtextbackgroundcolor.md) |
| Selected text color | The color for selected text. | [selectedTextColor](../appkit/nscolor/selectedtextcolor.md) |
| Separator color | A separator between different sections of content. | [separatorColor](../appkit/nscolor/separatorcolor.md) |
| Shadow color | The virtual shadow cast by a raised object onscreen. | [shadowColor](../appkit/nscolor/shadowcolor.md) |
| Tertiary label color | The text of a label of lesser importance than a secondary label. | [tertiaryLabelColor](../appkit/nscolor/tertiarylabelcolor.md) |
| Text background color | The background color behind text. | [textBackgroundColor](../appkit/nscolor/textbackgroundcolor.md) |
| Text color | The text in a document. | [textColor](../appkit/nscolor/textcolor.md) |
| Under page background color | The background behind a document’s content. | [underPageBackgroundColor](../appkit/nscolor/underpagebackgroundcolor.md) |
| Unemphasized selected content background color | The selected content in a non-key window or view. | [unemphasizedSelectedContentBackgroundColor](../appkit/nscolor/unemphasizedselectedcontentbackgroundcolor.md) |
| Unemphasized selected text background color | A background for selected text in a non-key window or view. | [unemphasizedSelectedTextBackgroundColor](../appkit/nscolor/unemphasizedselectedtextbackgroundcolor.md) |
| Unemphasized selected text color | Selected text in a non-key window or view. | [unemphasizedSelectedTextColor](../appkit/nscolor/unemphasizedselectedtextcolor.md) |
| Window background color | The background of a window. | [windowBackgroundColor](../appkit/nscolor/windowbackgroundcolor.md) |
| Window frame text color | The text in the window’s title bar area. | [windowFrameTextColor](../appkit/nscolor/windowframetextcolor.md) |


#### App accent colors
Beginning in macOS 11, you can specify an *accent color* to customize the appearance of your app’s buttons, selection highlighting, and sidebar icons. The system applies your accent color when the current value in General > Accent color settings is *multicolor*.
![A screenshot of the accent color picker in the System Settings app.](/images/com.apple.HIG/colors-accent-colors-picker-multicolor~dark@2x.png)
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
| Red | [red](../swiftui/color/red.md) | ![R-255,G-56,B-60](/images/com.apple.HIG/colors-unified-red-light~dark@2x.png) | ![R-255,G-66,B-69](/images/com.apple.HIG/colors-unified-red-dark~dark@2x.png) | ![R-233,G-21,B-45](/images/com.apple.HIG/colors-unified-accessible-red-light~dark@2x.png) | ![R-255,G-97,B-101](/images/com.apple.HIG/colors-unified-accessible-red-dark~dark@2x.png) |
| Orange | [orange](../swiftui/color/orange.md) | ![R-255,G-141,B-40](/images/com.apple.HIG/colors-unified-orange-light~dark@2x.png) | ![R-255,G-146,B-48](/images/com.apple.HIG/colors-unified-orange-dark~dark@2x.png) | ![R-197,G-83,B-0](/images/com.apple.HIG/colors-unified-accessible-orange-light~dark@2x.png) | ![R-255,G-160,B-86](/images/com.apple.HIG/colors-unified-accessible-orange-dark~dark@2x.png) |
| Yellow | [yellow](../swiftui/color/yellow.md) | ![R-255,G-204,B-0](/images/com.apple.HIG/colors-unified-yellow-light~dark@2x.png) | ![R-255,G-214,B-0](/images/com.apple.HIG/colors-unified-yellow-dark~dark@2x.png) | ![R-161,G-106,B-0](/images/com.apple.HIG/colors-unified-accessible-yellow-light~dark@2x.png) | ![R-254,G-223,B-67](/images/com.apple.HIG/colors-unified-accessible-yellow-dark~dark@2x.png) |
| Green | [green](../swiftui/color/green.md) | ![R-52,G-199,B-89](/images/com.apple.HIG/colors-unified-green-light~dark@2x.png) | ![R-48,G-209,B-88](/images/com.apple.HIG/colors-unified-green-dark~dark@2x.png) | ![R-0,G-137,B-50](/images/com.apple.HIG/colors-unified-accessible-green-light~dark@2x.png) | ![R-74,G-217,B-104](/images/com.apple.HIG/colors-unified-accessible-green-dark~dark@2x.png) |
| Mint | [mint](../swiftui/color/mint.md) | ![R-0,G-200,B-179](/images/com.apple.HIG/colors-unified-mint-light~dark@2x.png) | ![R-0,G-218,B-195](/images/com.apple.HIG/colors-unified-mint-dark~dark@2x.png) | ![R-0,G-133,B-117](/images/com.apple.HIG/colors-unified-accessible-mint-light~dark@2x.png) | ![R-84,G-223,B-203](/images/com.apple.HIG/colors-unified-accessible-mint-dark~dark@2x.png) |
| Teal | [teal](../swiftui/color/teal.md) | ![R-0,G-195,B-208](/images/com.apple.HIG/colors-unified-teal-light~dark@2x.png) | ![R-0,G-210,B-224](/images/com.apple.HIG/colors-unified-teal-dark~dark@2x.png) | ![R-0,G-129,B-152](/images/com.apple.HIG/colors-unified-accessible-teal-light~dark@2x.png) | ![R-59,G-221,B-236](/images/com.apple.HIG/colors-unified-accessible-teal-dark~dark@2x.png) |
| Cyan | [cyan](../swiftui/color/cyan.md) | ![R-0,G-192,B-232](/images/com.apple.HIG/colors-unified-cyan-light~dark@2x.png) | ![R-60,G-211,B-254](/images/com.apple.HIG/colors-unified-cyan-dark~dark@2x.png) | ![R-0,G-126,B-174](/images/com.apple.HIG/colors-unified-accessible-cyan-light~dark@2x.png) | ![R-109,G-217,B-255](/images/com.apple.HIG/colors-unified-accessible-cyan-dark~dark@2x.png) |
| Blue | [blue](../swiftui/color/blue.md) | ![R-0,G-136,B-255](/images/com.apple.HIG/colors-unified-blue-light~dark@2x.png) | ![R-0,G-145,B-255](/images/com.apple.HIG/colors-unified-blue-dark~dark@2x.png) | ![R-30,G-110,B-244](/images/com.apple.HIG/colors-unified-accessible-blue-light~dark@2x.png) | ![R-92,G-184,B-255](/images/com.apple.HIG/colors-unified-accessible-blue-dark~dark@2x.png) |
| Indigo | [indigo](../swiftui/color/indigo.md) | ![R-97,G-85,B-245](/images/com.apple.HIG/colors-unified-indigo-light~dark@2x.png) | ![R-109,G-124,B-255](/images/com.apple.HIG/colors-unified-indigo-dark~dark@2x.png) | ![R-86,G-74,B-222](/images/com.apple.HIG/colors-unified-accessible-indigo-light~dark@2x.png) | ![R-167,G-170,B-255](/images/com.apple.HIG/colors-unified-accessible-indigo-dark~dark@2x.png) |
| Purple | [purple](../swiftui/color/purple.md) | ![R-203,G-48,B-224](/images/com.apple.HIG/colors-unified-purple-light~dark@2x.png) | ![R-219,G-52,B-242](/images/com.apple.HIG/colors-unified-purple-dark~dark@2x.png) | ![R-176,G-47,B-194](/images/com.apple.HIG/colors-unified-accessible-purple-light~dark@2x.png) | ![R-234,G-141,B-255](/images/com.apple.HIG/colors-unified-accessible-purple-dark~dark@2x.png) |
| Pink | [pink](../swiftui/color/pink.md) | ![R-255,G-45,B-85](/images/com.apple.HIG/colors-unified-pink-light~dark@2x.png) | ![R-255,G-55,B-95](/images/com.apple.HIG/colors-unified-pink-dark~dark@2x.png) | ![R-231,G-18,B-77](/images/com.apple.HIG/colors-unified-accessible-pink-light~dark@2x.png) | ![R-255,G-138,B-196](/images/com.apple.HIG/colors-unified-accessible-pink-dark~dark@2x.png) |
| Brown | [brown](../swiftui/color/brown.md) | ![R-172,G-127,B-94](/images/com.apple.HIG/colors-unified-brown-light~dark@2x.png) | ![R-183,G-138,B-102](/images/com.apple.HIG/colors-unified-brown-dark~dark@2x.png) | ![R-149,G-109,B-81](/images/com.apple.HIG/colors-unified-accessible-brown-light~dark@2x.png) | ![R-219,G-166,B-121](/images/com.apple.HIG/colors-unified-accessible-brown-dark~dark@2x.png) |

visionOS system colors use the default dark color values.

### iOS, iPadOS system gray colors
| Name | UIKit API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
| --- | --- | --- | --- | --- | --- |
| Gray | [systemGray](../uikit/uicolor/systemgray.md) | ![R-142,G-142,B-147](/images/com.apple.HIG/ios-default-systemgray~dark@2x.png) | ![R-142,G-142,B-147](/images/com.apple.HIG/ios-default-systemgraydark~dark@2x.png) | ![R-108,G-108,B-112](/images/com.apple.HIG/ios-accessible-systemgray~dark@2x.png) | ![R-174,G-174,B-178](/images/com.apple.HIG/ios-accessible-systemgraydark~dark@2x.png) |
| Gray (2) | [systemGray2](../uikit/uicolor/systemgray2.md) | ![R-174,G-174,B-178](/images/com.apple.HIG/ios-default-systemgray2~dark@2x.png) | ![R-99,G-99,B-102](/images/com.apple.HIG/ios-default-systemgray2dark~dark@2x.png) | ![R-142,G-142,B-147](/images/com.apple.HIG/ios-accessible-systemgray2~dark@2x.png) | ![R-124,G-124,B-128](/images/com.apple.HIG/ios-accessible-systemgray2dark~dark@2x.png) |
| Gray (3) | [systemGray3](../uikit/uicolor/systemgray3.md) | ![R-199,G-199,B-204](/images/com.apple.HIG/ios-default-systemgray3~dark@2x.png) | ![R-72,G-72,B-74](/images/com.apple.HIG/ios-default-systemgray3dark~dark@2x.png) | ![R-174,G-174,B-178](/images/com.apple.HIG/ios-accessible-systemgray3~dark@2x.png) | ![R-84,G-84,B-86](/images/com.apple.HIG/ios-accessible-systemgray3dark~dark@2x.png) |
| Gray (4) | [systemGray4](../uikit/uicolor/systemgray4.md) | ![R-209,G-209,B-214](/images/com.apple.HIG/ios-default-systemgray4~dark@2x.png) | ![R-58,G-58,B-60](/images/com.apple.HIG/ios-default-systemgray4dark~dark@2x.png) | ![R-188,G-188,B-192](/images/com.apple.HIG/ios-accessible-systemgray4~dark@2x.png) | ![R-68,G-68,B-70](/images/com.apple.HIG/ios-accessible-systemgray4dark~dark@2x.png) |
| Gray (5) | [systemGray5](../uikit/uicolor/systemgray5.md) | ![R-229,G-229,B-234](/images/com.apple.HIG/ios-default-systemgray5~dark@2x.png) | ![R-44,G-44,B-46](/images/com.apple.HIG/ios-default-systemgray5dark~dark@2x.png) | ![R-216,G-216,B-220](/images/com.apple.HIG/ios-accessible-systemgray5~dark@2x.png) | ![R-54,G-54,B-56](/images/com.apple.HIG/ios-accessible-systemgray5dark~dark@2x.png) |
| Gray (6) | [systemGray6](../uikit/uicolor/systemgray6.md) | ![R-242,G-242,B-247](/images/com.apple.HIG/ios-default-systemgray6~dark@2x.png) | ![R-28,G-28,B-30](/images/com.apple.HIG/ios-default-systemgray6dark~dark@2x.png) | ![R-235,G-235,B-240](/images/com.apple.HIG/ios-accessible-systemgray6~dark@2x.png) | ![R-36,G-36,B-38](/images/com.apple.HIG/ios-accessible-systemgray6dark~dark@2x.png) |

In SwiftUI, the equivalent of `systemGray` is [gray](../swiftui/color/gray.md).

## Resources

#### Related
[Dark Mode](dark-mode.md)
[Accessibility](accessibility.md)
[Materials](materials.md)
[Apple Design Resources](https://developer.apple.com/design/resources/)

#### Developer documentation
[Color](../swiftui/color.md) — SwiftUI
[UIColor](../uikit/uicolor.md) — UIKit
[Color](../appkit/color.md) — AppKit

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
