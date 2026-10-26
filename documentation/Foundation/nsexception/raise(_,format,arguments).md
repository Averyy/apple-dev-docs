# raise(_:format:arguments:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and raises an exception with the specified name, reason, and arguments.

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
class func raise(_ name: NSExceptionName, format: String, arguments argList: CVaListPointer)
```

```objc
+ (void) raise:(NSExceptionName) name format:(NSString *) format arguments:(va_list) argList;
```

#### Discussion

The user-defined dictionary of the generated object is `nil`.

## Parameters

- `name`: The name of the exception.
- `format`: A human-readable message string (that is, the exception reason) with conversion specifications for the variable arguments in `argList`.
- `argList`: Variable information to be inserted into the formatted exception reason (in the manner of `vprintf`).

## See Also

### Creating and Raising an NSException Object
- [init(name: NSExceptionName, reason: String?, userInfo: [AnyHashable : Any]?)](./init%28name,reason,userinfo%29.md)
  Initializes and returns a newly allocated exception object.
- [func raise()](./raise%28%29.md)
  Raises the receiver, causing program flow to jump to the local exception handler.
- [+ exceptionWithName:reason:userInfo:](./exceptionwithname_reason_userinfo_.md)
  Creates and returns an exception object .
### Related Documentation
- [+ raise:format:](./raise_format_.md)
  A convenience method that creates and raises an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/raise(_:format:arguments:))*