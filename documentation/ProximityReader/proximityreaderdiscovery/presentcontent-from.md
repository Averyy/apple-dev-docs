# presentContent(_:from:)

**Framework**: ProximityReader  
**Kind**: method

Presents a sheet that teaches merchants how to use the specified feature.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
final func presentContent(_ content: ProximityReaderDiscovery.Content, from viewController: UIViewController) async throws
```

#### Discussion

> **Note**: This method throws a [`ProximityReaderDiscovery.ContentError`](proximityreaderdiscovery/contenterror.md) if the sheet fails to appear.

Call this method when you want to display information about how to use [`ProximityReader`](ProximityReader.md) features on a merchant’s iPhone.  For example, you might use this method to display instructions for how the merchant uses Tap to Pay on iPhone. This method presents the requested information in a sheet on top of your app’s UI, which remains on-screen until the person dismiss it or an error occurs.

## Parameters

- `content`: The topic to teach. You can get a list of available   topics from the   property or fetch a topic for a   specific subject using the   method.
- `viewController`: The view controller to use when presenting the   sheet. Specify a currently visible view controller in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery/presentcontent(_:from:))*