# raise(_:format:arguments:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

The user-defined dictionary of the generated object is `nil`.

## Parameters

- `name`: The name of the exception.
- `format`: A human-readable message string (that is, the exception reason) with conversion specifications for the variable arguments in  .
- `argList`: Variable information to be inserted into the formatted exception reason (in the manner of  ).

## See Also

- [init(name: NSExceptionName, reason: String?, userInfo: [AnyHashable : Any]?)](nsexception/init(name:reason:userinfo:).md)
  Initializes and returns a newly allocated exception object.
- [func raise()](nsexception/raise.md)
  Raises the receiver, causing program flow to jump to the local exception handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/raise(_:format:arguments:))*