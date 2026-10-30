---
url: https://developer.apple.com/design/human-interface-guidelines/pointing-devices
framework: HIG
---

# Pointing devices

**Type:** article

**Platforms:** ios, ipados, macos, visionos

> **Updated 2026-10-28:** Added guidance for revealing hidden controls with touch on Mac, and updated guidance and artwork for iPadOS and macOS.

People can use a pointing device like a trackpad or mouse to navigate the interface and initiate actions.

![A sketch of an arrow-shaped pointer, suggesting use of a mouse or trackpad. The image is overlaid with rectangular and circular grid lines and is tinted purple to subtly reflect the purple in the original six-color Apple logo.](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-pointing-devices-intro@2x.png)

People appreciate the precision and flexibility that pointing devices offer. On a Mac, people typically expect to combine a pointing device with a keyboard as they navigate apps and the system. On iPad and Apple Vision Pro, a pointing device gives people an additional way to interact with apps and content, without replacing touch, eyes, or gestures.

## Best practices
**Be consistent when responding to mouse and trackpad gestures.** People expect most gestures to work the same throughout the system, regardless of the app or game they’re using. On a Mac, for example, people rely on the “Swipe between pages” gesture to behave the same way whether they’re browsing individual document pages, webpages, or images.

**Avoid redefining systemwide trackpad gestures.** Even in a game that uses app-specific gestures in a custom way, people expect systemwide gestures to be available; for example, people expect to make familiar gestures to reveal the Dock or Mission Control in macOS. Remember that Mac users can customize the gestures for performing systemwide actions.

**Provide a consistent experience in your app, whether people are using gestures, eyes, a pointing device, or a keyboard.** People expect to move fluidly between multiple types of input, and they don’t want to learn different interactions for each mode or for each app they use.

**Let people use the pointer to reveal and hide controls that automatically minimize or fade out.** In iPadOS, for example, people can reveal the minimized Safari toolbar by holding the pointer over it (the toolbar minimizes again when the pointer moves away). People can also move the pointer to reveal or hide playback controls while they watch a full-screen video.

**Provide a consistent experience when people press and hold a modifier key while interacting with objects in your app.** For example, if people can duplicate an object by pressing and holding the Option key while they drag that object, ensure the result is the same whether they drag using touch or the pointer.

## Platform considerations
*No additional considerations for iOS. Not supported in tvOS or watchOS.*

### iPadOS
iPadOS builds on the traditional pointer experience, automatically adapting the pointer to the current context and providing rich visual feedback at a level of precision that enhances productivity and simplifies common tasks on a touchscreen device. The iPadOS pointing system gives people an additional way to interact with apps and content — it doesn’t replace touch.

**Allow multiple selection in custom views when necessary.** When someone clicks and drags the pointer over multiple items to select them, the pointer expands into a visible rectangle that encompasses the selection. Standard nonlist collection views support this interaction by default; if you want to support multiple selection in custom views, you need to implement it yourself. For developer guidance, see [UIBandSelectionInteraction](../UIKit/uibandselectioninteraction.md).

**Distinguish between pointer and finger input only if it provides value.** For example, a scrubber can give people an additional way to target a location in a video when they’re using the pointer. In this scenario, people can drag the playhead using either the pointer or touch, but they can use the pointer to click a precise seek destination.

#### Pointer shape and content effects
iPadOS integrates the appearance and behavior of both the pointer and the element it moves over, bringing focus to the item the pointer is targeting. You can support the system-provided pointer effects or modify them to suit your experience.

By default, the pointer’s shape is an arrow, but it can display a system-defined or custom shape when people move it over specific elements or regions. For example, the pointer automatically uses the familiar I-beam shape when people move it over a text-entry area.

With a *content effect*, the UI element or region beneath the pointer can also change its appearance when people hold the pointer over it. iPadOS defines three content effects that bring focus to different types of interactive elements in your app: highlight, lift, and hover.

The *highlight effect* materializes a Liquid Glass shape between the pointer and the control it’s moving over. The subtle highlighting and movement bring focus to the control without distracting people from their task. By default, iPadOS applies the highlight effect to bar buttons, tab bars, segmented controls, and edit menus.

