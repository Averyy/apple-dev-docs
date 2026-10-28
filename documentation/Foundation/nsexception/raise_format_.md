# raise:format:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

A convenience method that creates and raises an exception.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (void) raise:(NSExceptionName) name format:(NSString *) format;
```

## Discussion

The user-defined information is `nil` for the generated exception object.

Pass variable information to be inserted into the formatted exception reason (in the manner of `printf`) as variadic arguments.

## Parameters

- `name`: The name of the exception.
- `format`: A human-readable message string (that is, the exception reason) with conversion specifications for the variable arguments that follow.

## See Also

### Creating and Raising an NSException Object
- [+ exceptionWithName:reason:userInfo:](./exceptionwithname_reason_userinfo_.md)
  Creates and returns an exception object .
- [class func raise(NSExceptionName, format: String, arguments: CVaListPointer)](./raise%28_,format,arguments%29.md)
  Creates and raises an exception with the specified name, reason, and arguments.
- [init(name: NSExceptionName, reason: String?, userInfo: [AnyHashable : Any]?)](./init%28name,reason,userinfo%29.md)
  Initializes and returns a newly allocated exception object.
- [func raise()](./raise%28%29.md)
  Raises the receiver, causing program flow to jump to the local exception handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/raise:format:)*