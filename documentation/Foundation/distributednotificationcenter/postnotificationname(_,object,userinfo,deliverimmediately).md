# postNotificationName(_:object:userInfo:deliverImmediately:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func postNotificationName(_ name: NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]? = nil, deliverImmediately: Bool)
```

```objc
- (void) postNotificationName:(NSNotificationName) name object:(NSString *) object userInfo:(NSDictionary *) userInfo deliverImmediately:(BOOL) deliverImmediately;
```

#### Discussion

This is the preferred method for posting notifications.

The `notificationInfo` dictionary is serialized as a property list, so it can be passed to another task. In the receiving task, it is deserialized back into a dictionary. This serialization imposes some restrictions on the objects that can be placed in the `notificationInfo` dictionary. See XML Property Lists for details.

## Parameters

- `name`: Name of the notification to post. Must not be `nil`.
- `object`: Sender of the notification. May be `nil`.
- `userInfo`: Dictionary containing additional information. May be `nil`.

  > ❗ **Important**:  Sandboxed apps can send notifications only if they do not contain a dictionary. If the sending application is in an App Sandbox, `userInfo` *must* be `nil`.
- `deliverImmediately`: Specifies when to deliver the notification. When [`false`](../../Swift/false.md), the receiver delivers notifications to their observers according to the suspended-notification behavior specified in the corresponding dispatch table entry. When [`true`](../../Swift/true.md), the receiver delivers the notification immediately to its observers.

## See Also

### Related Documentation
- [class func unarchiveObject(with: Data) -> Any?](../nsunarchiver/unarchiveobject%28with%29.md)
  Decodes and returns the object archived in a given `NSData` object.
- [func encodeRootObject(Any)](../nsarchiver/encoderootobject%28_%29.md)
  Archives a given object along with all the objects to which it is connected.
### Posting Notifications
- [func post(name: NSNotification.Name, object: String?)](./post%28name,object%29.md)
  Creates a notification, and posts it to the receiver.
- [func post(name: NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?)](./post%28name,object,userinfo%29.md)
  Creates a notification with information, and posts it to the receiver.
- [func postNotificationName(NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?, options: DistributedNotificationCenter.Options)](./postnotificationname%28_,object,userinfo,options%29.md)
  Creates a notification with information, and posts it to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/postnotificationname(_:object:userinfo:deliverimmediately:))*