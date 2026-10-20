# delegate

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The object that receives headphone motion manager events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- watchOS 7.0+

## Declaration

```swift
weak var delegate: (any CMHeadphoneMotionManagerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<CMHeadphoneMotionManagerDelegate> delegate;
```

## See Also

### Getting the Delegate
- [protocol CMHeadphoneMotionManagerDelegate](../cmheadphonemotionmanagerdelegate.md)
  A set of methods that defines an interface for connecting and disconnecting headphones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/delegate)*