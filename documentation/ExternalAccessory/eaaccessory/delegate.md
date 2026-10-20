# delegate

**Framework**: External Accessory  
**Kind**: property  
**Role**: Instance Property

The object that acts as the delegate of the accessory.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
unowned(unsafe) var delegate: (any EAAccessoryDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<EAAccessoryDelegate> delegate;
```

#### Discussion

The delegate receives notifications about changes to the status of the accessory object. The delegate must adopt the [`EAAccessoryDelegate`](../eaaccessorydelegate.md) protocol.

## See Also

### Responding to Disconnection Events
- [protocol EAAccessoryDelegate](../eaaccessorydelegate.md)
  A protocol that defines an optional method for receiving notifications when the associated accessory object is disconnected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessory/delegate)*