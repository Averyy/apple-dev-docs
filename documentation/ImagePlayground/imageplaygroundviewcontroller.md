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

Create an [`ImagePlaygroundViewController`](imageplaygroundviewcontroller.md) and configure it with an initial description of the image you want before you present it. Specify a text-based description of the image using the [`concepts`](imageplaygroundviewcontroller/concepts.md) property. If you have a starting image that you want to use to create the new image, specify your image in the [`sourceImage`](imageplaygroundviewcontroller/sourceimage.md) property.

Present this view controller from your interface and wait for it to deliver results to your custom [`delegate`](imageplaygroundviewcontroller/delegate-swift.property.md) object. If the person approves the image, the view controller sends that image to your app via this delegate object. The view controller also notifies your delegate if the person cancels the operation.

## Topics

### Creating the view controller
- [convenience init()](imageplaygroundviewcontroller/init.md)
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
  An option for enabling or disabling personalization in the system interface.
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
  Called after the controller’s view is loaded into memory.
- [func viewDidDisappear()](imageplaygroundviewcontroller/viewdiddisappear.md)
  Notifies the view controller that its view is about to be removed from a view hierarchy.
- [func viewWillAppear()](imageplaygroundviewcontroller/viewwillappear.md)
  Notifies the view controller that its view is about to be added to a view hierarchy.
### Instance Properties
- [var isModalInPresentation: Bool](imageplaygroundviewcontroller/ismodalinpresentation.md)
  A Boolean value indicating whether the view controller enforces a modal behavior.
- [var modalPresentationStyle: UIModalPresentationStyle](imageplaygroundviewcontroller/modalpresentationstyle.md)
  The presentation style for modal view controllers.
- [var options: ImagePlaygroundOptions](imageplaygroundviewcontroller/options.md)
  Options that influence the image-generation process.
- [var preferredContentSize: CGSize](imageplaygroundviewcontroller/preferredcontentsize.md)
  The preferred size for the view controller’s view.
### Instance Methods
- [func viewDidDisappear(Bool)](imageplaygroundviewcontroller/viewdiddisappear(_:).md)
  Notifies the view controller that its view is about to be removed from a view hierarchy.

## Relationships

### Inherits From
- [NSViewController](../appkit/nsviewcontroller.md)
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSEditor](../appkit/nseditor.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSeguePerforming](../appkit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller)*