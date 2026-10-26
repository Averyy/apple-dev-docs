# exceptionWithName:reason:userInfo:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an exception object .

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
+ (NSException *) exceptionWithName:(NSExceptionName) name reason:(NSString *) reason userInfo:(NSDictionary *) userInfo;
```

#### Return Value

The created `NSException` object or `nil` if the object couldn’t be created.

## Parameters

- `name`: The name of the exception.
- `reason`: A human-readable message string summarizing the reason for the exception.
- `userInfo`: A dictionary containing user-defined information relating to the exception

## See Also

### Related Documentation
- [var userInfo: [AnyHashable : Any]?](./userinfo-swift.property.md)
  A dictionary containing application-specific data pertaining to the receiver.
- [var reason: String?](./reason-swift.property.md)
  A string containing a “human-readable” reason for the receiver.
- [Exception Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Exceptions/Exceptions.html#//apple_ref/doc/uid/10000012i)
- [var name: NSExceptionName](./name-swift.property.md)
  A string used to uniquely identify the receiver.
### Creating and Raising an NSException Object
- [+ raise:format:](./raise_format_.md)
  A convenience method that creates and raises an exception.
- [class func raise(NSExceptionName, format: String, arguments: CVaListPointer)](./raise%28_,format,arguments%29.md)
  Creates and raises an exception with the specified name, reason, and arguments.
- [init(name: NSExceptionName, reason: String?, userInfo: [AnyHashable : Any]?)](./init%28name,reason,userinfo%29.md)
  Initializes and returns a newly allocated exception object.
- [func raise()](./raise%28%29.md)
  Raises the receiver, causing program flow to jump to the local exception handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/exceptionwithname:reason:userinfo:)*