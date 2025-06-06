# geocodeAddressString(_:in:preferredLocale:completionHandler:)

**Framework**: Core Location  
**Kind**: method

Submits a forward-geocoding requesting using the specified address string and locale information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- watchOS 4.0+

## Declaration

```swift
func geocodeAddressString(_ addressString: String, in region: CLRegion?, preferredLocale locale: Locale?) async throws -> [CLPlacemark]
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func geocodeAddressString(_ addressString: String, in region: CLRegion?, preferredLocale locale: Locale?) async throws -> [CLPlacemark]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func geocodeAddressString(_ addressString: String, in region: CLRegion?, preferredLocale locale: Locale?) async throws -> [CLPlacemark]
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method submits the specified location data to the geocoding server asynchronously and returns. When the request completes, the geocoder executes the provided completion handler on the main thread.

After initiating a forward-geocoding request, do not attempt to initiate another reverse- or forward-geocoding request. Geocoding requests are rate-limited for each app, so making too many requests in a short period of time may cause some of the requests to fail. When the maximum rate is exceeded, the geocoder passes an error object with the value [`network`](clerror-swift.struct/network.md) to your completion handler.

## Parameters

- `addressString`: A string describing the location you want to look up. For example, you could specify the string “1 Infinite Loop, Cupertino, CA” to locate Apple headquarters.
- `region`: A geographical region to use as a hint when looking up the specified address. Specifying a region lets you prioritize the returned set of results to locations that are close to some specific geographical area, which is typically the user’s current location. If the application is authorized for location services and you specify   for this parameter, the set of results is prioritized based on the user’s approximate location. Calling this method does not trigger a location services authorization request.
- `locale`: The locale of the address string. Specify   to use the current locale of the user.
- `completionHandler`: The handler block to execute with the results. The geocoder executes this handler regardless of whether the request was successful or unsuccessful. For more information on the format of this block, see  .

## See Also

- [func geocodeAddressString(String, completionHandler: CLGeocodeCompletionHandler)](clgeocoder/geocodeaddressstring(_:completionhandler:).md)
  Submits a forward-geocoding request using the specified string.
- [func geocodeAddressString(String, in: CLRegion?, completionHandler: CLGeocodeCompletionHandler)](clgeocoder/geocodeaddressstring(_:in:completionhandler:).md)
  Submits a forward-geocoding request using the specified string and region information.
- [func geocodePostalAddress(CNPostalAddress, completionHandler: CLGeocodeCompletionHandler)](clgeocoder/geocodepostaladdress(_:completionhandler:).md)
  Submits a forward-geocoding requesting using the specified Contacts framework information.
- [func geocodePostalAddress(CNPostalAddress, preferredLocale: Locale?, completionHandler: CLGeocodeCompletionHandler)](clgeocoder/geocodepostaladdress(_:preferredlocale:completionhandler:).md)
  Submits a forward-geocoding requesting using the specified locale and Contacts framework information.
- [func geocodeAddressDictionary([AnyHashable : Any], completionHandler: CLGeocodeCompletionHandler)](clgeocoder/geocodeaddressdictionary(_:completionhandler:).md)
  Submits a forward-geocoding request using the specified address dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clgeocoder/geocodeaddressstring(_:in:preferredlocale:completionhandler:))*