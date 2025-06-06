# ImagePlaygroundViewController

**Framework**: Image Playground  
**Kind**: class

Displays a standard system interface to generate images from the provided input.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@objc @preconcurrency class ImagePlaygroundViewController
```

#### Overview

Present an [`ImagePlaygroundViewController`](imageplaygroundviewcontroller.md) to display a standard system interface to generate images from a description you provide. People use the view controller interface to generate images and experiment with the contents before returning an image to your app. You can then incorporate that image into your app’s content.

Create a [`ImagePlaygroundViewController`](imageplaygroundviewcontroller.md) and configure it with an initial description of the image you want before you present it. Specify a text-based description of the image using the [`concepts`](imageplaygroundviewcontroller/concepts.md) property. If you have a starting image that you want to use to create the new image, specify your image in the [`sourceImage`](imageplaygroundviewcontroller/sourceimage.md) property.

Present this view controller from your interface and wait for it to deliver results to your custom [`delegate`](imageplaygroundviewcontroller/delegate-swift.property.md) object. If the person approves the image, the view controller sends that image to your app via this delegate object. The view controller also notifies your delegate if the person cancels the operation.

## Topics

### Creating the view controller
- [init()](imageplaygroundviewcontroller/init.md)
  Creates a new image-generation view controller for you to present.
### Processing a generated image
- [var delegate: (any ImagePlaygroundViewController.Delegate)?](imageplaygroundviewcontroller/delegate-swift.property.md)
  The delegate object that receives the generated image and handles events from the view controller.
- [ImagePlaygroundViewController.Delegate](imageplaygroundviewcontroller/delegate-swift.protocol.md)
  An interface you use to receive images and handle events related to an image-generation view controller.
### Specifying the configuration of the playground
- [var selectedGenerationStyle: ImagePlaygroundStyle](imageplaygroundviewcontroller/selectedgenerationstyle.md)
  Generation style to pre-select upong launching the playground among those in `allowedGenerationStyles`.
- [var allowedGenerationStyles: [ImagePlaygroundStyle]](imageplaygroundviewcontroller/allowedgenerationstyles.md)
  A list of allowed generation styles to choose from in the playground.
- [var personalizationPolicy: ImagePlaygroundPersonalizationPolicy](imageplaygroundviewcontroller/personalizationpolicy.md)
  The policy to apply when determining whether to include people in generated images.
- [enum ImagePlaygroundPersonalizationPolicy](imageplaygroundpersonalizationpolicy.md)
  A policy for enabling or disabling personalization in the system interface.
### Specifying the source content
- [var concepts: [ImagePlaygroundConcept]](imageplaygroundviewcontroller/concepts.md)
  An array of elements that describes the expected contents of the image.
- [var sourceImage: UIImage?](imageplaygroundviewcontroller/sourceimage.md)
  An image to use as source input for generating the new image.
### Getting the feature availability
- [class var isAvailable: Bool](imageplaygroundviewcontroller/isavailable.md)
  A Boolean value that indicates whether image generation is available on the current device.
### Managing the view
- [func viewDidLoad()](imageplaygroundviewcontroller/viewdidload.md)
- [func viewDidDisappear()](imageplaygroundviewcontroller/viewdiddisappear.md)
- [func viewWillAppear()](imageplaygroundviewcontroller/viewwillappear.md)
### Instance Properties
- [var isModalInPresentation: Bool](imageplaygroundviewcontroller/ismodalinpresentation.md)
- [var modalPresentationStyle: UIModalPresentationStyle](imageplaygroundviewcontroller/modalpresentationstyle.md)
  The presentation style for modal view controllers.
- [var preferredContentSize: CGSize](imageplaygroundviewcontroller/preferredcontentsize.md)
- [var supportedInterfaceOrientations: UIInterfaceOrientationMask](imageplaygroundviewcontroller/supportedinterfaceorientations.md)
### Instance Methods
- [func viewDidDisappear(Bool)](imageplaygroundviewcontroller/viewdiddisappear(_:).md)

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller)*