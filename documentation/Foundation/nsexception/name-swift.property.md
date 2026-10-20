# name

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A string used to uniquely identify the receiver.

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
var name: NSExceptionName { get }
```

```objc
@property (copy, readonly) NSExceptionName name;
```

## See Also

### Related Documentation
- [init(name: NSExceptionName, reason: String?, userInfo: [AnyHashable : Any]?)](./init%28name,reason,userinfo%29.md)
  Initializes and returns a newly allocated exception object.
### Querying an NSException Object
- [var reason: String?](./reason-swift.property.md)
  A string containing a “human-readable” reason for the receiver.
- [var userInfo: [AnyHashable : Any]?](./userinfo-swift.property.md)
  A dictionary containing application-specific data pertaining to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/name-swift.property)*