# NSException

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object that represents a special condition that interrupts the normal flow of program execution.

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
class NSException
```

```objc
@interface NSException : NSObject
```

#### Overview

Use [`NSException`](./nsexception.md) to implement exception handling. An exception is a special condition that interrupts the normal flow of program execution. Each application can interrupt the program for different reasons. For example, one application might interpret saving a file in a directory that is write-protected as an exception. In this sense, the exception is equivalent to an error. Another application might interpret the user’s key-press (for example, Control-C) as an exception: an indication that a long-running process should abort.

## Topics

### Creating and Raising an NSException Object
- [class func raise(NSExceptionName, format: String, arguments: CVaListPointer)](./nsexception/raise%28_,format,arguments%29.md)
  Creates and raises an exception with the specified name, reason, and arguments.
- [init(name: NSExceptionName, reason: String?, userInfo: [AnyHashable : Any]?)](./nsexception/init%28name,reason,userinfo%29.md)
  Initializes and returns a newly allocated exception object.
- [func raise()](./nsexception/raise%28%29.md)
  Raises the receiver, causing program flow to jump to the local exception handler.
### Querying an NSException Object
- [var name: NSExceptionName](./nsexception/name-swift.property.md)
  A string used to uniquely identify the receiver.
- [var reason: String?](./nsexception/reason-swift.property.md)
  A string containing a “human-readable” reason for the receiver.
- [var userInfo: [AnyHashable : Any]?](./nsexception/userinfo-swift.property.md)
  A dictionary containing application-specific data pertaining to the receiver.
### Getting Exception Stack Frames
- [var callStackReturnAddresses: [NSNumber]](./nsexception/callstackreturnaddresses.md)
  The call return addresses related to a raised exception.
- [var callStackSymbols: [String]](./nsexception/callstacksymbols.md)
  An array containing the current call stack symbols.
### Related Types
- [typealias NSUncaughtExceptionHandler](./nsuncaughtexceptionhandler.md)
  The type for uncaught exception handler functions.
- [struct NSExceptionName](./nsexceptionname.md)
### Functions
- [func NSGetUncaughtExceptionHandler() -> ((NSException) -> Void)?](./nsgetuncaughtexceptionhandler%28%29.md)
  Returns the top-level error handler.
- [func NSSetUncaughtExceptionHandler(((NSException) -> Void)?)](./nssetuncaughtexceptionhandler%28_%29.md)
  Changes the top-level error handler.
### Initializers
- [init?(coder: NSCoder)](./nsexception/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception)*