The *lift effect* combines a subtle parallax with the appearance of elevation to make an element seem like it’s floating above the screen. When the pointer is over the element, iPadOS creates the illusion of lift by scaling the element up while adding a shadow below it and a soft specular highlight on top of it. By default, iPadOS applies the lift effect to standalone Liquid Glass controls, app icons, and buttons in Control Center.

*Hover* is a generic effect that lets you apply custom scale, tint, or shadow values to an element as the pointer moves over it. The hover effect combines your custom values to bring focus to an item, but it doesn’t transform the default pointer shape.

#### Pointer accessories
Pointer accessories are visual indicators that help people understand how they can use the pointer to interact with the current UI element. For example, a pointer approaching a resizable element might display small arrows to indicate that the element allows resizing along a certain axis.

Unlike pointer shapes and content effects, accessories are secondary items that can combine with any pointer to communicate additional information. For developer guidance, see [UIPointerAccessory](../UIKit/uipointeraccessory.md).

**Use clear, simple images to create custom accessories.** A pointer accessory is small, so it’s essential to create an image that communicates the pointer interaction without using too many details.

**Consider using the accessory transition to signal a change in an element’s state or behavior.** In addition to animating the appearance and disappearance of pointer accessories, the system also animates the transitions among accessory shapes and positions that can accompany content effects. For example, you could communicate that an add action has become unavailable by transitioning the pointer accessory from the `plus` symbol to the `circle.slash` symbol.

#### Standard pointers and effects
**When possible, support the system-provided content effects.** People quickly become accustomed to the content effects they see throughout the system and generally expect their experience to apply to every app they use. To provide a consistent user experience, align your interactions with the design intent of each effect. Specifically:

- Use highlight for a group of controls placed within a Liquid Glass container.
- Use lift for a standalone Liquid Glass control or a small element that has an opaque background.
- Use hover for large elements and customize the scale, tint, and shadow attributes as needed (for guidance, see [Customizing pointers](pointing-devices.md#Customizing-pointers)).

**Prefer the system-provided pointer appearances for standard buttons and text-entry areas.** You can help people feel more comfortable with your app when the pointer behaves in ways they expect.

**Add padding around interactive elements to create comfortable hit regions.** You might need to experiment to determine the right size for an element’s hit region. If the hit region is too small, it can make people feel that they have to be extra precise when interacting with the element. On the other hand, when an element’s hit region is too large, people can feel that it takes a lot of effort to pull the pointer away from the element. In general, it works well to add about 12 points of padding around elements that include a bezel; for elements without a bezel, it works well to add about 24 points of padding around the element’s visible edges.

![An illustration of a button that's centered on top of a shaded rectangle that extends beyond the button by the same distance on all sides. Centered on each side, a callout indicates that the padding between the button and each edge of the shaded rectangle is 12 points.](https://developer.apple.com/tutorials/images/com.apple.HIG/padding-for-button-with-bezel@2x.png)

![An illustration of a symbol centered on top of a shaded rectangle that extends beyond the symbol by the same distance on all sides. Centered on each side, a callout indicates that the padding between the symbol and each edge of the shaded rectangle is 24 points.](https://developer.apple.com/tutorials/images/com.apple.HIG/padding-for-glyph@2x.png)

![An illustration of a button without a bezel, centered on top of a shaded rectangle that extends beyond the button by the same distance on all sides. Centered on each side, a callout indicates that the padding between the button and each edge of the shaded rectangle is 24 points.](https://developer.apple.com/tutorials/images/com.apple.HIG/padding-for-button-without-bezel@2x.png)

**Create contiguous hit regions for custom bar buttons.** If there’s space between the hit regions of adjacent buttons in a bar, people may experience a distracting motion when the highlight shape briefly disappears as the pointer moves between buttons.

#### Customizing pointers
**Prefer system-provided pointer effects for custom elements that behave like standard elements.** When a custom element behaves like a standard one, people generally expect to interact with it using familiar pointer interactions. For example, if buttons in a custom toolbar don’t use the standard highlight effect, people might think they’re broken.

**Use pointer effects in consistent ways throughout your app.** For example, if your app helps people draw, provide a similar pointer experience for every drawing area in your app so that people can apply the knowledge they gain in one area to the others.

**Avoid creating gratuitous pointer and content effects.** People notice when the appearance of the pointer or the UI element beneath it changes, and they expect the changes to be useful. Creating a purely decorative pointer effect can distract and even irritate people without providing any practical value.

**Keep custom pointer shapes simple.** Ideally, the pointer’s shape signals the action people can take in the current context without drawing too much attention to itself. If people don’t instantly understand your custom pointer shape, they’re likely to waste time trying to discover what the shape means.

**Consider enhancing the pointer experience by displaying custom annotations that provide useful information.** For example, you could display X and Y values when people hold the pointer over a graphing area in your app. Keynote uses annotations to display the current width and height of a resizable image.

![An illustration of a custom pointer hovering over a resize handle on the edge of a shaded rectangle. Above the pointer is a small annotation that displays the image’s width and height values against a dark background.](https://developer.apple.com/tutorials/images/com.apple.HIG/useful-pointer-annotation@2x.png)

**Avoid displaying instructional text with a pointer.** A pointer that displays instructional text can make an app seem complicated and difficult to use. Instead of providing instructions, prioritize clarity and simplicity in your interface, so that people can quickly grasp how to use your app whether they’re using the pointer or touching the screen.

**Consider the interplay of shadow, scale, and element spacing when defining custom hover effects.** In general, reserve scaling for elements that can increase in size without crowding nearby elements. For example, scaling doesn’t work well for a table row because a row can’t expand without overlapping adjacent rows. For an element that has little space around it, consider using a hover effect that includes tint, but not scale and shadow. Note that it doesn’t work well to use shadow without including scale, because an unscaled element doesn’t appear to get closer to the viewer even when its shadow implies that it’s elevated above the screen.

### macOS
macOS supports a wide range of standard mouse and trackpad interactions that people can customize. For example, when a click or gesture isn’t a primary way to interact with content, people can often turn it on or off based on their current workflow. People can also choose specific regions of a mouse or trackpad to invoke secondary clicks, and select specific finger combinations and movements for certain gestures.

| Click or gesture | Expected behavior | Mouse | Trackpad |
| --- | --- | --- | --- |
| Primary click | Select or activate an item, such as a file or button. | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Secondary click | Reveal context menus. | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Scrolling | Move content up, down, left, or right within a view. | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Smart zoom | Zoom in or out on content, such as a web page or PDF. | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Swipe between pages | Navigate forward or backward between individually displayed pages. | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Swipe between full-screen apps | Navigate forward or backward between full-screen apps and spaces. | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Mission Control (double-tap the mouse with two fingers or swipe up on the trackpad with three or four fingers) | Activate Mission Control. | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Lookup and data detectors (force click with one finger or tap with three fingers) | Display a lookup window above selected content. |  | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Tap to click | Perform the primary click action using a tap rather than a click. |  | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Force click | Click then press firmly to display a Quick Look window or lookup window above selected content. Apply a variable amount of pressure to affect pressure-sensitive controls, such as variable speed media controls. |  | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Zoom in or out (pinch with two fingers) | Zoom in or out. |  | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Rotate (move two fingers in a circular motion) | Rotate content, such as an image. |  | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Notification Center (swipe from the edge of the trackpad) | Display Notification Center. |  | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| App Exposé (swipe down with three or four fingers) | Display the current app’s windows in Exposé. |  | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Apps (pinch with thumb and three fingers) | Display the list of apps. |  | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Show Desktop (spread with thumb and three fingers) | Slide all windows out of the way to reveal the desktop. |  | ![A checkmark denoting availability.](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png) |

#### Pointers
macOS offers a variety of standard pointer styles, which your app can use to communicate the interactive state of an interface element or the result of a drag operation.

| Pointer | Name | Meaning | APIs |
| --- | --- | --- | --- |
| ![A pointer that resembles a diagonal arrow pointing up and to the left.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-default@2x.png) | Arrow | Standard pointer for selecting and interacting with content and interface elements. | AppKit: [arrow](../AppKit/nscursor/arrow.md), SwiftUI: [default](../SwiftUI/pointerstyle/default.md) |
| ![A closed hand.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-closed-hand@2x.png) | Closed hand | Dragging to reposition content within a view. | AppKit: [closedHand](../AppKit/nscursor/closedhand.md), SwiftUI: [grabActive](../SwiftUI/pointerstyle/grabactive.md) |
| ![A pointer arrow with a small rounded rectangle that resembles a menu below and to the right of the arrow.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-contextual-menu@2x.png) | Context menu | A context menu is available for the content below the pointer. This pointer is generally shown only when the Control key is pressed. | AppKit: [contextualMenu](../AppKit/nscursor/contextualmenu.md) |
| ![A plus symbol.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-crosshair@2x.png) | Cross | Precise rectangular selection is possible, such as when viewing an image in Preview. | AppKit: [crosshair](../AppKit/nscursor/crosshair.md), SwiftUI: [rectSelection](../SwiftUI/pointerstyle/rectselection.md) |
| ![A small pointer arrowhead with a circle underneath; the circle contains an X.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-disappearing-item@2x.png) | Disappearing item | A dragged item will disappear when dropped. If the item references an original item, the original is unaffected. For example, when dragging a mailbox out of the favorites bar in Mail, the original mailbox isn’t removed. | AppKit: [disappearingItem](../AppKit/nscursor/disappearingitem.md) |
| ![A small pointer arrowhead with a circle underneath; the circle contains a plus symbol.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-drag-copy@2x.png) | Drag copy | Duplicates a dragged—not moved—item when dropped into the destination. Appears when pressing the Option key during a drag operation. | AppKit: [dragCopy](../AppKit/nscursor/dragcopy.md) |
| ![A curved arrow, pointing up and to the right.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-drag-link@2x.png) | Drag link | During a drag and drop operation, creates an alias of the selected file when dropped. The alias points to the original file, which remains unmoved. Appears when pressing the Option and Command keys during a drag operation. | AppKit: [dragLink](../AppKit/nscursor/draglink.md) |
| ![Opposing vertical braces, used to form an insertion marker.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-horizontal-i-beam@2x.png) | Horizontal I beam | Selection and insertion of text is possible in a horizontal layout, such as a TextEdit or Pages document. | AppKit: [iBeam](../AppKit/nscursor/ibeam.md), SwiftUI: [horizontalText](../SwiftUI/pointerstyle/horizontaltext.md) |
| ![An open hand.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-open-hand@2x.png) | Open hand | Dragging to reposition content within a view is possible. | AppKit: [openHand](../AppKit/nscursor/openhand.md), SwiftUI: [grabIdle](../SwiftUI/pointerstyle/grabidle.md) |
| ![A small pointer arrowhead with a do not enter symbol underneath.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-operation-not-allowed@2x.png) | Operation not allowed | A dragged item can’t be dropped in the current location. | AppKit: [operationNotAllowed](../AppKit/nscursor/operationnotallowed.md) |
| ![A hand with the index finger extended.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-pointing-hand@2x.png) | Pointing hand | The content beneath the pointer is a URL link to a webpage, document, or other item. | AppKit: [pointingHand](../AppKit/nscursor/pointinghand.md), SwiftUI: [link](../SwiftUI/pointerstyle/link.md) |
| ![A horizontal bar with a downward-pointing arrow at its midpoint.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-down@2x.png) | Resize down | A horizontal divider can move only downward. | AppKit: [rowResize(directions:)](../AppKit/nscursor/rowresize%28directions%29.md), SwiftUI: [rowResize(directions:)](../SwiftUI/pointerstyle/rowresize%28directions%29.md) |
| ![Two triangles side by side, one pointing left in gray and one pointing right in black.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-east@2x.png) | Resize east | Resize a window or other rectangular frame only by moving an edge to the right, such as when it has reached its minimum or maximum width. | AppKit: [frameResize(position:directions:)](../AppKit/nscursor/frameresize%28position,directions%29.md), SwiftUI: [frameResize(position:directions:)](../SwiftUI/pointerstyle/frameresize%28position,directions%29.md) |
| ![Two black triangles side by side, one pointing left and one pointing right.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-east-west@2x.png) | Resize east west | Resize a window or other rectangular frame by dragging its left or right edge in either direction. | AppKit: [frameResize(position:directions:)](../AppKit/nscursor/frameresize%28position,directions%29.md), SwiftUI: [frameResize(position:directions:)](../SwiftUI/pointerstyle/frameresize%28position,directions%29.md) |
| ![A vertical bar with a left-pointing arrow at its midpoint.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-left@2x.png) | Resize left | A vertical divider can move only to the left. | AppKit: [columnResize(directions:)](../AppKit/nscursor/columnresize%28directions%29.md), SwiftUI: [columnResize(directions:)](../SwiftUI/pointerstyle/columnresize%28directions%29.md) |
| ![A vertical bar with left- and right-pointing arrows extending from its midpoint.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-left-right@2x.png) | Resize left right | Resize a column by dragging a vertical divider in either direction. | AppKit: [columnResize](../AppKit/nscursor/columnresize.md), [columnResize(directions:)](../AppKit/nscursor/columnresize%28directions%29.md); SwiftUI: [columnResize](../SwiftUI/pointerstyle/columnresize.md), [columnResize(directions:)](../SwiftUI/pointerstyle/columnresize%28directions%29.md) |
| ![Two triangles stacked vertically, one pointing up in black and one pointing down in gray.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-north@2x.png) | Resize north | Resize a window or other rectangular frame only by moving an edge upward, such as when it has reached its minimum or maximum height. | AppKit: [frameResize(position:directions:)](../AppKit/nscursor/frameresize%28position,directions%29.md), SwiftUI: [frameResize(position:directions:)](../SwiftUI/pointerstyle/frameresize%28position,directions%29.md) |
| ![Two black triangles stacked vertically, one pointing up and one pointing down.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-north-south@2x.png) | Resize north south | Resize a window or other rectangular frame by dragging its top or bottom edge in either direction. | AppKit: [frameResize(position:directions:)](../AppKit/nscursor/frameresize%28position,directions%29.md), SwiftUI: [frameResize(position:directions:)](../SwiftUI/pointerstyle/frameresize%28position,directions%29.md) |
| ![Two triangles along a diagonal from the bottom left to the top right; the top-right triangle is black and the bottom-left triangle is gray.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-northeast@2x.png) | Resize northeast | Resize a window or other rectangular frame only by moving a corner toward the top right, such as when it has reached its minimum or maximum size. | AppKit: [frameResize(position:directions:)](../AppKit/nscursor/frameresize%28position,directions%29.md), SwiftUI: [frameResize(position:directions:)](../SwiftUI/pointerstyle/frameresize%28position,directions%29.md) |
| ![Two black triangles along a diagonal that runs from the bottom left to the top right.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-northeast-southwest@2x.png) | Resize northeast southwest | Resize a window or other rectangular frame by dragging its top-right or bottom-left corner in either direction. | AppKit: [frameResize(position:directions:)](../AppKit/nscursor/frameresize%28position,directions%29.md), SwiftUI: [frameResize(position:directions:)](../SwiftUI/pointerstyle/frameresize%28position,directions%29.md) |
| ![Two triangles along a diagonal from the top left to the bottom right; the top-left triangle is black and the bottom-right triangle is gray.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-northwest@2x.png) | Resize northwest | Resize a window or other rectangular frame only by moving a corner toward the top left, such as when it has reached its minimum or maximum size. | AppKit: [frameResize(position:directions:)](../AppKit/nscursor/frameresize%28position,directions%29.md), SwiftUI: [frameResize(position:directions:)](../SwiftUI/pointerstyle/frameresize%28position,directions%29.md) |
| ![Two black triangles along a diagonal that runs from the top left to the bottom right.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-northwest-southeast@2x.png) | Resize northwest southeast | Resize a window or other rectangular frame by dragging its top-left or bottom-right corner in either direction. | AppKit: [frameResize(position:directions:)](../AppKit/nscursor/frameresize%28position,directions%29.md), SwiftUI: [frameResize(position:directions:)](../SwiftUI/pointerstyle/frameresize%28position,directions%29.md) |
| ![A vertical bar with a right-pointing arrow at its midpoint.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-right@2x.png) | Resize right | A vertical divider can move only to the right. | AppKit: [columnResize(directions:)](../AppKit/nscursor/columnresize%28directions%29.md), SwiftUI: [columnResize(directions:)](../SwiftUI/pointerstyle/columnresize%28directions%29.md) |
| ![Two triangles stacked vertically, one pointing up in gray and one pointing down in black.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-south@2x.png) | Resize south | Resize a window or other rectangular frame only by moving an edge downward, such as when it has reached its minimum or maximum height. | AppKit: [frameResize(position:directions:)](../AppKit/nscursor/frameresize%28position,directions%29.md), SwiftUI: [frameResize(position:directions:)](../SwiftUI/pointerstyle/frameresize%28position,directions%29.md) |
| ![Two triangles along a diagonal from the top left to the bottom right; the bottom-right triangle is black and the top-left triangle is gray.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-southeast@2x.png) | Resize southeast | Resize a window or other rectangular frame only by moving a corner toward the bottom right, such as when it has reached its minimum or maximum size. | AppKit: [frameResize(position:directions:)](../AppKit/nscursor/frameresize%28position,directions%29.md), SwiftUI: [frameResize(position:directions:)](../SwiftUI/pointerstyle/frameresize%28position,directions%29.md) |
| ![Two triangles along a diagonal from the bottom left to the top right; the bottom-left triangle is black and the top-right triangle is gray.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-southwest@2x.png) | Resize southwest | Resize a window or other rectangular frame only by moving a corner toward the bottom left, such as when it has reached its minimum or maximum size. | AppKit: [frameResize(position:directions:)](../AppKit/nscursor/frameresize%28position,directions%29.md), SwiftUI: [frameResize(position:directions:)](../SwiftUI/pointerstyle/frameresize%28position,directions%29.md) |
| ![A horizontal bar with an up-pointing arrow at its midpoint.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-up@2x.png) | Resize up | A horizontal divider can move only upward. | AppKit: [rowResize(directions:)](../AppKit/nscursor/rowresize%28directions%29.md), SwiftUI: [rowResize(directions:)](../SwiftUI/pointerstyle/rowresize%28directions%29.md) |
| ![A horizontal bar with up- and down-pointing arrows extending from its midpoint.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-up-down@2x.png) | Resize up down | Resize a row by dragging a horizontal divider in either direction. | AppKit: [rowResize](../AppKit/nscursor/rowresize.md), [rowResize(directions:)](../AppKit/nscursor/rowresize%28directions%29.md); SwiftUI: [rowResize](../SwiftUI/pointerstyle/rowresize.md), [rowResize(directions:)](../SwiftUI/pointerstyle/rowresize%28directions%29.md) |
| ![Two triangles side by side, one pointing left in black and one pointing right in gray.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-west@2x.png) | Resize west | Resize a window or other rectangular frame only by moving an edge to the left, such as when it has reached its minimum or maximum width. | AppKit: [frameResize(position:directions:)](../AppKit/nscursor/frameresize%28position,directions%29.md), SwiftUI: [frameResize(position:directions:)](../SwiftUI/pointerstyle/frameresize%28position,directions%29.md) |
| ![Opposing horizontal braces, used to form an insertion marker.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-vertical-i-beam@2x.png) | Vertical I beam | Selection and insertion of text is possible in a vertical layout. | AppKit: [iBeamCursorForVerticalLayout](../AppKit/nscursor/ibeamcursorforverticallayout.md), SwiftUI: [verticalText](../SwiftUI/pointerstyle/verticaltext.md) |
| ![A magnifying glass with a plus symbol inside the lens.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-zoom-in@2x.png) | Zoom in | Zoom in on (magnify) a canvas or object. | AppKit: [zoomIn](../AppKit/nscursor/zoomin.md), SwiftUI: [zoomIn](../SwiftUI/pointerstyle/zoomin.md) |
| ![A magnifying glass with a minus symbol inside the lens.](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-zoom-out@2x.png) | Zoom out | Zoom out of a canvas or object. | AppKit: [zoomOut](../AppKit/nscursor/zoomout.md), SwiftUI: [zoomOut](../SwiftUI/pointerstyle/zoomout.md) |

#### Touch support for hidden controls
Some Mac apps reveal certain controls only when the pointer moves over them. These controls need another way to appear when someone uses touch on a Mac that supports it. For related guidance, see [Gestures](gestures.md).

**Decide which hidden controls need touch support.** Reserve touch support for essential controls. In general, don’t add touch support for features that display static information, like tooltips, or for features people can already use another way with touch. For example, someone can swipe to scroll a carousel, so there’s no need to reveal the navigation buttons that exist for mice without a scroll wheel. Avoid keeping hidden controls visible all the time just to accommodate touch.

**Reveal a hidden control when someone taps its general location on a touch display.** Reveal only controls relevant to the content someone is working with; too many at once can overwhelm and distract people. Hide a control again when the person finishes with it, or after a few seconds if they don’t use it. Sidebars and the close button in a tabbed window are exceptions; see the guidance below.

**Retain the current selection when revealing a hidden control.** In a view that supports selection, keep the current selection when someone taps the area of a hidden control to reveal it, and when they then tap the revealed control. The control might act on the selection, and changing it would force people to select again.

**Make essential hidden controls available in a context menu.** A context menu gives people a dependable way to reach a control without finding the spot where it appears. Include the controls people need most, and keep the menu short. Someone who uses touch can open a context menu with a touch and hold. For guidance, see [Context menus](context-menus.md).

**In a sidebar, reveal hidden controls when someone taps the corresponding section header or row.** A tap performs the same action as a click, like expanding or collapsing a section or selecting a row. For example, tapping the Favorites header in the Finder sidebar collapses the section and reveals a disclosure button. Reveal only the controls for the tapped item, and keep them visible until touch moves outside the sidebar or someone uses a pointing device again. If someone taps the area of a hidden control, reveal the control without activating it. The control acts only when they tap it again.

**In a tabbed window, reveal the selected tab’s close button when someone taps anywhere in the window.** Keep the button visible until they resume using a pointing device. If someone closes the selected tab while still using touch, show the close button on the newly selected tab.

### visionOS
In visionOS, people can attach an external pointing device or keyboard, and use both devices while they continue to use their eyes and hands. If people look at an element and then move the pointer, the system brings focus to the element under the pointer. Your app doesn’t have to do anything to support this behavior.

When a pointing device is attached, the area people are looking at determines the pointer’s context. For example, when people shift their eyes from one window to another, the pointer’s context seamlessly transitions to the new window.

[Video: A recording that shows a pointer moving around, highlighting items, and scrolling content within a Safari window in visionOS. A picture-in-picture window is visible in the bottom left corner of the recording. It shows a person's hand operating a trackpad next to a keyboard outside the field of view. The person's gestures on the trackpad correspond to the pointer movements.](https://developer.apple.com/tutorials/videos/com.apple.HIG/visionos-trackpad-pointer-input.mp4)

When people use an attached pointing device that supports gestures, like a trackpad or mouse, the pointer hides while people are gesturing, minimizing visual distraction. In this scenario, the pointer remains hidden until people move it, when it reappears in the location they’re looking at.

## Resources

#### Related
[Entering data](entering-data.md)

[Keyboards](keyboards.md)

#### Developer documentation
[Input events](../SwiftUI/input-events.md) — SwiftUI

[Pointer interactions](../UIKit/pointer-interactions.md) — UIKit

[Mouse, Keyboard, and Trackpad](../AppKit/mouse-keyboard-and-trackpad.md) — AppKit

## Change log
| Date | Changes |
| --- | --- |
| October 28, 2026 | Added guidance for revealing hidden controls with touch on Mac, and updated guidance and artwork for iPadOS and macOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |

---
*Source: [https://developer.apple.com/design/human-interface-guidelines/pointing-devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)*
