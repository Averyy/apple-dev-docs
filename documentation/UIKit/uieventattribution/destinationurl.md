# destinationURL

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The destination URL to attribute.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
var destinationURL: URL { get }
```

```objc
@property (nonatomic, copy, readonly) NSURL * destinationURL;
```

## Discussion

This property contains the URL associated with the event; for example, the `destinationURL` for an advertisement contains the external link opened when the user taps the ad.

This field corresponds to the `attributed_on_site` field of a web attribution.

## See Also

### Setting attribution details
- [var purchaser: String](./purchaser.md)
  The entity that purchased the ad or content.
- [var reportEndpoint: URL?](./reportendpoint.md)
  The URL that receives attribution data.
- [var sourceDescription: String](./sourcedescription.md)
  A string describing the source tapped to launch the external link.
- [var sourceIdentifier: UInt8](./sourceidentifier.md)
  A number that identifies the source of the attribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieventattribution/destinationurl)*