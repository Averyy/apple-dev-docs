# Building complications with SwiftUI

**Framework**: ClockKit

Design the appearance of a graphic complication using SwiftUI.

#### Overview

ClockKit provides SwiftUI templates for all of the graphic complication families. These templates use a [`View`](https://developer.apple.com/documentation/SwiftUI/View) instance to define some or all of the complication’s content. To access these templates, import both ClockKit and SwiftUI.

```swift
import ClockKit
import SwiftUI
```

ClockKit provides a variety of templates for each family. Many of these mix SwiftUI views with other data providers. However, some templates take only a single SwiftUI view.

- [`CLKComplicationTemplateGraphicCircularView`](clkcomplicationtemplategraphiccircularview.md)
- [`CLKComplicationTemplateGraphicRectangularFullView`](clkcomplicationtemplategraphicrectangularfullview.md)
- [`CLKComplicationTemplateGraphicExtraLargeCircularView`](clkcomplicationtemplategraphicextralargecircularview.md)

These templates provide a blank canvas that you can use to draw the entire complication.

##### Present a View

ClockKit varies the SwiftUI view’s size based on the template. The SwiftUI template replaces a full color image provider with a SwiftUI view. The view has the same dimensions as the corresponding image.

Also, the template may mask the SwiftUI view to a circle or apply a corner radius to the view, just as it does for the full color images. In particular, the [`CLKComplicationTemplateGraphicRectangularFullView`](clkcomplicationtemplategraphicrectangularfullview.md) template provides the full graphic rectangular complication as a single SwiftUI view. This view is 162 pt x 69 pt on the 40 mm Apple Watch, and 184 pt x 78 pt on the 44 mm watch, but the template provides a safe area inset to help you avoid clipping your content. Use the [`edgesIgnoringSafeArea(_:)`](https://developer.apple.com/documentation/SwiftUI/View/edgesIgnoringSafeArea(_:)) modifier, if you need to fill the complication to the edges.

![An illustration showing a graph drawn using the rectangular full-view template.](https://docs-assets.developer.apple.com/published/acd6832a230be836af2d31f4adf36337/media-3683203%402x.png)

For additional details, see each template’s class reference document.

##### Design a View

Use SwiftUI static views, such as text, shapes, or images, to create your complication’s content. You can also add render effects like blurs and gradients, but keep in mind that complications only have one or two frames in which to render the effect.

Because complications show a snapshot of the apps data at a particular point in time, they don’t support features like animation. Additionally, if the user touches your complication, the system launches your app instead of passing the touch event to the SwiftUI views, so a complication can’t use interactive elements like buttons or switches.

##### Support Tinted Views

Some watch faces let the user select a tint color that affects how the face displays graphical complications. Some watch faces use a complex set of colors; for example, the Solar Dial face sets both a foreground and background color, and the colors change based on the time of day.

By default, when ClockKit displays your complication on a tinted watch face, it desaturates your SwiftUI view to create a grayscale version. For some faces, like the California face, it then applies a single tint color to the desaturated view.

To control how the system tints your view, divide your view hierarchy into two layers, a foreground layer and the background layer. ClockKit looks at the opacity of each layer when applying the tint.

For most watch faces, ClockKit applies the user-selected tint color to one layer, and a system-defined color to the other. For example, the Infograph watch face applies white to the background and the user-selected tint to the foreground. However, the foreground and background colors can change from face to face. in the X-Large watch face, ClockKit applies white to the foreground, and the tint color to the background. On other faces, like Solar Dial, it applies system-defined colors to both layers.

![Two watch faces. The first face displays a tinted circular graphic template in the upper left corner as a red icon on a white background. The second face displays the extra-large version of that template in the center of the screen with a white icon on a red background.](https://docs-assets.developer.apple.com/published/7dd0c57b64844500c2ab6376343e33ef/media-3666656%402x.png)

To divide your view into layers, add the [`complicationForeground()`](https://developer.apple.com/documentation/SwiftUI/View/complicationForeground()) modifier to part of your view hierarchy. That view and all of its subviews become the foreground layer. Everything else is in the background layer.

```swift
ZStack {
    Rectangle()
        .fill(Color.purple)
    Image("coffee_template")
        .renderingMode(.template)
        .resizable()
        .aspectRatio(contentMode: .fit)
        .foregroundColor(.yellow)
        .complicationForeground()
}
```

![An image of two watch faces with an extra-large circular complication. The first face displays the full-color version, while the second displays the tinted version.](https://docs-assets.developer.apple.com/published/72c68d04d89f5bcdbf64fef840e0f04b/media-3666654%402x.png)

For even greater control, you can check the complication’s rendering mode, and then change the design based on whether the system displays the face in a full color or a tinted mode. You can access the current [`ComplicationRenderingMode`](complicationrenderingmode.md) value from the [`Environment`](https://developer.apple.com/documentation/SwiftUI/Environment).

```swift
@Environment(\.complicationRenderingMode) var renderingMode

var body: some View {
    ZStack {
        
        if renderingMode == .fullColor {
            Circle()
                .fill(Color.purple)
        } else {
            Circle()
                .fill(LinearGradient(
                        gradient: Gradient(
                            colors: [Color.white.opacity(0.3),
                                     Color.white.opacity(1.0)]),
                        startPoint: .top,
                        endPoint: .bottom))
        }
        
        Image("coffee_template")
            .renderingMode(.template)
            .resizable()
            .aspectRatio(contentMode: .fit)
            .foregroundColor(.yellow)
            .complicationForeground()
    }
}
```

In this example, if the system renders the watch face in [`ComplicationRenderingMode.fullColor`](complicationrenderingmode/fullcolor.md) mode, it uses a solid blue circle as the background. However, if the system renders the face in [`ComplicationRenderingMode.tinted`](complicationrenderingmode/tinted.md) mode, it uses a gradient fill. For a tinted complication, the selected color has no effect; the system only looks at the opacity, and then applies its own color.

![An image of two watch faces with an extra-large circular complication. The first face displays the full-color version, while the second displays the tinted version with a gradient fill.](https://docs-assets.developer.apple.com/published/8f42c390bf5d10537538cd2340933901/media-3666655%402x.png)

##### Preview the Complication

Like other SwiftUI views, you can preview your complications as you design them. To enable previews:

1. Add a [`PreviewProvider`](https://developer.apple.com/documentation/SwiftUI/PreviewProvider) to the bottom of your complication controller’s file.
2. In the [`previews`](https://developer.apple.com/documentation/SwiftUI/PreviewProvider/previews-swift.type.property) property, instantiate your template, and call its `previewContext(faceColor:)` method.

Calling `previewContext()` with no argument defaults to a full-color watch face. To preview a tinted watch face, pass the desired tint color to the `faceColor` parameter. Use a `Group` to preview multiple complications at once.

```swift
struct ComplicationController_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            
            CLKComplicationTemplateGraphicExtraLargeCircularView(MyCoffeeView()).previewContext()
            
            CLKComplicationTemplateGraphicExtraLargeCircularView(MyCoffeeView()).previewContext(faceColor: .red)
        }
    }
}
```

![An image of two watch previews of an extra-large circular complication. The first preview displays the full-color version, while the second displays a red-tinted version.](https://docs-assets.developer.apple.com/published/8111333d80569f7f219ac5de2a4f1539/media-3666657%402x.png)

## See Also

- [Creating complications for your watchOS app](creating-complications-for-your-watchos-app.md)
  Set up and implement complications for your watchOS app.
- [Declaring complications for your app](declaring-complications-for-your-app.md)
  Define the complications that your app supports.
- [Creating a timeline entry](creating-a-timeline-entry.md)
  Package your app-specific data into a template and create a timeline entry for that template.
- [Loading future timeline events](loading-future-timeline-events.md)
  Preserve battery life and improve performance on the watch by providing a timeline with expected data and updates.
- [Keeping your complications up to date](keeping-your-complications-up-to-date.md)
  Replace or extend the data in your complication’s timeline.
- [Displaying progress views and gauges](displaying-progress-views-and-gauges.md)
  Add rich visual data to your SwiftUI complications with progress views and gauges.
- [Adding text to a complication](adding-text-to-a-complication.md)
  Use text in SwiftUI complications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/building-complications-with-swiftui)*