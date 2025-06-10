# Displaying place information using the Maps Embed API

**Framework**: MapKit JS

Show place information on a map using a URL.

#### Overview

You can use the Maps Embed API to show information about a place within the context of a map by copying an HTML snippet onto your website. This is a minimal code approach to showcasing place information. All you need is the following:

1. The ID for your place. See [`Identifying unique locations with Place IDs`](https://developer.apple.com/documentation/MapKit/identifying-unique-locations-with-place-ids) for more information about Place IDs, or find one with [`Place ID Lookup`](https://developer.apple.comhttps://developer.apple.com/maps/place-id-lookup).
2. Your API token. See [`Creating a Maps token`](creating-a-maps-token.md) for more information on how to request a token.

Once you have these items, create the HTML snippet using [`Create a Map`](https://developer.apple.comhttps://developer.apple.com/maps/create-a-map/), then copy the resulting HTML snippet and paste it onto your website.

Alternatively, you can construct the snippet yourself by manually adjusting the URL parameters in the snippet’s `iframe SRC` attribute.

> **Note**:  For greater control over the presentation style of the Place Card and map, use [`mapkit.PlaceDetail`](mapkit.placedetail.md).

![A screenshot showing the Place Card for the Apple Park Visitor Center above a map of the area. The hours of operation, website, phone number, and address are in the Place Card.](https://docs-assets.developer.apple.com/published/c3e6646de27b9b9915804b9b27b64218/displaying-place-information-using-the-maps-embed-api-01%402x.png)

## See Also

- [Creating a Maps token](creating-a-maps-token.md)
  Generate your token to access MapKit services with proper authorization.
- [Loading the latest version of MapKit JS](loading-the-latest-version-of-mapkit-js.md)
  Link to the most recent autoupdating version of MapKit JS, or a version of your choice.
- [mapkit](mapkit.md)
  The JavaScript API for embedding Apple Maps on your website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/displaying-place-information-using-the-maps-embed-api)*