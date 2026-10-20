# delegate

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A delegate that receives incoming call information from the provider.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any NEAppPushDelegate)? { get set }
```

```objc
@property (weak, readwrite, nullable) id<NEAppPushDelegate> delegate;
```

## See Also

### Working with a delegate
- [protocol NEAppPushDelegate](../neapppushdelegate.md)
  A protocol that defines how an app push manager instance interacts with the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/delegate)*