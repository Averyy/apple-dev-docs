# AVRouting

**Framework**: AVRouting  
**Kind**: module

Display custom destinations to stream media in the system route picker.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 26.0+ (Beta)

#### Overview

Use the AVRouting framework to add third-party devices and protocols to [`AVRoutePickerView`](https://developer.apple.com/documentation/AVKit/AVRoutePickerView). This enables a user to stream AV content through a third-party protocol using the same system menu as AirPlay.

When the user taps the view, the system presents a popover that lists the available media receivers. If your app’s bundle includes an extension with the [`Media Device Discovery Extension`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.media-device-discovery-extension) entitlement, the system runs the extension and adds its associated third-party protocol to the picker, if the device resides nearby.

![A screenshot of a popover with a list of items. The top item is an iPad icon with a check mark to the right. Below that is the title Speakers and TVs with a list of six subitems. The first subitem says Third-party device, followed by AirPlay and Third-party protocol. The remaining subitems are Sunset Beach with an Apple TV icon on the left, Link with TV code with a globe icon on the left, and Show more. ](https://docs-assets.developer.apple.com/published/1d9b9665560d183b359bbdc62fe3f340/media-4084674%402x.png)

##### Add a Custom Route to the System Device Picker View

To indicate your app’s intent to search for a nearby third-party media receiver, set a custom routing controller ([`AVCustomRoutingController`](avcustomroutingcontroller.md)) on the view.

```swift
struct DevicePickerView: UIViewRepresentable {
    func makeUIView(context: Context) -> UIView {
        let routePickerView = AVRoutePickerView()
        routePickerView.delegate = context.coordinator
        routePickerView.customRoutingController = RouteManager.shared.customRoutingController
```

Next, let the view know which particular device your app intends to add. Each device requires a unique device discovery extension, which distinguishes itself through a uniform type identifier in its `Info.plist` file. Add a custom routing action ([`AVCustomRoutingActionItem`](avcustomroutingactionitem.md)) with [`type`](avcustomroutingactionitem/type.md) set to the identifier and pass the item to the controller’s [`customActionItems`](avcustomroutingcontroller/customactionitems.md).

```swift
func routePickerViewWillBeginPresentingRoutes(_ routePickerView: AVRoutePickerView) {
    if let type = UTType("com.example.apple-DataAccessDemo.menu") {
        let customRow1 = AVCustomRoutingActionItem()
        customRow1.type = type
        RouteManager.shared.customRoutingController?.customActionItems = [customRow1]
    }
}
```

If the extension finds the device at runtime, it passes the device to the system for display in the picker. See [`Discovering a third-party media-streaming device`](https://developer.apple.com/documentation/DeviceDiscoveryExtension/discovering-a-third-party-media-streaming-device) for a complete sample code project that routes media through a custom protocol.

## Topics

### Media routing
- [class AVCustomRoutingController](avcustomroutingcontroller.md)
  An object that manages the connection from a device to a destination.
- [protocol AVCustomRoutingControllerDelegate](avcustomroutingcontrollerdelegate.md)
  A protocol for delegates of a custom routing controller.
- [class AVCustomRoutingEvent](avcustomroutingevent.md)
  An object that represents an event that occurs on a route.
- [class AVCustomRoutingActionItem](avcustomroutingactionitem.md)
  An object that represents a custom action item to display in a device route picker.
### Playback arbitration
- [class AVRoutingPlaybackArbiter](avroutingplaybackarbiter.md)
  An object that manages playback routing preferences.
- [protocol AVRoutingPlaybackParticipant](avroutingplaybackparticipant.md)
  A protocol for objects that participate in playback routing arbitration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVRouting)*