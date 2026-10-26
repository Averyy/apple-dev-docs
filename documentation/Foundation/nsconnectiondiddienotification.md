# NSConnectionDidDieNotification

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

Posted when an `NSConnection` object is deallocated or when it’s notified that its `NSPort` object has become invalid. The notification object is the `NSConnection` object. This notification does not contain a `userInfo` dictionary.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```c
extern NSString * const NSConnectionDidDieNotification;
```

#### Discussion

An `NSConnection` object attached to a remote `NSSocketPort` object cannot detect when the remote port becomes invalid, even if the remote port is on the same machine. Therefore, it cannot post this notification when the connection is lost. Instead, you must detect the timeout error when the next message is sent.

The `NSConnection` object posting this notification is no longer useful, so all receivers should unregister themselves for any notifications involving the `NSConnection` object.

## See Also

### Related Documentation
- [class let didBecomeInvalidNotification: NSNotification.Name](./port/didbecomeinvalidnotification.md)
  Posted from the [`invalidate()`](./port/invalidate%28%29.md) method, which is invoked when the `NSPort` is deallocated or when it notices that its communication channel has been damaged. The notification object is the `NSPort` object that has become invalid. This notification does not contain a `userInfo` dictionary.
### Notifications
- [NSConnectionDidInitializeNotification](./nsconnectiondidinitializenotification.md)
  Posted when an `NSConnection` object is initialized using [`initWithReceivePort:sendPort:`](./nsconnection/initwithreceiveport_sendport_.md) (the designated initializer for `NSConnection`). The notification object is the `NSConnection` object. This notification does not contain a `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnectiondiddienotification)*