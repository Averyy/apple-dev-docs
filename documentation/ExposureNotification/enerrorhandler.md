# ENErrorHandler

**Framework**: Exposure Notification  
**Kind**: typealias

The handler for error conditions.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
typealias ENErrorHandler = ((any Error)?) -> Void
```

#### Discussion

> ❗ **Important**:  This type is available in iOS 12.5, and in iOS 13.5 and later.

 This type is available in iOS 12.5, and in iOS 13.5 and later.

## See Also

- [struct ENError](enerror.md)
  Errors that the exposure notification framework issues.
- [ENError.Code](enerror/code.md)
  Error codes that the exposure notification framework issues.
- [let ENErrorDomain: String](enerrordomain.md)
  The domain for an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enerrorhandler)*