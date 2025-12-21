# requestTemporaryFullAccuracyAuthorization(withPurposeKey:)

**Framework**: Core Location  
**Kind**: method

Requests permission to temporarily use location services with full accuracy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func requestTemporaryFullAccuracyAuthorization(withPurposeKey purposeKey: String)
```

#### Discussion

This method behaves the same as calling the [`requestTemporaryFullAccuracyAuthorization(withPurposeKey:completion:)`](cllocationmanager/requesttemporaryfullaccuracyauthorization(withpurposekey:completion:).md) method, passing `nil` as the completion closure. Use this method if your app’s logic to respond to changes in location data accuracy is already handled by the [`locationManagerDidChangeAuthorization(_:)`](cllocationmanagerdelegate/locationmanagerdidchangeauthorization(_:).md) delegate method, and your app doesn’t have any work to do in the closure.

## Parameters

- `purposeKey`: A key in the   dictionary of the app’s   file.  The value for this key is an app-provided string that describes the reason for accessing location data with full accuracy.  To localize a usage description, add an entry to your   file with the same key you provide for this parameter.

## See Also

- [func requestWhenInUseAuthorization()](cllocationmanager/requestwheninuseauthorization.md)
  Requests the user’s permission to use location services while the app is in use.
- [func requestAlwaysAuthorization()](cllocationmanager/requestalwaysauthorization.md)
  Requests the user’s permission to use location services regardless of whether the app is in use.
- [func requestTemporaryFullAccuracyAuthorization(withPurposeKey: String, completion: (((any Error)?) -> Void)?)](cllocationmanager/requesttemporaryfullaccuracyauthorization(withpurposekey:completion:).md)
  Requests permission to temporarily use location services with full accuracy and reports the results to the provided completion handler.
- [var authorizationStatus: CLAuthorizationStatus](cllocationmanager/authorizationstatus-swift.property.md)
  The current authorization status for the app.
- [enum CLAuthorizationStatus](clauthorizationstatus.md)
  Constants that indicate the app’s authorization to use location services.
- [NSLocationDefaultAccuracyReduced](../BundleResources/Information-Property-List/NSLocationDefaultAccuracyReduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../BundleResources/Information-Property-List/NSLocationAlwaysAndWhenInUseUsageDescription.md)
  A message that tells people why the app is requesting access to their location information at all times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/requesttemporaryfullaccuracyauthorization(withpurposekey:))*