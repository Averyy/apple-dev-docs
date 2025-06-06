# userInfo

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

`nil` if no application-specific data exists. As an example, if a method’s return value caused the exception to be raised, the return value might be available to the exception handler through this method.

## See Also

- [init(name: NSExceptionName, reason: String?, userInfo: [AnyHashable : Any]?)](nsexception/init(name:reason:userinfo:).md)
  Initializes and returns a newly allocated exception object.
- [var name: NSExceptionName](nsexception/name-swift.property.md)
  A string used to uniquely identify the receiver.
- [var reason: String?](nsexception/reason-swift.property.md)
  A string containing a “human-readable” reason for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/userinfo-swift.property)*