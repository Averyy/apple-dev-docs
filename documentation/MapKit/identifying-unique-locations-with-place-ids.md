# Identifying unique locations with Place IDs

**Framework**: MapKit

Obtain information about a point of interest that persists over its lifetime.

#### Overview

[`MapKit for AppKit and UIKit`](mapkit-for-appkit-and-uikit.md), [`MapKit JS`](https://developer.apple.com/documentation/MapKitJS), and [`Apple Maps Server API`](https://developer.apple.com/documentation/AppleMapsServerAPI) provide a way for you to store and share references to places that matter to your application: the Place ID. A Place ID is an opaque string that semantically represents references to points of interest in the world, rather than particular coordinates or addresses.

A Place ID is a great feature for referencing a place’s information, even after that place’s information changes. Place IDs are also useful for displaying a place on a map. Use Place IDs to maintain unique collections of places that are important to your app.

> **Note**:  Place IDs are exempt from the storage restrictions in Section 2.5 of Attachment 6 to the [`Apple Developer Program License Agreement`](https://developer.apple.comhttps://developer.apple.com/support/terms/apple-developer-program-license-agreement/).

##### Obtain a Place Id

You obtain a Place ID by using Geocoder Lookup, Search, Search Autocomplete, Point-of-Interest Search, or choosing a place from Maps. You can also use a Place ID as a primary key or as part of a composite key in a database, or share Place IDs with other apps.

[`MKMapItem`](mkmapitem.md) in MapKit for AppKit and UIKit, [`Place`](https://developer.apple.com/documentation/MapKitJS/Place) in MapKit JS, and [`Place`](https://developer.apple.com/documentation/AppleMapsServerAPI/Place) objects in Apple Maps Server API include Place IDs that you can read and store. Additionally, you can obtain Place IDs for specific points of interest interactively from [`Place ID Lookup`](https://developer.apple.comhttps://developer.apple.com/maps/place-id-lookup/).

##### Look Up Referenced Place Information

All MapKit platforms support using a Place ID to obtain the referenced place’s latest information, whether by issuing an [`MKMapItemRequest`](mkmapitemrequest.md) in MapKit for AppKit and UIKit, a [`mapkit.PlaceLookup`](https://developer.apple.com/documentation/MapKitJS/mapkit.PlaceLookup) in MapKit JS, or a [`Search for places using mulitple identifiers`](https://developer.apple.com/documentation/AppleMapsServerAPI/-v1-place) request in Apple Maps Server API. These always return the most recent information for the place that the Place ID refers to, even if that information changed since you originally obtained it. You don’t have to track these changes or even update the stored Place ID.

A once-valid Place ID might fail to resolve from a lookup. However, this only happens when the referred place is no longer pertinent to Apple Maps. For instance, lookup failure might occur if a place has long been closed or simply no longer exists in the world in any meaningful way.

##### Display a Referenced Place

Use Place IDs to display annotations with [`MKMapItemAnnotation`](mkmapitemannotation.md) from MapKit for AppKit and UIKit or [`mapkit.PlaceAnnotation`](https://developer.apple.com/documentation/MapKitJS/mapkit.PlaceAnnotation) from MapKit JS.  You can also use Place IDs to show more detailed selection accessories, such as popups that automatically display a place’s name, address, hours, and more, with [`MKSelectionAccessory`](mkselectionaccessory.md) from MapKit for AppKit and UIKit and [`mapkit.PlaceSelectionAccessory`](https://developer.apple.com/documentation/MapKitJS/mapkit.PlaceSelectionAccessory) from MapKit JS.

##### Maintain a Unique Collection of Places

Although Place IDs themselves are unique, they might not uniquely refer to a place. Multiple different Place IDs might refer to the same place. Because of this, storing collections of  Place IDs, where each Place ID refers to a unique place (for example, a user’s favorite place list that shouldn’t contain the same place twice) is more complicated than simply making sure that each ID is bitwise-unique with every other ID in the set.

To aid with this task, place objects don’t just contain a Place ID in [`identifier`](mkmapitem/identifier-swift.property.md). They also contain a set of alternate Place IDs. For [`MapKit for AppKit and UIKit`](mapkit-for-appkit-and-uikit.md) it’s [`alternateIdentifiers`](mkmapitem/alternateidentifiers.md), and for [`MapKit JS`](https://developer.apple.com/documentation/MapKitJS) it’s [`alternateIds`](https://developer.apple.com/documentation/mapkitjs/place/4408163-alternateids). This list is a nonexhaustive set of alternate Place IDs referring to the place.

This list is critical in maintaining a set of Place IDs that refer to unique places. When adding a new Place ID to an existing set of Place IDs meant to refer to unique places, consult the list of alternate Place IDs for the new Place ID. If your set already contains any of the alternate Place IDs, don’t add the new Place ID to the set because it would be a duplicate.

The procedure of checking for the presence of alternate Place IDs before insertion into an existing set works to minimize duplicate references. However, in rare cases, because alternate Place ID lists aren’t exhaustive, duplicates might occasionally occur. Ensure that your set of Place IDs doesn’t contain two Place IDs that refer to the same place by performing the following steps:

1. Create an empty set of Place IDs. This is the temporary set.
2. For each Place ID, look up its alternate IDs and check if the temporary set contains either the Place ID itself or any of its alternates. If the existing set already contains any of those IDs, remove the Place ID from the existing set, as it’s a duplicate. Otherwise, add the Place ID and all alternates to the temporary set.

After you’ve completed the above steps, delete the temporary set you used to ensure that there were no duplicates amongst Place IDs and their alternates. The existing set now has all duplicates removed.

To maintain performance, use these steps to perform de-duplication on a periodic basis. Alternatively, use Apple Maps Server API’s [`Obtain a list of alternate place identifiers`](https://developer.apple.com/documentation/AppleMapsServerAPI/-v1-place-alternateIds) for an efficient way of performing de-duplication.

## See Also

- [Enabling Maps capability in Xcode](enabling-maps-capability-in-xcode.md)
  Configure your routing app to support providing directions.
- [class MKMapView](mkmapview.md)
  An embeddable map interface, similar to the one that the Maps app provides.
- [class MKMapItem](mkmapitem.md)
  A point of interest on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/identifying-unique-locations-with-place-ids)*