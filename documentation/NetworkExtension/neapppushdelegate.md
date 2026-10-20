# NEAppPushDelegate

**Framework**: Network Extension  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol NEAppPushDelegate <NSObject>
```

## Topics

### Receiving calls
- [func appPushManager(NEAppPushManager, didReceiveIncomingCallWithUserInfo: [AnyHashable : Any])](./neapppushdelegate/apppushmanager%28_,didreceiveincomingcallwithuserinfo%29.md)
  A delegate method that the framework invokes when the provider reports an incoming call.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with a delegate
- [var delegate: (any NEAppPushDelegate)?](./neapppushmanager/delegate.md)
  A delegate that receives incoming call information from the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushdelegate)*