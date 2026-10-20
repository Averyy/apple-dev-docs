# ENErrorHandler

**Framework**: Exposure Notification  
**Kind**: typealias  
**Role**: Type Alias

The handler for error conditions.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
typealias ENErrorHandler = ((any Error)?) -> Void
```

```c
typedef void (^)(NSError *) ENErrorHandler;
```

#### Discussion

> ❗ **Important**:  This type is available in iOS 12.5, and in iOS 13.5 and later.

## See Also

### Errors
- [struct ENError](./enerror.md)
  Errors that the exposure notification framework issues.
- [ENError.Code](./enerror/code.md)
  Error codes that the exposure notification framework issues.
- [let ENErrorDomain: String](./enerrordomain.md)
  The domain for an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enerrorhandler)*