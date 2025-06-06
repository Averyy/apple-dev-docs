# delegate

**Framework**: HomeKit  
**Kind**: property

A delegate that receives updates on the collection of homes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
weak var delegate: (any HMHomeManagerDelegate)? { get set }
```

## See Also

- [protocol HMHomeManagerDelegate](hmhomemanagerdelegate.md)
  An interface the home manager uses to communicate changes to the state of the home network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/delegate)*