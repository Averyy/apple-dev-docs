# updatePostbackConversionValue(_:coarseValue:completionHandler:)

**Framework**: StoreKit  
**Kind**: method

Updates the fine and coarse conversion values, and calls a completion handler if the update fails.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+

## Declaration

```swift
class func updatePostbackConversionValue(_ fineValue: Int, coarseValue: SKAdNetwork.CoarseConversionValue) async throws
```

## Mentions

- [SKAdNetwork 4 release notes](skadnetwork-4-release-notes.md)
- [Receiving postbacks in multiple conversion windows](receiving-postbacks-in-multiple-conversion-windows.md)
- [Configuring an advertised app](configuring-an-advertised-app.md)

#### Discussion

Call this method when the user first launches an app to register the app installation, and optionally again, to update conversion values as the user engages with the app.

This method is identical to calling [`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:coarsevalue:lockwindow:completionhandler:).md) with the `lockWindow` parameter set to `false`.

This method returns [`SKANError.Code.invalidConversionValue`](skanerror-swift.struct/code/invalidconversionvalue.md) if the `fineValue` is outside of the allowed range.

> ❗ **Important**:  The system ignores calls to this method if the `fineValue` is outside of the valid range. Valid conversion updates your app sends before or after an invalid conversion remain available.

## Parameters

- `fineValue`: An unsigned 6-bit value   and  . The app or the ad network defines the meaning of the conversion value.
- `coarseValue`: An   value. The app or the ad network defines the meaning of this value.
- `completion`: An optional completion handler you provide to catch and handle any errors this method encounters when you update a conversion value. Set this value to   if you don’t provide a handler.

## See Also

- [class func updatePostbackConversionValue(Int, coarseValue: SKAdNetwork.CoarseConversionValue, lockWindow: Bool, completionHandler: (((any Error)?) -> Void)?)](skadnetwork/updatepostbackconversionvalue(_:coarsevalue:lockwindow:completionhandler:).md)
  Updates the fine and coarse conversion values and indicates whether to send the postback before the conversion window ends, and calls a completion handler if the update fails.
- [SKAdNetwork.CoarseConversionValue](skadnetwork/coarseconversionvalue.md)
  Coarse values to use for updating conversion values.
- [class func updatePostbackConversionValue(Int, completionHandler: (((any Error)?) -> Void)?)](skadnetwork/updatepostbackconversionvalue(_:completionhandler:).md)
  Verifies the first launch of an advertised app and, on subsequent calls, updates the conversion value or calls a completion handler if the update fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadnetwork/updatepostbackconversionvalue(_:coarsevalue:completionhandler:))*