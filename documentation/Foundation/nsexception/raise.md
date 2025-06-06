# raise()

**Framework**: Foundation  
**Kind**: method

Raises the receiver, causing program flow to jump to the local exception handler.

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
func raise()
```

#### Discussion

When there are no exception handlers in the exception handler stack, unless the exception is raised during the posting of a notification, this method calls the uncaught exception handler, in which last-minute logging can be performed. The program then terminates, regardless of the actions taken by the uncaught exception handler.

## See Also

- [class func raise(NSExceptionName, format: String, arguments: CVaListPointer)](nsexception/raise(_:format:arguments:).md)
  Creates and raises an exception with the specified name, reason, and arguments.
- [init(name: NSExceptionName, reason: String?, userInfo: [AnyHashable : Any]?)](nsexception/init(name:reason:userinfo:).md)
  Initializes and returns a newly allocated exception object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/raise())*