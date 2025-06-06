# Providing images for different appearances

**Framework**: UIKit

Supply image resources appropriate for light and dark appearances and for high-contrast environments.

#### Overview

Wherever your app’s interface uses bitmap images, make sure those images look good in both light and dark appearances. A bitmap image that looks good in one appearance might look washed out or be hard to see in another. Fortunately, asset catalogs simplify the process for managing image assets for each appearance style, and for displaying the correct image at the proper time.

An alternative to creating bitmap images is to use template images or symbol images instead. Template images specify the shape you want to draw, but not the associated color information. Symbol images are similar to template images but are vector based, so they scale to different sizes. Both types of images simplify the process for supporting Dark Mode. They also reduce the number of image assets you must ship with your app.

##### Customize Image Assets for Different Appearances

The best way to manage images for different appearances is with asset catalogs. Each asset in an asset catalog represents a named image that you load from your app. Inside that asset are multiple variations of the same image, each with the appropriate content and colors for light, dark, and high-contrast environments. When you load an asset, you get a reference to the entire asset and all of its image variations. During drawing, the system automatically draws the appropriate variant based on the current settings. When the settings change, the system redraws the image with the new settings.

Create image assets in Xcode, and use the Appearance attributes to configure which variants you want to supply.

![An image of the Xcode interface for configuring an image asset. After configuring the appearance options from the attributes inspector, drag each image variant to the appropriate slot in the editor window. ](https://docs-assets.developer.apple.com/published/cb4d3252a2f2c326daa5fa1775710e13/media-3013535%402x.png)

You can supply image assets for different combinations of the following characteristics:

- Screen resolution. Provide images for regular and Retina displays. The system picks the image that best matches the resolution of the current screen.
- Light and dark appearances. Provide images for both light and dark appearances. Use the Any Appearance slots to support older versions of macOS or iOS.
- High contrast. Provide images with greater visual separation between adjoining colors. Such images make it easier for users with vision impairments to see the image details.

##### Create Scalable and Tintable Images Using Symbol Images

In iOS, tvOS, and watchOS, use symbol images in places where you would usually combine images and text to form icons. A symbol image is a vector-based image that you use in places where you want to display a simple shape or glyph. For example, use symbol images in bar button items or in places where you want to combine an icon with a description. Symbol images have several advantages:

- They scale without losing any of their sharpness.
- You can tint them with an appropriate color.
- They include a baseline for layout with text.
- You can configure them with font-related style information to make them appear as if they belong to that font.

The system provides a library of images for you to use, and you can create new symbol images for any custom iconography your app requires.  For information about how to create and use symbol images, see [`Configuring and displaying symbol images in your UI`](configuring-and-displaying-symbol-images-in-your-ui.md).

##### Create Tintable Images Using Template Images

An alternative to providing separate images for different appearances is to provide a single template image that adapts to all appearances. A template image is a bitmap image where only the opacity of the image matters. Typically, you use template images to represent iconic shapes. For example, you might use template images to represent the play and pause buttons of a media app.

When you add a template image to a button or image view, you also specify a tint color. The view applies the tint color to every pixel that doesn’t have an alpha of `0.0`, causing the image’s shape to adopt that color. To support different appearances, simply change the tint color. For example, you might apply a dark tint color in light environments and a light tint color in dark environments.

![Views apply tints to a template image to make it stand out against the background. The tint colors change based on whether the view is displayed with a light or dark appearance.](https://docs-assets.developer.apple.com/published/e3a52be619fd3661abd1aa29b773d44c/media-3009972%402x.png)

Use your favorite image editor to create template image files. When creating your image, use a transparent background and add black pixels wherever you want the image to appear. The pixels can be fully or partially opaque, depending on whether you want portions of your template image to blend with the background colors. When adding the image to your asset catalog, set the Render As option for the Image Set asset to Template Image in the inspector.

##### Create Images with a Drawing Handler in Macos

When designing your app’s interface, you typically create images at design time and include them in the app bundle that you ship. However, in macOS, you can also create images dynamically, which you might do if you don’t yet know what the image content will be, or if that content is changeable.

To create an image that draws its content dynamically, use the [`init(size:flipped:drawingHandler:)`](https://developer.apple.com/documentation/AppKit/NSImage/init(size:flipped:drawingHandler:)) method to initialize your image with a custom drawing handler block. AppKit calls your handler block whenever the system appearance changes, giving you a chance to redraw the image using the new appearance.

## See Also

- [Configuring and displaying symbol images in your UI](configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/providing-images-for-different-appearances)*