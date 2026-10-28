# init(name:reason:userInfo:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes and returns a newly allocated exception object.

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
init(name aName: NSExceptionName, reason aReason: String?, userInfo aUserInfo: [AnyHashable : Any]? = nil)
```

```objc
- (instancetype) initWithName:(NSExceptionName) aName reason:(NSString *) aReason userInfo:(NSDictionary *) aUserInfo;
```

## Return Value

The created `NSException` object or `nil` if the object couldn’t be created.

## Discussion

This is the designated initializer.

## Parameters

- `aName`: The name of the exception.
- `aReason`: A human-readable message string summarizing the reason for the exception.
- `aUserInfo`: A dictionary containing user-defined information relating to the exception

## See Also

### Creating and Raising an NSException Object
- [class func raise(NSExceptionName, format: String, arguments: CVaListPointer)](./raise%28_,format,arguments%29.md)
  Creates and raises an exception with the specified name, reason, and arguments.
- [func raise()](./raise%28%29.md)
  Raises the receiver, causing program flow to jump to the local exception handler.
- [+ raise:format:](./raise_format_.md)
  A convenience method that creates and raises an exception.
### Related Documentation
- [+ exceptionWithName:reason:userInfo:](./exceptionwithname_reason_userinfo_.md)
  Creates and returns an exception object .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/init(name:reason:userinfo:))*