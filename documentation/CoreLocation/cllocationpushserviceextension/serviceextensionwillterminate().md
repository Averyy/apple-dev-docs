# serviceExtensionWillTerminate()

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Notifies your app extension that the system is about to terminate the extension because it’s taking too long to complete its task.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
optional func serviceExtensionWillTerminate()
```

```objc
- (void) serviceExtensionWillTerminate;
```

#### Discussion

If your [`didReceiveLocationPushPayload(_:completion:)`](./didreceivelocationpushpayload%28_,completion%29.md) method takes too long to collect a location and call its completion block, the system calls this method on the main thread. Use this method to execute the completion block from [`didReceiveLocationPushPayload(_:completion:)`](./didreceivelocationpushpayload%28_,completion%29.md) as quickly as possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceextension/serviceextensionwillterminate())*