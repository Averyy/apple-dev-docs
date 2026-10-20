# identifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The identifier for the user notification action.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
var identifier: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * identifier;
```

## See Also

### Getting the Identifier and Title
- [var title: String?](./title.md)
  The localized title shown to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationaction/identifier)*