# delegate

**Framework**: AVRouting  
**Kind**: property  
**Role**: Instance Property

A delegate object for a routing controller.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any AVCustomRoutingControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<AVCustomRoutingControllerDelegate> delegate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller/delegate)*