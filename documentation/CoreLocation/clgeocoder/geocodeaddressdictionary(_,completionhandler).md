# geocodeAddressDictionary(_:completionHandler:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Submits a forward-geocoding request using the specified address dictionary.

**Availability**:
- iOS 5.0+ - Deprecated in 11.0
- iPadOS 5.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0
- watchOS 1.0+ - Deprecated in 4.0

> **Deprecated**: Use [`geocodePostalAddress(_:preferredLocale:completionHandler:)`](./geocodepostaladdress%28_,preferredlocale,completionhandler%29.md) or [`geocodePostalAddress(_:completionHandler:)`](./geocodepostaladdress%28_,completionhandler%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS*

```swift
func geocodeAddressDictionary(_ addressDictionary: [AnyHashable : Any], completionHandler: @escaping @Sendable ([CLPlacemark]?, (any Error)?) -> Void)
```

*Mac Catalyst*

```swift
func geocodeAddressDictionary(_ addressDictionary: [AnyHashable : Any]) async throws -> [CLPlacemark]
```

```objc
- (void) geocodeAddressDictionary:(NSDictionary *) addressDictionary completionHandler:(CLGeocodeCompletionHandler) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func geocodeAddressDictionary(_ addressDictionary: [AnyHashable : Any]) async throws -> [CLPlacemark]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

This method submits the specified location data to the geocoding server asynchronously and returns. Your completion handler block will be executed on the main thread.

After initiating a forward-geocoding request, do not attempt to initiate another forward- or reverse-geocoding request. Geocoding requests are rate-limited for each app, so making too many requests in a short period of time may cause some of the requests to fail. When the maximum rate is exceeded, the geocoder passes an error object with the value [`CLError.Code.network`](../clerror-swift.struct/code/network.md) to your completion handler.

## Parameters

- `addressDictionary`: An Address Book dictionary containing information about the address to look up.
- `completionHandler`: A block object containing the code to execute at the end of the request. This code is called whether the request is successful or unsuccessful.

## See Also

### Geocoding an address
- [func geocodeAddressString(String, in: CLRegion?, preferredLocale: Locale?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](./geocodeaddressstring%28_,in,preferredlocale,completionhandler%29.md)
  Submits a forward-geocoding requesting using the specified address string and locale information.
- [func geocodeAddressString(String, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](./geocodeaddressstring%28_,completionhandler%29.md)
  Submits a forward-geocoding request using the specified string.
- [func geocodeAddressString(String, in: CLRegion?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](./geocodeaddressstring%28_,in,completionhandler%29.md)
  Submits a forward-geocoding request using the specified string and region information.
- [func geocodePostalAddress(CNPostalAddress, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](./geocodepostaladdress%28_,completionhandler%29.md)
  Submits a forward-geocoding requesting using the specified Contacts framework information.
- [func geocodePostalAddress(CNPostalAddress, preferredLocale: Locale?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](./geocodepostaladdress%28_,preferredlocale,completionhandler%29.md)
  Submits a forward-geocoding requesting using the specified locale and Contacts framework information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clgeocoder/geocodeaddressdictionary(_:completionhandler:))*