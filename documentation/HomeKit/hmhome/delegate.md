# delegate

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A delegate that receives updates on the state of the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
weak var delegate: (any HMHomeDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<HMHomeDelegate> delegate;
```

## See Also

### Keeping track of home configuration changes
- [protocol HMHomeDelegate](../hmhomedelegate.md)
  An interface that communicates changes to a home’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/delegate)*