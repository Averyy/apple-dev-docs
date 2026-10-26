# reason

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A string containing a “human-readable” reason for the receiver.

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
var reason: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * reason;
```

## See Also

### Related Documentation
- [init(name: NSExceptionName, reason: String?, userInfo: [AnyHashable : Any]?)](./init%28name,reason,userinfo%29.md)
  Initializes and returns a newly allocated exception object.
- [+ exceptionWithName:reason:userInfo:](./exceptionwithname_reason_userinfo_.md)
  Creates and returns an exception object .
### Querying an NSException Object
- [var name: NSExceptionName](./name-swift.property.md)
  A string used to uniquely identify the receiver.
- [var userInfo: [AnyHashable : Any]?](./userinfo-swift.property.md)
  A dictionary containing application-specific data pertaining to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/reason-swift.property)*