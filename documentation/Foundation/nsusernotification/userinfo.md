# userInfo

**Framework**: Foundation  
**Kind**: property

Application-specific user info that can be attached to the notification.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var userInfo: [String : Any]? { get set }
```

#### Discussion

All items must be property list types or an exception is thrown.

The `userInfo` content must be of reasonable serialized size (less than 1KB) or an exception is thrown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/userinfo)*