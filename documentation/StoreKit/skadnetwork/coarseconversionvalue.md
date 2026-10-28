# SKAdNetwork.CoarseConversionValue

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Coarse values to use for updating conversion values.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+

## Declaration

```swift
struct CoarseConversionValue
```

```c
typedef NSString * SKAdNetworkCoarseConversionValue;
```

## Mentions

- [SKAdNetwork 4 release notes](../skadnetwork-4-release-notes.md)

## Discussion

When you provide the coarse conversion value to the [`updatePostbackConversionValue(_:coarseValue:completionHandler:)`](./updatepostbackconversionvalue%28_,coarsevalue,completionhandler%29.md) or [`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`](./updatepostbackconversionvalue%28_,coarsevalue,lockwindow,completionhandler%29.md) methods, use the static constants [`low`](./coarseconversionvalue/low.md), [`medium`](./coarseconversionvalue/medium.md), or [`high`](./coarseconversionvalue/high.md).

These constants have no special meaning. The app or ad network can define their meaning, as is useful for their ad campaigns. The app is responsible for assigning a coarse conversion value, as well as the fine conversion value, when it calls one of the conversion value methods. You can determine how the coarse and fine conversion values relate to the types of conversion events you want to measure.

## Topics

### Providing coarse conversion values
- [static let high: SKAdNetwork.CoarseConversionValue](./coarseconversionvalue/high.md)
  A string constant value for indicating a high coarse conversion value.
- [static let low: SKAdNetwork.CoarseConversionValue](./coarseconversionvalue/low.md)
  A string constant value for indicating a low coarse conversion value.
- [static let medium: SKAdNetwork.CoarseConversionValue](./coarseconversionvalue/medium.md)
  A string constant value for indicating a medium coarse conversion value.
- [init(rawValue: String)](./coarseconversionvalue/init%28rawvalue%29.md)
  Creates a coarse conversion value from the raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Providing conversion information
- [class func updatePostbackConversionValue(Int, coarseValue: SKAdNetwork.CoarseConversionValue, lockWindow: Bool, completionHandler: (((any Error)?) -> Void)?)](./updatepostbackconversionvalue%28_,coarsevalue,lockwindow,completionhandler%29.md)
  Updates the fine and coarse conversion values and indicates whether to send the postback before the conversion window ends, and calls a completion handler if the update fails.
- [class func updatePostbackConversionValue(Int, coarseValue: SKAdNetwork.CoarseConversionValue, completionHandler: (((any Error)?) -> Void)?)](./updatepostbackconversionvalue%28_,coarsevalue,completionhandler%29.md)
  Updates the fine and coarse conversion values, and calls a completion handler if the update fails.
- [class func updatePostbackConversionValue(Int, completionHandler: (((any Error)?) -> Void)?)](./updatepostbackconversionvalue%28_,completionhandler%29.md)
  Verifies the first launch of an advertised app and, on subsequent calls, updates the conversion value or calls a completion handler if the update fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadnetwork/coarseconversionvalue)*