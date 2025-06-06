# NEAppPushDelegate

**Framework**: Network Extension  
**Kind**: protocol

A protocol that defines how an app push manager instance interacts with the framework.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol NEAppPushDelegate : NSObjectProtocol
```

## Topics

### Receiving calls
- [func appPushManager(NEAppPushManager, didReceiveIncomingCallWithUserInfo: [AnyHashable : Any])](neapppushdelegate/apppushmanager(_:didreceiveincomingcallwithuserinfo:).md)
  A delegate method that the framework invokes when the provider reports an incoming call.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any NEAppPushDelegate)?](neapppushmanager/delegate.md)
  A delegate that receives incoming call information from the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushdelegate)*