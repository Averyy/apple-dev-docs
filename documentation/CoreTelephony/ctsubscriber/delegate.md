# delegate

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

A delegate that receives updates on the subscriber information.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 12.1+

## Declaration

```swift
weak var delegate: (any CTSubscriberDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<CTSubscriberDelegate> delegate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctsubscriber/delegate)*