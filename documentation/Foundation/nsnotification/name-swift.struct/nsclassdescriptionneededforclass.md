# NSClassDescriptionNeededForClass

**Framework**: Foundation  
**Kind**: property

Posted by [`init(for:)`](nsclassdescription/init(for:).md) when a class description cannot be found for a class.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static let NSClassDescriptionNeededForClass: NSNotification.Name
```

#### Discussion

After the notification is processed, [`init(for:)`](nsclassdescription/init(for:).md) checks for a class description again. This checking allows an observer to register class descriptions lazily. The notification is posted only once for any given class, even if the class description remains undefined.

The notification object is the class object for which the class description is requested. This notification does not contain a `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsclassdescriptionneededforclass)*