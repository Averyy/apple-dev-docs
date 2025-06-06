# UIImageView

**Framework**: Uikit  
**Kind**: class

A view that displays a single image or a sequence of animated images in your interface.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIImageView
```

#### Overview

Image views let you efficiently draw any image that can be specified using a [`UIImage`](uiimage.md) object. For example, you can use the [`UIImageView`](uiimageview.md) class to display the contents of many standard image files, such as JPEG and PNG files. You can configure image views programmatically or in your storyboard file and change the images they display at runtime. For animated images, you can also use the methods of this class to start and stop the animation and specify other animation parameters.

![An image view](https://docs-assets.developer.apple.com/published/707440cc50954c46cf2c38fbab7cd76b/media-2923882%402x.png)

##### Understand How Images Are Scaled

An image view uses its [`contentMode`](uiview/contentmode-swift.property.md) property and the configuration of the image itself to determine how to display the image. It’s best to specify images whose dimensions match the dimensions of the image view exactly, but image views can scale your images to fit all or some of the available space. If the size of the image view itself changes, it automatically scales the image as needed.

For an image without cap insets, the presentation of the image is determined solely by the image view’s [`contentMode`](uiview/contentmode-swift.property.md) property. The [`UIView.ContentMode.scaleAspectFit`](uiview/contentmode-swift.enum/scaleaspectfit.md) and [`UIView.ContentMode.scaleAspectFill`](uiview/contentmode-swift.enum/scaleaspectfill.md) modes scale the image to fit or fill the space while maintaining the image’s original aspect ratio. The [`UIView.ContentMode.scaleToFill`](uiview/contentmode-swift.enum/scaletofill.md) value scales the image without regard to the original aspect ratio, which can cause the image to appear distorted. Other content modes place the image at the appropriate location in the image view’s bounds without scaling it.

For a resizable image with cap insets, those insets affect the final appearance of the image. Specifically, cap insets define which parts of the image may be scaled and in which directions. You can create a resizable image that stretches using the [`resizableImage(withCapInsets:resizingMode:)`](uiimage/resizableimage(withcapinsets:resizingmode:).md) method of [`UIImage`](uiimage.md). When using an image of this type, you typically set the image view’s content mode to [`UIView.ContentMode.scaleToFill`](uiview/contentmode-swift.enum/scaletofill.md) so that the image stretches in the appropriate places and fills the image view’s bounds.

For tips on how to prepare images, see [`Debug issues with your image view`](uiimageview#Debug-issues-with-your-image-view.md). For more information on creating resizable images with cap insets, see [`UIImage`](uiimage.md).

##### Determine the Final Transparency of the Image

Images are composited onto the image view’s background and are then composited into the rest of the window. Any transparency in the image allows the image view’s background to show through. Similarly, any further transparency in the background of the image is dependent on the transparency of the image view and the transparency of the [`UIImage`](uiimage.md) object it displays. When the image view and its image both have transparency, the image view uses alpha blending to combine the two.

- The image is composited onto the image view’s background.
- If the image view’s [`isOpaque`](uiview/isopaque.md) property is [`true`](https://developer.apple.com/documentation/swift/true), the image’s pixels are composited on top of the image view’s background color and the [`alpha`](uiview/alpha.md) property of the image view is ignored.
- If the image view’s [`isOpaque`](uiview/isopaque.md) property is [`false`](https://developer.apple.com/documentation/swift/false), the alpha value of each pixel is multiplied by the image view’s [`alpha`](uiview/alpha.md) value, with the resulting value becoming the actual transparency value for that pixel. If the image doesn’t have an alpha channel, the alpha value of each pixel is assumed to be `1.0`.

> ❗ **Important**:  It’s computationally expensive to composite the alpha channel of an image with the alpha channel of a non-opaque image view. The performance impact is further magnified if you use Core Animation shadows, because the shape of the shadow is then based on the contents of the view and must be dynamically computed. If you aren’t intentionally using the alpha channel of the image or the alpha channel of the image view, set the [`isOpaque`](uiview/isopaque.md) property to [`true`](https://developer.apple.com/documentation/swift/true) to improve performance. For additional optimization tips, see [`Improve performance`](uiimageview#Improve-performance.md).

##### Animate a Sequence of Images

An image view can store an animated image sequence and play all or part of that sequence. You specify an image sequence as an array of [`UIImage`](uiimage.md) objects and assign them to the [`animationImages`](uiimageview/animationimages.md) property. Once assigned, you can use the methods and properties of this class to configure the animation timing and to start and stop the animation.

> **Note**:  You can also construct a single [`UIImage`](uiimage.md) object from a sequence of individual images using the [`animatedImage(with:duration:)`](uiimage/animatedimage(with:duration:).md) method. Doing so yields the same results as assigning the individual images to the [`animationImages`](uiimageview/animationimages.md) property.

Consider the following tips when displaying a sequence of animated images:

-  When scaling is required, the image view scales each image in the sequence separately. If the images are different sizes, scaling may not yield the results you want.
-  Make sure the [`scale`](uiimage/scale.md) property of each image contains the same value.

##### Respond to Touch Events

Image views ignore user events by default. Normally, you use image views only to present visual content in your interface. If you want an image view to handle user interactions as well, change the value of its [`isUserInteractionEnabled`](uiimageview/isuserinteractionenabled.md) property to [`true`](https://developer.apple.com/documentation/swift/true). After doing that, you can attach gesture recognizers or use any other event handling techniques to respond to touch events or other user-initiated events.

For more information about handling events, see [`Event Handling Guide for UIKit Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html#//apple_ref/doc/uid/TP40009541).

