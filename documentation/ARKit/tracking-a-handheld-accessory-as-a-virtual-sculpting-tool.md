# Tracking a handheld accessory as a virtual sculpting tool

**Framework**: ARKit

Use a tracked accessory with Apple Vision Pro to create a virtual sculpture.

**Availability**:
- visionOS 26.0+
- Xcode 26.0+

#### Overview

> **Note**: This sample code project is associated with WWDC25 session 289: [`Explore spatial accessory input on visionOS`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/289).

#### Configure the Sample Code Project

Because this sample app has hardware requirements, it won’t run in Simulator. Instead, you’ll need to build the sample and run it on Apple Vision Pro, using a tracked accessory for sculpting.

## See Also

- [class AccessoryTrackingProvider](accessorytrackingprovider.md)
  Provides the real time position of accessories in the user’s environment.
- [struct Accessory](accessory.md)
  Represents an accessory to be tracked.
- [struct AccessoryAnchor](accessoryanchor.md)
  Represents a tracked accessory.
- [Tracking accessories in volumetric windows](tracking-accessories-in-volumetric-windows.md)
  Translate the position and velocity of tracked handheld accessories to throw virtual balls at a stack of cans.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/tracking-a-handheld-accessory-as-a-virtual-sculpting-tool)*