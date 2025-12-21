# openMaps(with:launchOptions:)

**Framework**: MapKit  
**Kind**: method

Opens the Maps app and displays the specified map items.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func openMaps(with mapItems: [MKMapItem], launchOptions: [String : Any]? = nil) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the Maps app successfully opens the maps items, or [`false`](https://developer.apple.com/documentation/Swift/false) if there’s an error.

#### Discussion

You use this method to pass one or more map items to the Maps app. For example, you might use this method to ask the Maps app to display location-based search results that your app generates. The Maps app displays pins at each location you specify and uses the contents of each map item object to display additional information.

If you specify the [`MKLaunchOptionsDirectionsModeKey`](mklaunchoptionsdirectionsmodekey.md) option in the `launchOptions` dictionary, the `mapItems` array may have no more than two items in it. If the array contains one item, the Maps app generates directions from the user’s location to the location that the map item specifies. If the array contains two items, the Maps app generates directions from the location of the first item to the location of the second item in the array.

If you don’t include the [`MKLaunchOptionsMapCenterKey`](mklaunchoptionsmapcenterkey.md) and [`MKLaunchOptionsMapSpanKey`](mklaunchoptionsmapspankey.md) keys in your `launchOptions` dictionary, the Maps app constructs a region that encompasses the provided items. It uses this region to set the visible portion of the map.

## Parameters

- `mapItems`: An array containing one or more   objects representing the items you want to display on the map.
- `launchOptions`: You may specify   for this parameter.

## See Also

- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openmaps(with:launchoptions:completionhandler:).md)
  Opens the Maps app using the specified map items and options.
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?, from: UIScene?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openmaps(with:launchoptions:from:completionhandler:).md)
  Opens the Maps app from a particular scene using the specified map items and options.
- [func openInMaps(launchOptions: [String : Any]?) -> Bool](mkmapitem/openinmaps(launchoptions:).md)
  Opens the Maps app and displays the map item.
- [func openInMaps(launchOptions: [String : Any]?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openinmaps(launchoptions:completionhandler:).md)
  Opens the Maps app and displays the map item.
- [func openInMaps(launchOptions: [String : Any]?, from: UIScene?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openinmaps(launchoptions:from:completionhandler:).md)
  Opens the Maps app from a particular scene using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/openmaps(with:launchoptions:))*