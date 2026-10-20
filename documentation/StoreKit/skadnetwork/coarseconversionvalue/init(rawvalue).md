# init(rawValue:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

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

You don’t need to call the initializer to use coarse conversion values. When you provide the coarse conversion value to the [`updatePostbackConversionValue(_:coarseValue:completionHandler:)`](../updatepostbackconversionvalue%28_,coarsevalue,completionhandler%29.md) or [`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`](../updatepostbackconversionvalue%28_,coarsevalue,lockwindow,completionhandler%29.md) methods, use the static constants, [`low`](./low.md), [`medium`](./medium.md), or [`high`](./high.md).

## Parameters

- `rawValue`: A string that is one of  [`low`](./low.md), [`medium`](./medium.md), or [`high`](./high.md).

## See Also

### Providing coarse conversion values
- [static let high: SKAdNetwork.CoarseConversionValue](./high.md)
  A string constant value for indicating a high coarse conversion value.
- [static let low: SKAdNetwork.CoarseConversionValue](./low.md)
  A string constant value for indicating a low coarse conversion value.
- [static let medium: SKAdNetwork.CoarseConversionValue](./medium.md)
  A string constant value for indicating a medium coarse conversion value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadnetwork/coarseconversionvalue/init(rawvalue:))*