##### Improve Performance

Image scaling and alpha blending are two relatively expensive operations that can impact your app’s performance. To maximize performance of your image view code, consider the following tips:

-  If you expect certain large images to be displayed frequently in a scaled-down thumbnail view, consider creating the scaled-down images in advance and storing them in a thumbnail cache. Doing so alleviates the need for each image view to scale them separately.
-  Rather than assigning a large image to an image view, created a scaled version that matches the current size of the image view. You can also create a resizable image object using the [`UIImage.ResizingMode.tile`](uiimage/resizingmode-swift.enum/tile.md) option, which tiles the image instead of scaling it.
-  Unless you’re intentionally working with images that contain transparency (drawing UI elements, for example), make sure the [`isOpaque`](uiview/isopaque.md) property of your image view is set to [`true`](https://developer.apple.com/documentation/swift/true). For more information about how transparency is determined, see [`Determine the final transparency of the image`](uiimageview#Determine-the-final-transparency-of-the-image.md).

##### Debug Issues with Your Image View

If your image view isn’t displaying what you expected, use the following tips to help diagnose the problem:

-  Use the [`init(named:in:compatibleWith:)`](uiimage/init(named:in:compatiblewith:).md) method of [`UIImage`](uiimage.md) to load images from asset catalogs or your app’s bundle. For images outside of your app’s bundle, use the [`imageWithContentsOfFile:`](uiimage/imagewithcontentsoffile:.md) method.
-  The [`UIImageView`](uiimageview.md) class doesn’t draw its content using the [`draw(_:)`](uiview/draw(_:).md) method. Use image views only to present images. To do custom drawing involving images, subclass [`UIView`](uiview.md) directly and draw your image there.

##### Interface Builder Attributes

The following table lists the attributes that you configure for image views in Interface Builder.

| Attribute | Discussion |
| --- | --- |
| Image | The image to display. You can specify any image in your Xcode project, including standalone images and those in image assets. To set this attribute programmatically, use the [`image`](uiimageview/image.md) or [`animationImages`](uiimageview/animationimages.md) property. |
| Highlighted | The image to display when the image view is highlighted. To set this attribute programmatically, use the [`highlightedImage`](uiimageview/highlightedimage.md) or [`highlightedAnimationImages`](uiimageview/highlightedanimationimages.md) property. |
| State | The initial state of the image. Use this attribute to mark the image as highlighted. To set this attribute programmatically, use the [`isHighlighted`](uiimageview/ishighlighted.md) property. |

##### Internationalization

Internationalization of image views is automatic if your view displays only static images loaded from your app bundle. If you’re loading images programmatically, you’re at least partially responsible for loading the correct image.

- For resources in your app bundle, you do this by specifying the name in the attributes inspector or by calling the [`init(named:)`](uiimage/init(named:).md) class method on [`UIImage`](uiimage.md) to obtain the localized version of each image.
- For images that aren’t in your app bundle, your code must do the following:

1. Determine which image to load in a manner specific to your app, such as providing a localized string that contains the URL.
2. Load that image by passing the URL or data for the correct image to an appropriate [`UIImage`](uiimage.md) class method, such as [`imageWithData:`](uiimage/imagewithdata:.md) or [`imageWithContentsOfFile:`](uiimage/imagewithcontentsoffile:.md).

> **Note**:  Screen metrics and layout may also change depending on the language and locale, particularly if the internationalized versions of your images have different dimensions. Where possible, you should try to make minimize dimension differences in internationalized versions of image resources.

For more information, see [`Localization`](https://developer.apple.com/documentation/Xcode/localization).

##### Accessibility

Image views are accessible by default. The default accessibility traits for an image view are Image and User Interaction Enabled.

For more information about making iOS controls accessible, see the accessibility information in [`UIControl`](uicontrol.md). For general information about making your interface accessible, see [`Accessibility for UIKit`](accessibility-for-uikit.md).

##### State Preservation

When you assign a value to an image view’s [`restorationIdentifier`](uiviewcontroller/restorationidentifier.md) property, it attempts to preserve the frame of the displayed image. Specifically, the class preserves the values of the [`bounds`](uiview/bounds.md), [`center`](uiview/center.md), and [`transform`](uiview/transform.md) properties of the view and the [`anchorPoint`](https://developer.apple.com/documentation/QuartzCore/CALayer/anchorPoint) property of the underlying layer. During restoration, the image view restores these values so that the image appears exactly as before. For more information about how state preservation and restoration works, see [`Restoring your app’s state`](restoring-your-app-s-state.md).

## Topics

### Creating an image view
- [init(image: UIImage?)](uiimageview/init(image:).md)
  Returns an image view initialized with the specified image.
- [init(image: UIImage?, highlightedImage: UIImage?)](uiimageview/init(image:highlightedimage:).md)
  Returns an image view initialized with the specified regular and highlighted images.
### Accessing the displayed images
- [var image: UIImage?](uiimageview/image.md)
  The image displayed in the image view.
- [var highlightedImage: UIImage?](uiimageview/highlightedimage.md)
  The highlighted image displayed in the image view.
### Animating a sequence of images
- [var animationImages: [UIImage]?](uiimageview/animationimages.md)
  An array of [`UIImage`](uiimage.md) objects to use for an animation.
- [var highlightedAnimationImages: [UIImage]?](uiimageview/highlightedanimationimages.md)
  An array of [`UIImage`](uiimage.md) objects to use for an animation when the view is highlighted.
- [var animationDuration: TimeInterval](uiimageview/animationduration.md)
  The amount of time it takes to go through one cycle of the images.
- [var animationRepeatCount: Int](uiimageview/animationrepeatcount.md)
  Specifies the number of times to repeat the animation.
- [func startAnimating()](uiimageview/startanimating.md)
  Starts animating the images in the receiver.
- [func stopAnimating()](uiimageview/stopanimating.md)
  Stops animating the images in the receiver.
- [var isAnimating: Bool](uiimageview/isanimating.md)
  Returns a Boolean value indicating whether the animation is running.
### Configuring the image view
- [var isUserInteractionEnabled: Bool](uiimageview/isuserinteractionenabled.md)
  A Boolean value that determines whether user events are ignored and removed from the event queue.
- [var isHighlighted: Bool](uiimageview/ishighlighted.md)
  A Boolean value that determines whether the image is highlighted.
- [var tintColor: UIColor!](uiimageview/tintcolor.md)
  A color used to tint template images in the view hierarchy.
### Configuring the appearance of symbol images
- [Configuring and displaying symbol images in your UI](configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [var preferredSymbolConfiguration: UIImage.SymbolConfiguration?](uiimageview/preferredsymbolconfiguration.md)
  The configuration values to use when rendering the image.
### Configuring symbol effects
- [func addSymbolEffect(some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](uiimageview/addsymboleffect(_:options:animated:completion:)-18jqj.md)
  Adds a discrete symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](uiimageview/addsymboleffect(_:options:animated:completion:)-2ixnm.md)
  Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](uiimageview/addsymboleffect(_:options:animated:completion:)-896qd.md)
  Adds an indefinite symbol effect to the image view with the specified options and animation.
- [func setSymbolImage(UIImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions, completion: UISymbolEffectCompletion?)](uiimageview/setsymbolimage(_:contenttransition:options:completion:).md)
  Sets a symbol image using the specified content-transition effect, options, and completion handler.
- [func removeSymbolEffect(ofType: some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](uiimageview/removesymboleffect(oftype:options:animated:completion:)-218lh.md)
  Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](uiimageview/removesymboleffect(oftype:options:animated:completion:)-31zec.md)
  Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](uiimageview/removesymboleffect(oftype:options:animated:completion:)-2boi2.md)
  Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [func removeAllSymbolEffects(options: SymbolEffectOptions, animated: Bool)](uiimageview/removeallsymboleffects(options:animated:).md)
  Removes all symbol effects from the image view, using the specified options and animation setting.
- [typealias UISymbolEffectCompletion](uisymboleffectcompletion-7qt7g.md)
  A completion handler for adding and removing symbol effects and transitions.
- [struct UISymbolEffectCompletionContext](uisymboleffectcompletioncontext-swift.struct.md)
  Information about a symbol effect’s addition or removal.
### Managing focus-related behaviors
- [var adjustsImageWhenAncestorFocused: Bool](uiimageview/adjustsimagewhenancestorfocused.md)
  Allows [`UIImageView`](uiimageview.md) to respond when an ancestor becomes focused.
- [var focusedFrameGuide: UILayoutGuide](uiimageview/focusedframeguide.md)
  The layout guide to use when the image view is focused.
- [var masksFocusEffectToContents: Bool](uiimageview/masksfocuseffecttocontents.md)
  A Boolean value indicating whether the floating focused appearance uses the image’s alpha channel.
### Layering content on top of the image view
- [var overlayContentView: UIView](uiimageview/overlaycontentview.md)
  A view for hosting layered content on top of the image view.
### Specifying the dynamic range
- [var imageDynamicRange: UIImage.DynamicRange](uiimageview/imagedynamicrange.md)
- [var preferredImageDynamicRange: UIImage.DynamicRange](uiimageview/preferredimagedynamicrange.md)
- [UIImage.DynamicRange](uiimage/dynamicrange.md)

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityContentSizeCategoryImageAdjusting](uiaccessibilitycontentsizecategoryimageadjusting.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIActivityIndicatorView](uiactivityindicatorview.md)
  A view that shows that a task is in progress.
- [class UICalendarView](uicalendarview.md)
  A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates.
- [class UIContentUnavailableView](uicontentunavailableview.md)
  A view that indicates there’s no content to display.
- [class UIPickerView](uipickerview.md)
  A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values.
- [class UIProgressView](uiprogressview.md)
  A view that depicts the progress of a task over time.
- [class UIWebView](uiwebview.md)
  A view that embeds web content in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit/uiimageview)*