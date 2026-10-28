# isEqual(to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the configuration objects are equivalent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func isEqual(to otherConfiguration: UIImage.SymbolConfiguration?) -> Bool
```

```objc
- (BOOL) isEqualToConfiguration:(UIImageSymbolConfiguration *) otherConfiguration;
```

## Return Value

[`true`](../../../Swift/true.md) if the trait collections and image configuration values of both objects match; otherwise, [`false`](../../../Swift/false.md).

## Parameters

- `otherConfiguration`: The other configuration object. Specify `nil` to compare the current configuration object to the configuration object in the [`unspecified`](./unspecified.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/isequal(to:))*