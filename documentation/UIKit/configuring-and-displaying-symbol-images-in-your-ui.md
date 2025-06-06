# Configuring and displaying symbol images in your UI

**Framework**: Uikit

Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.

#### Overview

Symbol images give you a consistent set of icons to use in your app, and ensure that those icons adapt to different sizes and to app-specific content. A symbol image contains a vector-based shape that scales without losing its sharpness. You generate its final appearance by applying a tint color, or if you’re using SF Symbols 2 or later, you can apply multiple colors to add depth and emphasis to your symbol. You use symbol images in places where you display a simple shape or glyph, such as a bar button item.

Although symbols are images, they support many traits you associate with text. In fact, several system symbol images include letters, numbers, or symbolic characters in their content. For example, the system provides symbol images for mathematical operators for addition, subtraction, multiplication, and division. You can also apply text-related traits to a symbol image to make it look like the surrounding text:

- Apply a font text style to a symbol image so that it matches text with the same style. Font text styles also cause symbol images to scale to match the current Dynamic Type setting.
- Apply weights, such as thin, heavy, or bold, to a symbol image.
- Scale and style symbol images to match the font you use for text.
- Align a symbol image with neighboring text by using the image’s baseline.

The system provides a collection of standard symbol images for you, including images for folders, the trash can, favorite items, and many more. Symbol images also adapt to the current trait environment, reducing the work required to support different sized interfaces. To browse the available symbol images, use the SF Symbols app, which you can download from [`Apple Design Resources`](https://developer.apple.comhttps://developer.apple.com/design/resources/).

You can also create symbol image files for your app’s custom iconography, as described in [`Creating custom symbol images for your app`](creating-custom-symbol-images-for-your-app.md).

##### Load a Symbol Image

When configuring an image view in a storyboard file, you browse the list of symbol image names in the Attribute inspector. When loading symbol images from your code, you look up the name for a symbol image using the SF Symbols app. For custom symbol images, create a Symbol Image Set asset in your asset catalog and load the asset by name.

Methods for loading symbol images are available across SwiftUI, UIKit, and AppKit. In each, you use certain methods when loading system images by name. When loading custom symbol images, you use a different set of methods. Each method looks only for its designated image type, which avoids namespace collisions between your custom images and the system images.

The following examples show how to load a system symbol and a custom symbol across frameworks.

In SwiftUI, you use `Image(systemName:)` to load a system symbol image and `Image(_:)` to load your custom symbol, as the following code shows:

```swift
// Create a system symbol image.
Image(systemName: "multiply.circle.fill")

// Create a custom symbol image using an asset in an asset catalog in Xcode.
Image("custom.multiply.circle")
```

In UIKit, a [`UIImage`](uiimage.md) object includes methods for loading the symbol image with specific traits or configuration options. When you load system symbol images, use [`init(systemName:)`](uiimage/init(systemname:).md), [`init(systemName:compatibleWith:)`](uiimage/init(systemname:compatiblewith:).md), or [`init(systemName:withConfiguration:)`](uiimage/init(systemname:withconfiguration:).md). When you load your custom symbol images from an asset catalog, use [`init(named:)`](uiimage/init(named:).md), [`init(named:in:compatibleWith:)`](uiimage/init(named:in:compatiblewith:).md), or [`init(named:in:with:)`](uiimage/init(named:in:with:).md).

```swift
// Create a system symbol image.
let image = UIImage(systemName: "multiply.circle.fill")                  

// Create a custom symbol image using an asset in an asset catalog in Xcode.
let image = UIImage(named: "custom.multiply.circle")
```

When you use AppKit, use [`init(systemSymbolName:accessibilityDescription:)`](https://developer.apple.com/documentation/AppKit/NSImage/init(systemSymbolName:accessibilityDescription:)) to load a system symbol image, and [`init(named:)`](https://developer.apple.com/documentation/AppKit/NSImage/init(named:)) to load your custom symbol image.

```swift
// Create a system symbol image with an accessibility description.
let image = NSImage(systemSymbolName: "multiply.circle.fill",
                    accessibilityDescription: "A multiply symbol inside a filled circle.")

// Create a custom symbol image using an asset in an asset catalog in Xcode.
let image = NSImage(named: "custom.multiply.circle")
```

##### Apply a Specific Appearance to a Symbol Image

UIKit and AppKit methods return an image object with symbol image information. When you display that symbol image in an image view, the system applies default styling to it. An image with the default styling might appear out of place next to bold text or text that uses the headline text style.

To make the symbol image blend in with the rest of your content, you create a [`UIImage.SymbolConfiguration`](uiimage/symbolconfiguration-swift.class.md) or [`NSImage.SymbolConfiguration`](https://developer.apple.com/documentation/AppKit/NSImage/SymbolConfiguration-swift.class) object with information about how to style the symbol image. Configure the object with the text style you use for neighboring labels and text views, or specify the font you use in those views. You can add weight information to give the symbol image a thinner or thicker appearance, and you can specify whether you want the image to appear slightly larger or smaller than the neighboring text.

In UIKit, you assign configuration data to the [`preferredSymbolConfiguration`](uiimageview/preferredsymbolconfiguration.md) property of the `UIImageView` that contains your symbol image. Typically, you apply configuration data only to image views. For other types of system views, UIKit provides configuration data based on system requirements. For example, bars configure the symbol images in their bar button items to match the bar’s configuration. The only other time you might use configuration data is when drawing the image directly. In that case, use the [`applying(_:)`](uiimage/configuration-swift.class/applying(_:).md) method to create a version of your image that includes the specified configuration data.

```swift
// Create a configuration object that the system initializes with two palette colors.
var config = UIImage.SymbolConfiguration(paletteColors: [.systemTeal, .systemGray5])

// Apply a configuration that scales to the system font point size of 42.
config = config.applying(UIImage.SymbolConfiguration(font: .systemFont(ofSize: 42.0)))

// Apply the configuration to an image view.
imageView.preferredSymbolConfiguration = config
```

If you’re using SwiftUI, there are several modifiers available to configure a symbol image, as the following code shows:

```swift
Image(systemName: "multiply.circle.fill")
      .foregroundStyle(.teal, .gray)
      .font(.system(size: 42.0))
```

In AppKit, you create a configuration object and set [`symbolConfiguration`](https://developer.apple.com/documentation/AppKit/NSImageView/symbolConfiguration) on [`NSImageView`](https://developer.apple.com/documentation/AppKit/NSImageView).

```swift
var configuration = NSImage.SymbolConfiguration(paletteColors: [.systemTeal, .systemGray])
configuration = config.applying(.init(textStyle: .title1))
imageView.symbolConfiguration = config
```

##### Update the Rendering Mode for a Symbol

SF Symbols contains four rendering modes: monochrome, palette, hierarchical, and multicolor. Symbols don’t have an intrinsic color, so by default, the system uses the tint color to render them. For example, the following code illustrates applying a tint color to an entire image:

```swift
// Create a system symbol image and apply a tint using SwiftUI.
Image(systemName: "multiply.circle.fill")
      .foregroundColor(.red)

// Create a symbol image with a tint using UIKit.
imageView.image = image?.withTintColor(.systemRed, renderingMode: .alwaysOriginal)
```

In SwiftUI, you set the rendering mode using [`symbolRenderingMode(_:)`](https://developer.apple.com/documentation/SwiftUI/Image/symbolRenderingMode(_:)), and apply colors using `foregroundStyle(_:)`. If a symbol doesn’t support the rendering mode you choose, the system uses the monochrome version. Using `foregroundStyle` with multiple colors implies switching to palette rendering mode, so you can omit setting the rendering mode.

```swift
// Create a system symbol image in palette rendering mode.
Image(systemName: "multiply.circle.fill")
      .foregroundStyle(.teal, .gray)
```

In UIKit and AppKit, you use a symbol configuration object to modify a symbol’s rendering mode. In AppKit, you apply a configuration using [`withSymbolConfiguration(_:)`](https://developer.apple.com/documentation/AppKit/NSImage/withSymbolConfiguration(_:)), whereas in UIKit, you apply a configuration by using [`applyingSymbolConfiguration(_:)`](uiimage/applyingsymbolconfiguration(_:).md), as the code below shows:

```swift
// Create an object configured for palette rendering mode.
let config = UIImage.SymbolConfiguration(paletteColors: [.systemTeal, .systemGray])

// Create a new symbol image using the configuration object.
imageView.image = image.applyingSymbolConfiguration(config)
```

Starting in iOS 16, symbols don’t automatically render in monochrome mode when you don’t specify a mode. For example, the system symbol “airpodsmax” defaults to hierarchical. If your app needs monochrome rendering for a symbol, use [`preferringMonochrome()`](uiimage/symbolconfiguration-swift.class/preferringmonochrome().md). To determine the default rendering mode for a symbol, find the symbol in the SF Symbols app and inspect the color sidebar.

##### Apply Variable Rendering

In iOS 16 and later, the system can dynamically apply colors to system and custom symbols using a percentage value to convey the strength or progress over time. For example, the following code creates a symbol of a speaker wave with two of the three bars highlighted:

```swift
// Create a system symbol image at 36% intensity.
let image = UIImage(systemName: "speaker.wave.3", variableValue: 0.36)
```

To use variable rendering in AppKit, see [`init(symbolName:variableValue:)`](https://developer.apple.com/documentation/AppKit/NSImage/init(symbolName:variableValue:)).

##### Update the Weight and Scale of a Symbol

There are nine symbol weights corresponding to a weight of the San Francisco system font, helping you achieve precise weight matching between symbols and adjacent text, while supporting flexibility for different sizes and context.

By specifying a scale, you adjust a symbol’s emphasis compared to adjacent text without disrupting the weight matching with text that uses the same point size.  See [`imageScale`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/imageScale) (SwiftUI), [`UIImage.SymbolScale`](uiimage/symbolscale.md) (UIKit), and [`NSImage.SymbolScale`](https://developer.apple.com/documentation/AppKit/NSImage/SymbolScale) (AppKit).

```swift
// Create a large scaled symbol image using SwiftUI.
Image(systemName: "multiply.circle.fill")
      .imageScale(.large)

// Create a large scaled symbol image using UIKit.
var config = UIImage.SymbolConfiguration(scale: .large)
imageView.image = image.withSymbolConfiguration(config)

// Create a large scaled symbol image using AppKit.
var config = NSImage.SymbolConfiguration(scale: .large)
imageView.image = image.withSymbolConfiguration(config)
```

##### Apply a Symbol Image Variant

SF Symbols defines design variants — such as outline, fill, slash, and enclosed — to help you communicate precise states and actions, while maintaining visual consistency and simplicity in your UI. For example, you might use the slash variant to show that an action is unavailable, or use the fill variant to indicate when the user selects something.

> **Note**:  If a variant doesn’t exist for a symbol, the system uses the base symbol. For example, tab bars in iOS default to using a fill variant, so choosing a symbol without a fill variant uses the original symbol.

In SwiftUI, you use the modifier `symbolVariant(_:)` to apply a variant. Search the SF Symbols app to find the variants the multiply symbol supports, such as `circle`, `circle.fill`, `square`, and `square.fill`.

```swift
// Create a system symbol image that is enclosed with a filled circle variant.
Image(systemName: "multiply")
      .symbolVariant(.circle.fill)
```

##### Align Symbol Images with a Text Label By Using a Baseline

Because of the typographical nature of SF Symbols, when you position an image view containing a symbol image next to a label, you should align the views using their baselines. To align views in your storyboard, select the two views and add a first baseline constraint. Programmatically, you create this constraint by setting the [`firstBaselineAnchor`](uiview/firstbaselineanchor.md) of both views to be equal, as the following code example shows:

All system symbol images include baseline information, and `UIImage` exposes the baseline value as an offset from the bottom of the image. Typically, the baseline of a symbol image aligns with the bottom of any text that appears in the image, but even symbol images without text have a baseline. In AppKit, a symbol’s baseline corresponds to the bottom of the [`alignmentRect`](https://developer.apple.com/documentation/AppKit/NSImage/alignmentRect) property, and in UIKit you can add a baseline to any image by calling its [`withBaselineOffset(fromBottom:)`](uiimage/withbaselineoffset(frombottom:).md) method.

```swift
// Create a custom symbol image.
let image = UIImage(named: "custom.multiply.circle")

// Add an offset of 2.0 points from the baseline.
let baselineImage = image?.withBaselineOffset(fromBottom: 2.0)
```

In SwiftUI, you use [`firstTextBaseline`](https://developer.apple.com/documentation/SwiftUI/VerticalAlignment/firstTextBaseline) to baseline align a symbol with text.

```swift
HStack(alignment: .firstTextBaseline) {
    Image(systemName: "menucard")
    Text("SF Symbols")
}
```

##### Use Fallback Assets for Deprecated Symbol Name Changes

Symbol names may change between operating system versions and SF Symbols app releases, so you need to review your symbol usage when supporting new versions. Look for the deployment target when browsing the SF Symbols app and use the old name if you’re backward deploying.

If a symbol doesn’t render in your app, use the SF Symbols app to search for the symbol name, and look for availability updates by choosing View > Inspectors > Show Info Sidebar.

Depending on the operating systems you support, you may need to provide assets that you fall back to. For example, SF Symbols is only supported in iOS 13 and later. In your asset catalog you might have a symbol image named `gamecontroller`, and a fallback PNG asset named `gamecontroller` that you use for earlier operating system versions. Using Interface Builder, set an image view with your asset named `gamecontroller` and it loads the first available asset based on the platform.

Programmatically, you need to use #`available` to load assets appropriately.

```swift
if #available(iOS 13.0, *) {
    // Load an SF Symbol image.
} else {
    // Load a PNG asset.
}
```

## See Also

- [Providing images for different appearances](providing-images-for-different-appearances.md)
  Supply image resources appropriate for light and dark appearances and for high-contrast environments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit/configuring-and-displaying-symbol-images-in-your-ui)*