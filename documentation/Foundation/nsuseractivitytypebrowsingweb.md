# NSUserActivityTypeBrowsingWeb

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

An activity that continues from Handoff or a universal link.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSUserActivityTypeBrowsingWeb: String
```

```c
extern NSString * const NSUserActivityTypeBrowsingWeb;
```

## Discussion

An [`NSUserActivity`](./nsuseractivity.md) object with an [`activityType`](./nsuseractivity/activitytype.md) value of [`NSUserActivityTypeBrowsingWeb`](./nsuseractivitytypebrowsingweb.md) indicates either an activity continued from a web browser-to-native app Handoff or a universal link. For this activity type, the [`webpageURL`](./nsuseractivity/webpageurl.md) property contains the `http` or `https` URL associated with the activity.

For more information on universal links, see [Allowing apps and websites to link to your content](../Xcode/allowing-apps-and-websites-to-link-to-your-content.md). For more information on web browser-to-native app Handoff, see [Web Browser–to–Native App Handoff](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Handoff/AdoptingHandoff/AdoptingHandoff.html#//apple_ref/doc/uid/TP40014338-CH2-SW10).

## See Also

### Browsing the web
- [var webpageURL: URL?](./nsuseractivity/webpageurl.md)
  The URL of the webpage to load in a browser to continue the activity.
- [var referrerURL: URL?](./nsuseractivity/referrerurl.md)
  The URL of the webpage that linked to the webpage URL.
- [let TVUserActivityTypeBrowsingChannelGuide: String](../TVServices/tvuseractivitytypebrowsingchannelguide.md)
  An activity for viewing your app’s channel guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivitytypebrowsingweb)*