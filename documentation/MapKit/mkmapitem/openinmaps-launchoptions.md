# openInMaps(launchOptions:)

**Framework**: MapKit  
**Kind**: method

Opens the Maps app and displays the map item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func openInMaps(launchOptions: [String : Any]? = nil) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the Maps app successfully opens the map item, or [`false`](https://developer.apple.com/documentation/swift/false) if there’s an error.

#### Discussion

You use this method to pass the map item to the Maps app. If your map item contains descriptive information about the location (such as a name or URL), the Maps app displays that information at the specified coordinate.

If you specify the [`MKLaunchOptionsDirectionsModeKey`](mklaunchoptionsdirectionsmodekey.md) option in the `launchOptions` dictionary, the Maps app interprets that as an attempt to map from the user’s current location to the location that the map item specifies.

> **Note**:  This is a blocking call and the system suspends interaction with your app until the Maps app finishes launching.

If you don’t include the [`MKLaunchOptionsMapCenterKey`](mklaunchoptionsmapcenterkey.md) and [`MKLaunchOptionsMapSpanKey`](mklaunchoptionsmapspankey.md) keys in your `launchOptions` dictionary, the Maps app constructs a region around the map item. It uses that region to set the visible portion of the map.

## Parameters

- `launchOptions`: This parameter may be  .

## See Also

- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?) -> Bool](mkmapitem/openmaps(with:launchoptions:).md)
  Opens the Maps app and displays the specified map items.
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openmaps(with:launchoptions:completionhandler:).md)
  Opens the Maps app using the specified map items and options.
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?, from: UIScene?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openmaps(with:launchoptions:from:completionhandler:).md)
  Opens the Maps app from a particular scene using the specified map items and options.
- [func openInMaps(launchOptions: [String : Any]?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openinmaps(launchoptions:completionhandler:).md)
  Opens the Maps app and displays the map item.
- [func openInMaps(launchOptions: [String : Any]?, from: UIScene?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openinmaps(launchoptions:from:completionhandler:).md)
  Opens the Maps app from a particular scene using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/openinmaps(launchoptions:))*