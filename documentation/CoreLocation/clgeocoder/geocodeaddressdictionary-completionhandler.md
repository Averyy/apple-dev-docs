# geocodeAddressDictionary(_:completionHandler:)

**Framework**: Core Location  
**Kind**: method

Submits a forward-geocoding request using the specified address dictionary.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func geocodeAddressDictionary(_ addressDictionary: [AnyHashable : Any]) async throws -> [CLPlacemark]
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func geocodeAddressDictionary(_ addressDictionary: [AnyHashable : Any]) async throws -> [CLPlacemark]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method submits the specified location data to the geocoding server asynchronously and returns. Your completion handler block will be executed on the main thread.

After initiating a forward-geocoding request, do not attempt to initiate another forward- or reverse-geocoding request. Geocoding requests are rate-limited for each app, so making too many requests in a short period of time may cause some of the requests to fail. When the maximum rate is exceeded, the geocoder passes an error object with the value [`CLError.Code.network`](clerror-swift.struct/code/network.md) to your completion handler.

## Parameters

- `addressDictionary`: An Address Book dictionary containing information about the address to look up.
- `completionHandler`: A block object containing the code to execute at the end of the request. This code is called whether the request is successful or unsuccessful.

## See Also

- [func geocodeAddressString(String, in: CLRegion?, preferredLocale: Locale?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodeaddressstring(_:in:preferredlocale:completionhandler:).md)
  Submits a forward-geocoding requesting using the specified address string and locale information.
- [func geocodeAddressString(String, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodeaddressstring(_:completionhandler:).md)
  Submits a forward-geocoding request using the specified string.
- [func geocodeAddressString(String, in: CLRegion?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodeaddressstring(_:in:completionhandler:).md)
  Submits a forward-geocoding request using the specified string and region information.
- [func geocodePostalAddress(CNPostalAddress, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodepostaladdress(_:completionhandler:).md)
  Submits a forward-geocoding requesting using the specified Contacts framework information.
- [func geocodePostalAddress(CNPostalAddress, preferredLocale: Locale?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodepostaladdress(_:preferredlocale:completionhandler:).md)
  Submits a forward-geocoding requesting using the specified locale and Contacts framework information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clgeocoder/geocodeaddressdictionary(_:completionhandler:))*