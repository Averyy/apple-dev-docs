# postNotificationName(_:object:userInfo:deliverImmediately:)

**Framework**: Foundation  
**Kind**: method

Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func postNotificationName(_ name: NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]? = nil, deliverImmediately: Bool)
```

#### Discussion

This is the preferred method for posting notifications.

The `notificationInfo` dictionary is serialized as a property list, so it can be passed to another task. In the receiving task, it is deserialized back into a dictionary. This serialization imposes some restrictions on the objects that can be placed in the `notificationInfo` dictionary. See XML Property Lists for details.

## Parameters

- `name`: Name of the notification to post. Must not be  .
- `object`: Sender of the notification. May be  .
- `userInfo`: Dictionary containing additional information. May be  .
- `deliverImmediately`: Specifies when to deliver the notification. When  , the receiver delivers notifications to their observers according to the suspended-notification behavior specified in the corresponding dispatch table entry. When  , the receiver delivers the notification immediately to its observers.

## See Also

- [class func unarchiveObject(with: Data) -> Any?](nsunarchiver/unarchiveobject(with:).md)
  Decodes and returns the object archived in a given `NSData` object.
- [func encodeRootObject(Any)](nsarchiver/encoderootobject(_:).md)
  Archives a given object along with all the objects to which it is connected.
- [func post(name: NSNotification.Name, object: String?)](distributednotificationcenter/post(name:object:).md)
  Creates a notification, and posts it to the receiver.
- [func post(name: NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?)](distributednotificationcenter/post(name:object:userinfo:).md)
  Creates a notification with information, and posts it to the receiver.
- [func postNotificationName(NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?, options: DistributedNotificationCenter.Options)](distributednotificationcenter/postnotificationname(_:object:userinfo:options:).md)
  Creates a notification with information, and posts it to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/postnotificationname(_:object:userinfo:deliverimmediately:))*