# NSConnectionDidInitializeNotification

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

Posted when an `NSConnection` object is initialized using [`initWithReceivePort:sendPort:`](./nsconnection/initwithreceiveport_sendport_.md) (the designated initializer for `NSConnection`). The notification object is the `NSConnection` object. This notification does not contain a `userInfo` dictionary.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```c
extern NSString * const NSConnectionDidInitializeNotification;
```

#### Discussion

## See Also

### Related Documentation
- [- initWithReceivePort:sendPort:](./nsconnection/initwithreceiveport_sendport_.md)
  Returns an `NSConnection` object initialized with given send and receive ports.
### Notifications
- [NSConnectionDidDieNotification](./nsconnectiondiddienotification.md)
  Posted when an `NSConnection` object is deallocated or when it’s notified that its `NSPort` object has become invalid. The notification object is the `NSConnection` object. This notification does not contain a `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnectiondidinitializenotification)*