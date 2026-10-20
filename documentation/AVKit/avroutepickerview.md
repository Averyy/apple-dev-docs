# AVRoutePickerView

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

A view that presents a list of nearby media receivers.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 11.0+

## Declaration

```swift
class AVRoutePickerView
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface AVRoutePickerView : UIView
```

*macOS*

```objc
@interface AVRoutePickerView : NSView
```

#### Overview

This view represents a button that users tap to stream audio/video content to a media receiver, such as a Mac or Apple TV.

![A screenshot of an AV route picker view that composes a button with text that says Choose output device on the left, and an icon of a computer screen next to a set-top box remote on the right.](https://developer.apple.com/tutorials/images/com.apple.avkit/media-4084059@2x.png)

When the user taps the button, the system presents a popover that displays all of the nearby AirPlay devices that can receive and play back media. If your app prefers video content, the system displays video-capable devices higher in the list.

![A screenshot of a popover with a list of items. The top item is an iPad icon with a check mark to the right. Below that is the title Speakers and TVs with a list of six subitems. The first subitem says Third-party device, followed by AirPlay and Third-party protocol. The remaining subitems are Sunset Beach with an Apple TV icon on the left, Link with TV code with a globe icon on the left, and Show more.](https://developer.apple.com/tutorials/images/com.apple.avkit/media-4084052@2x.png)

In iOS 16 and later, you can add devices to the list that implement custom protocols. For more information about displaying third-party routes, see [AVRouting](../AVRouting/AVRouting.md).

##### Configure the button’s text, color, and media preference

The following code example creates the view alongside custom text:

```swift
HStack {
    Text("Choose output device")
        .font(.title)
        .frame(maxWidth: .infinity, alignment: .center)
        .fixedSize()
        .padding(.leading)

    if routeDetected {
        DevicePickerView() // See implementation below.
        .frame(width: 60, height: 60)
        .padding(.trailing)
    }
}
```

Your app configures the button’s color scheme and indicates whether your app prefers video content, as the following code demonstrates:

```swift
struct DevicePickerView: UIViewRepresentable {
    func makeUIView(context: Context) -> UIView {
        let routePickerView = AVRoutePickerView()

        // Configure the button's color.
        routePickerView.delegate = context.coordinator
        routePickerView.backgroundColor = UIColor.white
        routePickerView.tintColor = UIColor.black

        // Indicate whether your app prefers video content.
        routePickerView.prioritizesVideoDevices = true

        return routePickerView
```

## Topics

### Configuring the delegate
- [var delegate: (any AVRoutePickerViewDelegate)?](./avroutepickerview/delegate.md)
  The delegate object for the route picker.
- [protocol AVRoutePickerViewDelegate](./avroutepickerviewdelegate.md)
  A protocol that defines the methods to adopt to respond to route picker view presentation events.
### Configuring the route picker view
- [var activeTintColor: UIColor!](./avroutepickerview/activetintcolor.md)
  The view’s tint color when AirPlay is active.
- [var isRoutePickerButtonBordered: Bool](./avroutepickerview/isroutepickerbuttonbordered.md)
  A Boolean value that indicates whether the route picker button has a border.
- [var prioritizesVideoDevices: Bool](./avroutepickerview/prioritizesvideodevices.md)
  A Boolean value that indicates whether the route picker sorts video output devices to the top of the list.
- [var routePickerButtonStyle: AVRoutePickerViewButtonStyle](./avroutepickerview/routepickerbuttonstyle.md)
  The button style for the route picker.
- [enum AVRoutePickerViewButtonStyle](./avroutepickerviewbuttonstyle.md)
  Constants that define the button styles a route picker view supports.
- [func routePickerButtonColor(for: AVRoutePickerView.ButtonState) -> NSColor](./avroutepickerview/routepickerbuttoncolor%28for%29.md)
  Returns the color of the picker button for the specified state.
- [func setRoutePickerButtonColor(NSColor?, for: AVRoutePickerView.ButtonState)](./avroutepickerview/setroutepickerbuttoncolor%28_,for%29.md)
  Sets the route picker button color for the specified state.
- [AVRoutePickerView.ButtonState](./avroutepickerview/buttonstate.md)
  Constants that describe the available button states.
### Accessing the player
- [var player: AVPlayer?](./avroutepickerview/player.md)
  The player object to perform routing operations for.
### Setting a custom routing controller
- [var customRoutingController: AVCustomRoutingController?](./avroutepickerview/customroutingcontroller.md)
  A routing controller that enables connections to non-AirPlay devices.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Route selection
- [protocol AVRoutePickerViewDelegate](./avroutepickerviewdelegate.md)
  A protocol that defines the methods to adopt to respond to route picker view presentation events.
- [enum AVRoutePickerViewButtonStyle](./avroutepickerviewbuttonstyle.md)
  Constants that define the button styles a route picker view supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerview)*