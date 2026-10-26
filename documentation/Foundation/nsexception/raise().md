# raise()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) raise;
```

#### Discussion

When there are no exception handlers in the exception handler stack, unless the exception is raised during the posting of a notification, this method calls the uncaught exception handler, in which last-minute logging can be performed. The program then terminates, regardless of the actions taken by the uncaught exception handler.

## See Also

### Creating and Raising an NSException Object
- [class func raise(NSExceptionName, format: String, arguments: CVaListPointer)](./raise%28_,format,arguments%29.md)
  Creates and raises an exception with the specified name, reason, and arguments.
- [init(name: NSExceptionName, reason: String?, userInfo: [AnyHashable : Any]?)](./init%28name,reason,userinfo%29.md)
  Initializes and returns a newly allocated exception object.
- [+ exceptionWithName:reason:userInfo:](./exceptionwithname_reason_userinfo_.md)
  Creates and returns an exception object .
### Related Documentation
- [+ raise:format:](./raise_format_.md)
  A convenience method that creates and raises an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/raise())*