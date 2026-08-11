# advertisingIdentifier

**Framework**: AdSupport  
**Kind**: property

The UUID that is specific to a device.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 6.0+

## Declaration

```swift
var advertisingIdentifier: UUID { get }
```

#### Discussion

The [`advertisingIdentifier`](asidentifiermanager/advertisingidentifier.md) is an alphanumeric string that’s unique to each device, and which you only use for advertising. Use this string for frequency capping, attribution, conversion events, estimating the number of unique users, advertising fraud detection, and debugging. On devices running iOS 14.5 and later and iPadOS 14.5 and later, your app must request tracking authorization before it can get the advertising identifier. For more information on getting the advertising identifier, see [`AdSupport`](AdSupport.md).

The advertising identifier returns either a unique UUID, or all zeros. It returns a unique UUID in the following cases:

- If Settings > Privacy > Tracking > Allow Apps to Request to Track is On, you’ve requested tracking authorization from the user by calling the [`App Tracking Transparency`](https://developer.apple.com/documentation/AppTrackingTransparency) APIs, and received authorization, indicated by [`ATTrackingManager.AuthorizationStatus.authorized`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/authorized).
- If the user changes Settings > Privacy > Tracking > Allow Apps to Request to Track to Off after authorizing your app, and leaves the permissions On for your app.

The advertising identifier returns all zeros (`00000000-0000-0000-0000-000000000000`) in the following cases:

- In Simulator, regardless of any settings.
- When you call this API on a device running macOS.
- When you call this API in a compatible iPad or iPhone app running in visionOS.
- On devices running iOS 14.5 and later and iPadOS 14.5 and later, if you haven’t requested authorization using the [`App Tracking Transparency`](https://developer.apple.com/documentation/AppTrackingTransparency) framework.
- If you’ve requested authorization using the [`App Tracking Transparency`](https://developer.apple.com/documentation/AppTrackingTransparency) framework and the user declines, which results in an authorization status of [`ATTrackingManager.AuthorizationStatus.denied`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/denied).
- When a profile or configuration restricts access to the advertising identifier. For more information about restrictions, see [`ATTrackingManager.AuthorizationStatus.restricted`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/restricted).

As a best practice, don’t store the advertising identifier value; access [`advertisingIdentifier`](asidentifiermanager/advertisingidentifier.md) instead. Users can change their authorization for tracking at any time in Settings > Privacy > Tracking. Check your app’s authorization using the App Tracking Transparency API [`trackingAuthorizationStatus`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/trackingAuthorizationStatus) to determine the user’s intent.

For more information about asking users for permission to track, see [`User Privacy and Data Use`](https://developer.apple.comhttps://developer.apple.com/app-store/user-privacy-and-data-use/).

## See Also

- [class func shared() -> ASIdentifierManager](asidentifiermanager/shared.md)
  The shared instance of the identifier manager class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adsupport/asidentifiermanager/advertisingidentifier)*