# delegate

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A delegate that receives updates on the state of the accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
weak var delegate: (any HMAccessoryDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<HMAccessoryDelegate> delegate;
```

## See Also

### Tracking changes to an accessory
- [protocol HMAccessoryDelegate](../hmaccessorydelegate.md)
  A set of methods that defines the communication method for state updates from accessories to their delegates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/delegate)*