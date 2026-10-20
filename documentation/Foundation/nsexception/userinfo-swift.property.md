# userInfo

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A dictionary containing application-specific data pertaining to the receiver.

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
var userInfo: [AnyHashable : Any]? { get }
```

```objc
@property (copy, readonly, nullable) NSDictionary * userInfo;
```

#### Discussion

`nil` if no application-specific data exists. As an example, if a method’s return value caused the exception to be raised, the return value might be available to the exception handler through this method.

## See Also

### Related Documentation
- [init(name: NSExceptionName, reason: String?, userInfo: [AnyHashable : Any]?)](./init%28name,reason,userinfo%29.md)
  Initializes and returns a newly allocated exception object.
### Querying an NSException Object
- [var name: NSExceptionName](./name-swift.property.md)
  A string used to uniquely identify the receiver.
- [var reason: String?](./reason-swift.property.md)
  A string containing a “human-readable” reason for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/userinfo-swift.property)*