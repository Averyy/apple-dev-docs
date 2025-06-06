# init(name:reason:userInfo:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

The created `NSException` object or `nil` if the object couldn’t be created.

#### Discussion

This is the designated initializer.

## Parameters

- `aName`: The name of the exception.
- `aReason`: A human-readable message string summarizing the reason for the exception.
- `aUserInfo`: A dictionary containing user-defined information relating to the exception

## See Also

- [class func raise(NSExceptionName, format: String, arguments: CVaListPointer)](nsexception/raise(_:format:arguments:).md)
  Creates and raises an exception with the specified name, reason, and arguments.
- [func raise()](nsexception/raise.md)
  Raises the receiver, causing program flow to jump to the local exception handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/init(name:reason:userinfo:))*