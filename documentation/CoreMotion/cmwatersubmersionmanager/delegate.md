# delegate

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The object that receives updates about submersion data and events.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
weak var delegate: (any CMWaterSubmersionManagerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<CMWaterSubmersionManagerDelegate> delegate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/delegate)*