# Converting a user’s location to a descriptive placemark

**Framework**: Core Location

Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.

#### Overview

You can show a user’s location on a map in order to orient them to elements of your app that use map content. For instance, a user’s current location can be a point of reference for retrieving search results or calculating directions. Additionally, you can display location information outside of the map, such as a search field pre-filled with the user’s current city or street address. To provide this information in your app, configure your map view to display the user’s location, and then translate the location to informative, user-friendly data.

##### Display the User Location Annotation

To provide user-friendly place information, configure your map view to display the user’s current location by enabling [`showsUserLocation`](https://developer.apple.com/documentation/MapKit/MKMapView/showsUserLocation). After enabling this property, the map delegate begins receiving updates to the user’s location, represented with a [`MKUserLocation`](https://developer.apple.com/documentation/MapKit/MKUserLocation) object, through [`mapView(_:didUpdate:)`](https://developer.apple.com/documentation/MapKit/MKMapViewDelegate/mapView(_:didUpdate:)).

##### Geocode the User Location Annotation

[`CLPlacemark`](clplacemark.md) objects represent user place names, and include properties for street name, city name, country or region name, and many other location identifiers. When [`mapView(_:didUpdate:)`](https://developer.apple.com/documentation/MapKit/MKMapViewDelegate/mapView(_:didUpdate:)) receives updates on the user’s location, convert the [`MKUserLocation`](https://developer.apple.com/documentation/MapKit/MKUserLocation) object to a [`CLPlacemark`](clplacemark.md) by reverse geocoding the [`location`](https://developer.apple.com/documentation/MapKit/MKUserLocation/location) property with a [`CLGeocoder`](clgeocoder.md). Readable descriptions of the user’s location are available as properties on the placemark, such as the city information stored in the [`locality`](clplacemark/locality.md) property.

> ❗ **Important**:  Geocoding requests are rate-limited for each app. Issue new geocoding requests only when the user has moved a significant distance and after a reasonable amount of time has passed.

 Geocoding requests are rate-limited for each app. Issue new geocoding requests only when the user has moved a significant distance and after a reasonable amount of time has passed.

```swift
func mapView(_ mapView: MKMapView, didUpdate userLocation: MKUserLocation) {
        guard let newLocation = userLocation.location else { return }
        
        let currentTime = Date()
        let lastLocation = self.currentLocation
        self.currentLocation = newLocation
        
        // Only get new placemark information if you don't have a previous location,
        // if the user has moved a meaningful distance from the previous location, such as 1000 meters,
        // and if it's been 60 seconds since the last geocode request.
        if let lastLocation = lastLocation,
            newLocation.distance(from: lastLocation) <= 1000,
            let lastTime = lastGeocodeTime,
            currentTime.timeIntervalSince(lastTime) < 60 {
            return
        }
        
        // Convert the user's location to a user-friendly place name by reverse geocoding the location.
        lastGeocodeTime = currentTime
        geocoder.reverseGeocodeLocation(newLocation) { (placemarks, error) in
            guard error == nil else {
                self.handleError(error)
                return
            }
            
            // Most geocoding requests contain only one result.
            if let firstPlacemark = placemarks?.first {
                self.mostRecentPlacemark = firstPlacemark
                self.currentCity = firstPlacemark.locality
            }
        }
    }
```

#### See Also

##### Related Documentation

- [`Converting between coordinates and user-friendly place names`](converting-between-coordinates-and-user-friendly-place-names.md)

## See Also

- [Converting between coordinates and user-friendly place names](converting-between-coordinates-and-user-friendly-place-names.md)
  Convert between a latitude and longitude pair and a more user-friendly description of that location.
- [class CLGeocoder](clgeocoder.md)
  An interface for converting between geographic coordinates and place names.
- [class CLPlacemark](clplacemark.md)
  A user-friendly description of a geographic coordinate, often containing the name of the place, its address, and other relevant information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/converting-a-user-s-location-to-a-descriptive-placemark)*