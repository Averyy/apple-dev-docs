# object

**Framework**: Foundation  
**Kind**: property

The object associated with the notification.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var object: Any? { get }
```

#### Discussion

This is often the object that posted this notification. In Objective-C, it may be `nil`.

Typically you use this method to find out what object a notification applies to when you receive a notification.

For example, suppose you’ve registered an object to receive the message `handlePortDeath:` when the `PortInvalid` notification is posted to the notification center and that `handlePortDeath:` needs to access the object monitoring the port that is now invalid. `handlePortDeath:` can retrieve that object as shown here:

Example of accessing notification object in Objective-C:

```objc
- (void)handlePortDeath:(NSNotification *)notification
{
    ...
    [self reclaimResourcesForPort:notification.object];
    ...
}
```

## See Also

- [var name: NSNotification.Name](nsnotification/name-swift.property.md)
  The name of the notification.
- [var userInfo: [AnyHashable : Any]?](nsnotification/userinfo.md)
  The user information dictionary associated with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/object)*