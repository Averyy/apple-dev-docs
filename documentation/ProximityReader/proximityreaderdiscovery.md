# ProximityReaderDiscovery

**Framework**: ProximityReader  
**Kind**: class

An object that presents a UI with information about how to use Tap to Pay on iPhone.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
final class ProximityReaderDiscovery
```

#### Overview

Use a [`ProximityReaderDiscovery`](proximityreaderdiscovery.md) object to educate people on how to read contactless credentials with their iPhone. When building a reader interface in your app, include controls to display help information. When a person taps those controls, use this type to present a view controller with information about how to use a particular feature. The system manages the presented view controller, displaying materials to teach people how the system works.

Create a [`ProximityReaderDiscovery`](proximityreaderdiscovery.md) object in response to requests for help from your app’s interface. Fetch a relevant help topic and present that topic using the [`presentContent(_:from:)`](proximityreaderdiscovery/presentcontent(_:from:).md) method, as shown in the following example. Present the topic displays a new view controller with information about how to use the relevant features. This view controller remains visible until the person dismisses it, at which point control returns to your app’s current view controller.

```None
let proximityReaderDiscovery = ProximityReaderDiscovery()

Task {
    do {
        let content = try await proximityReaderDiscovery.content(for: ProximityReaderDiscovery.Topic.payment(.howToTap))
        try await proximityReaderDiscovery.presentContent(content, from: myCurrentViewController)
    } catch {
        // Handle content display errors.
    }
}
```

## Topics

### Creating a discovery object
- [init()](proximityreaderdiscovery/init.md)
  Creates a new proximity reader discovery object.
### Fetching the content to display
- [func content(for: ProximityReaderDiscovery.Topic) async throws -> ProximityReaderDiscovery.Content](proximityreaderdiscovery/content(for:).md)
  Fetches the content for the specified topic.
- [ProximityReaderDiscovery.Topic](proximityreaderdiscovery/topic.md)
  The topics you can present to someone.
- [ProximityReaderDiscovery.Content](proximityreaderdiscovery/content.md)
  A type that represents content you can display on the current device.
- [var contentList: [ProximityReaderDiscovery.Content]](proximityreaderdiscovery/contentlist.md)
  The content you can present for the current device.
### Displaying the information
- [func presentContent(ProximityReaderDiscovery.Content, from: UIViewController) async throws](proximityreaderdiscovery/presentcontent(_:from:).md)
  Presents a sheet that teaches merchants how to use the specified feature.
### Getting relevant errors
- [ProximityReaderDiscovery.ContentError](proximityreaderdiscovery/contenterror.md)
  Errors that indicate a problem occurred when getting or showing content.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery)*