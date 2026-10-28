# reportEndpoint

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The URL that receives attribution data.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
var reportEndpoint: URL? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSURL * reportEndpoint;
```

## Discussion

This read-only property contains the URL that recieves the event attribution data. Your app sets this value by reading it from its `Info.plist` using the [`NSAdvertisingAttributionReportEndpoint`](../../BundleResources/information-property-list/nsadvertisingattributionreportendpoint.md) key.

Specify the desired value in your Xcode project’s `Info.plist` file. Your app uses the value you set in all PCM attribution requests. You can’t change the value at runtime.

This field corresponds to the `source_site` field of a web attribution.

## See Also

### Setting attribution details
- [var destinationURL: URL](./destinationurl.md)
  The destination URL to attribute.
- [var purchaser: String](./purchaser.md)
  The entity that purchased the ad or content.
- [var sourceDescription: String](./sourcedescription.md)
  A string describing the source tapped to launch the external link.
- [var sourceIdentifier: UInt8](./sourceidentifier.md)
  A number that identifies the source of the attribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieventattribution/reportendpoint)*