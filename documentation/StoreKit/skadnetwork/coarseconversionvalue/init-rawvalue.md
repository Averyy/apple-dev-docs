# init(rawValue:)

**Framework**: StoreKit  
**Kind**: init

Creates a coarse conversion value from the raw value.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+

## Declaration

```swift
init(rawValue: String)
```

#### Discussion

You don’t need to call the initializer to use coarse conversion values. When you provide the coarse conversion value to the [`updatePostbackConversionValue(_:coarseValue:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:coarsevalue:completionhandler:).md) or [`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:coarsevalue:lockwindow:completionhandler:).md) methods, use the static constants, [`low`](skadnetwork/coarseconversionvalue/low.md), [`medium`](skadnetwork/coarseconversionvalue/medium.md), or [`high`](skadnetwork/coarseconversionvalue/high.md).

## Parameters

- `rawValue`: A string that is one of   ,  , or  .

## See Also

- [static let high: SKAdNetwork.CoarseConversionValue](skadnetwork/coarseconversionvalue/high.md)
  A string constant value for indicating a high coarse conversion value.
- [static let low: SKAdNetwork.CoarseConversionValue](skadnetwork/coarseconversionvalue/low.md)
  A string constant value for indicating a low coarse conversion value.
- [static let medium: SKAdNetwork.CoarseConversionValue](skadnetwork/coarseconversionvalue/medium.md)
  A string constant value for indicating a medium coarse conversion value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadnetwork/coarseconversionvalue/init(rawvalue:))*