# UIEventAttribution

**Framework**: UIKit  
**Kind**: class

An object that contains event attribution information for Web AdAttributionKit.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIEventAttribution
```

#### Overview

Apps use event attribution objects to send data to the browser when opening an external website that supports Web AdAttributionKit (formerly known as Private Click Measurement, or PCM). For more information on the proposed PCM web standard, see [`Introducing Private Click Measurement`](https://developer.apple.comhttps://webkit.org/blog/11529/introducing-private-click-measurement-pcm/) and [`Private Click Measurement Draft Community Group Report`](https://developer.apple.comhttps://privacycg.github.io/private-click-measurement/).

> **Note**:  Mac apps built with Mac Catalyst don’t support Web AdAttributionKit.

 Mac apps built with Mac Catalyst don’t support Web AdAttributionKit.

You can’t subclass [`UIEventAttribution`](uieventattribution.md).

##### Define an Endpoint

In order to use Web AdAttributionKit, your app defines an `Info.plist` key called [`NSAdvertisingAttributionReportEndpoint`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAdvertisingAttributionReportEndpoint) that contains the URL to which the browser sends event attribution data. When an externally linked website reports that a conversion has occurred, the browser forwards your app’s event attribution data to the endpoint specified in the `Info.plist`. If your app’s `Info.plist` doesn’t contain this key, the browser won’t be able to forward the Web AdAttributionKit data when a conversion occurs.

Send event attribution data to the browser only when your app opens an external link as a result of a user tapping a control that sits below a [`UIEventAttributionView`](uieventattributionview.md) in the app’s view hierarchy. The event attribution view verifies that the user tapped a control. If that control doesn’t sit below an event attribution view, the system won’t send the Web AdAttributionKit data to the browser when opening the external link.

##### Create an Event Attribution Data Object

Here’s how you create a [`UIEventAttribution`](uieventattribution.md) object:

##### Send Event Attribution Data to the Browser

Once you create a [`UIEventAttribution`](uieventattribution.md) object, send it to the browser when your app opens a URL as the result of a user tap. If the external website reports a conversion within 7 days, the browser forwards the data from the [`UIEventAttribution`](uieventattribution.md) object to the specified remote server sometime between 24 and 48 hours after the conversion.

There are two different ways to send event attribution data when your app opens an external link, depending on whether your app uses [`UIScene`](uiscene.md) or [`UIApplication`](uiapplication.md) for life cycle management. For more information on application life cycle management, see [`Managing your app’s life cycle`](managing-your-app-s-life-cycle.md).

> ❗ **Important**:  The browser, and not your app, sends the event attribution data to the remote server. If the user’s selected browser doesn’t support Web AdAttributionKit, the event attribution fails even if the external website reports a conversion.

 The browser, and not your app, sends the event attribution data to the remote server. If the user’s selected browser doesn’t support Web AdAttributionKit, the event attribution fails even if the external website reports a conversion.

If your app uses [`UIScene`](uiscene.md)-based life cycle management, create a [`UIScene.OpenExternalURLOptions`](uiscene/openexternalurloptions.md) object, assign the event attribution object you created to its [`eventAttribution`](uiapplication/openexternalurloptionskey/eventattribution.md) property, and call [`open(_:options:completionHandler:)`](uiscene/open(_:options:completionhandler:).md):

If your app uses [`UIApplication`](uiapplication.md)-based life cycle management, create a dictionary that contains the [`eventAttribution`](uiapplication/openurloptionskey/eventattribution.md) key with the [`UIEventAttribution`](uieventattribution.md) object you created as its value, and call [`open(_:options:completionHandler:)`](uiapplication/open(_:options:completionhandler:).md), passing the dictionary using the `options` parameter.

##### Send Event Attribution Data to Sfsafariviewcontroller

If your app displays a web page in [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) after a person taps an ad, add a [`UIEventAttributionView`](uieventattributionview.md) subview to the ad view or control in order to measure taps. When a person taps the ad, follow these steps:

1. Create an [`SFSafariViewController.Configuration`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController/Configuration-swift.class) object.
2. Assign the [`UIEventAttribution`](uieventattribution.md) object you created to the [`eventAttribution`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController/Configuration-swift.class/eventAttribution) property of the [`SFSafariViewController.Configuration`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController/Configuration-swift.class) object.
3. Initialize an [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) instance with the configuration object, and present it. [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) validates that a tap on a [`UIEventAttributionView`](uieventattributionview.md) initiated the navigation to the webpage. If not, it discards the attribution data.

## Topics

### Creating event attribution objects
- [init(sourceIdentifier: UInt8, destinationURL: URL, sourceDescription: String, purchaser: String)](uieventattribution/init(sourceidentifier:destinationurl:sourcedescription:purchaser:).md)
  Initializes a new event attribution object.
### Setting attribution details
- [var destinationURL: URL](uieventattribution/destinationurl.md)
  The destination URL to attribute.
- [var purchaser: String](uieventattribution/purchaser.md)
  The entity that purchased the ad or content.
- [var reportEndpoint: URL?](uieventattribution/reportendpoint.md)
  The URL that receives attribution data.
- [var sourceDescription: String](uieventattribution/sourcedescription.md)
  A string describing the source tapped to launch the external link.
- [var sourceIdentifier: UInt8](uieventattribution/sourceidentifier.md)
  A number that identifies the source of the attribution.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIEventAttributionView](uieventattributionview.md)
  An overlay view that verifies user interaction for Web AdAttributionKit.
- [NSAdvertisingAttributionReportEndpoint](../BundleResources/Information-Property-List/NSAdvertisingAttributionReportEndpoint.md)
  The URL where Private Click Measurement and SKAdNetwork send attribution information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieventattribution)*