# delegate

**Framework**: HomeKit  
**Kind**: property

A delegate that HomeKit tells about changes in the state of network access.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
weak var delegate: (any HMNetworkConfigurationProfileDelegate)? { get set }
```

## See Also

- [protocol HMNetworkConfigurationProfileDelegate](hmnetworkconfigurationprofiledelegate.md)
  An interface that your app adopts to receive notifications about changes in the state of network access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmnetworkconfigurationprofile/delegate)*