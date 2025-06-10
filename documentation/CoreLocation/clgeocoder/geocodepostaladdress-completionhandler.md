# geocodePostalAddress(_:completionHandler:)

**Framework**: Core Location  
**Kind**: method

Submits a forward-geocoding requesting using the specified Contacts framework information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func geocodePostalAddress(_ postalAddress: CNPostalAddress) async throws -> [CLPlacemark]
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func geocodePostalAddress(_ postalAddress: CNPostalAddress) async throws -> [CLPlacemark]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method submits the specified location data to the geocoding server asynchronously and returns. When the request completes, the geocoder executes the provided completion handler on the main thread.

After initiating a forward-geocoding request, do not attempt to initiate another reverse- or forward-geocoding request. Geocoding requests are rate-limited for each app, so making too many requests in a short period of time may cause some of the requests to fail. When the maximum rate is exceeded, the geocoder passes an error object with the value [`network`](clerror-swift.struct/network.md) to your completion handler.

## Parameters

- `postalAddress`: A postal address from the Contacts framework. The address should be specified in the user’s current locale.
- `completionHandler`: The handler block to execute with the results. The geocoder executes this handler regardless of whether the request was successful or unsuccessful. For more information on the format of this block, see  .

## See Also

- [func geocodeAddressString(String, in: CLRegion?, preferredLocale: Locale?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodeaddressstring(_:in:preferredlocale:completionhandler:).md)
  Submits a forward-geocoding requesting using the specified address string and locale information.
- [func geocodeAddressString(String, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodeaddressstring(_:completionhandler:).md)
  Submits a forward-geocoding request using the specified string.
- [func geocodeAddressString(String, in: CLRegion?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodeaddressstring(_:in:completionhandler:).md)
  Submits a forward-geocoding request using the specified string and region information.
- [func geocodePostalAddress(CNPostalAddress, preferredLocale: Locale?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodepostaladdress(_:preferredlocale:completionhandler:).md)
  Submits a forward-geocoding requesting using the specified locale and Contacts framework information.
- [func geocodeAddressDictionary([AnyHashable : Any], completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodeaddressdictionary(_:completionhandler:).md)
  Submits a forward-geocoding request using the specified address dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clgeocoder/geocodepostaladdress(_:completionhandler:))*