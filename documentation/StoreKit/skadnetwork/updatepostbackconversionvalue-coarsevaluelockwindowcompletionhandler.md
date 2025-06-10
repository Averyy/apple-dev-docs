# updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)

**Framework**: StoreKit  
**Kind**: method

Updates the fine and coarse conversion values and indicates whether to send the postback before the conversion window ends, and calls a completion handler if the update fails.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+

## Declaration

```swift
class func updatePostbackConversionValue(_ fineValue: Int, coarseValue: SKAdNetwork.CoarseConversionValue, lockWindow: Bool) async throws
```

## Mentions

- [Receiving postbacks in multiple conversion windows](receiving-postbacks-in-multiple-conversion-windows.md)
- [SKAdNetwork 4 release notes](skadnetwork-4-release-notes.md)
- [Identifying the parameters in install-validation postbacks](identifying-the-parameters-in-install-validation-postbacks.md)
- [Receiving ad attributions and postbacks](receiving-ad-attributions-and-postbacks.md)
- [Configuring an advertised app](configuring-an-advertised-app.md)

#### Discussion

Call this method when the user first launches an app to register the app installation, and again to update conversion values as the user engages with the app. It’s up to your app to decide what the conversion values signify in your app, both the `fineValue` and the `coarseValue`.

This method supports ads signed with any verison of SKAdNetwork, and you can use it instead of calling [`updatePostbackConversionValue(_:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:completionhandler:).md) and [`updatePostbackConversionValue(_:coarseValue:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:coarsevalue:completionhandler:).md). The system automatically determines the method’s behavior based on the ad’s version, as the following sections describe — the app doesn’t need to know the ad version. To take advantage of the multiple postbacks available starting in version 4, use this method or [`updatePostbackConversionValue(_:coarseValue:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:coarsevalue:completionhandler:).md).

This method returns [`SKANError.Code.invalidConversionValue`](skanerror-swift.struct/code/invalidconversionvalue.md) if the `fineValue` is outside of the allowed range.

> ❗ **Important**:  The system ignores calls to this method if the `fineValue` is outside of the valid range. Valid conversion updates your app sends before or after an invalid conversion remain available.

##### Update Conversion Values for Ads Signed with Skadnetwork 4 or Later

For ads that ad networks sign using version 4 or later, calling this method behaves as follows:

- Both the `fineValue` and `coarseValue` represent conversion values. The method ignores the `fineValue` after the first conversion window.
- Setting the `lockWindow` parameter to `true` indicates a final update for the conversion value for the current conversion window. The system ignores additional calls to update the conversion value until the end of the conversion window.
- Setting the `lockWindow` parameter to `false` continues updating the conversion value throughout the conversion window.

For information about the data you may receive in postbacks, see [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md).

##### Update Conversion Values for Ads Signed with Skadnetwork 3 or Earlier

For ads that ad networks sign using version 3 or earlier, calling this method behaves as follows:

- The `fineValue` represents the conversion value.
- The method ignores the `coarseValue` and `lockWindow` parameters.
- There’s a single conversion period that ends after a rolling 24-hour timer expires. The 24-hour timer restarts each time the app calls this method with a valid conversion value greater than the previous value. When the timer expires, the conversion value is final and subsequent calls to this method have no effect.
- The device sends the postback 0–24 hours after the timer expires.
- The postback contains the final conversion value only if the postback data tier contains the value.

For more information about SKAdNetwork versions, see [`SKAdNetwork release notes`](skadnetwork-release-notes.md).

## Parameters

- `fineValue`: An unsigned 6-bit value   and  . The app or the ad network defines the meaning of the fine conversion value.
- `coarseValue`: An   value of  ,  , or  . The app or the ad network defines the meaning of the coarse conversion value.
- `lockWindow`: A Boolean value that indicates whether to send the postback before the conversion window ends. Use   to tell the system to send the postback without waiting for the end of the conversion window. The default value is  .
- `completion`: An optional completion handler you provide to catch and handle any errors this method encounters when you update a conversion value. Set this value to   if you don’t provide a handler.

## See Also

- [class func updatePostbackConversionValue(Int, coarseValue: SKAdNetwork.CoarseConversionValue, completionHandler: (((any Error)?) -> Void)?)](skadnetwork/updatepostbackconversionvalue(_:coarsevalue:completionhandler:).md)
  Updates the fine and coarse conversion values, and calls a completion handler if the update fails.
- [SKAdNetwork.CoarseConversionValue](skadnetwork/coarseconversionvalue.md)
  Coarse values to use for updating conversion values.
- [class func updatePostbackConversionValue(Int, completionHandler: (((any Error)?) -> Void)?)](skadnetwork/updatepostbackconversionvalue(_:completionhandler:).md)
  Verifies the first launch of an advertised app and, on subsequent calls, updates the conversion value or calls a completion handler if the update fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadnetwork/updatepostbackconversionvalue(_:coarsevalue:lockwindow:completionhandler:))*