# FinanceError

**Framework**: FinanceKit  
**Kind**: enum

Values that describe errors that may occur when accessing financial data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum FinanceError
```

## Topics

### Enumeration Cases
- [case dataRestricted(FinanceStore.DataType)](financeerror/datarestricted(_:).md)
  The data is in a restricted state.
- [FinanceError.historyTokenInvalid](financeerror/historytokeninvalid.md)
- [FinanceError.unknown](financeerror/unknown.md)
  An unknown error occurred.
### Instance Properties
- [var errorCode: Int](financeerror/errorcode.md)
  The error code within the given domain.
- [var errorDescription: String?](financeerror/errordescription.md)
  A localized message that describes what error occurred.
- [var errorUserInfo: [String : Any]](financeerror/erroruserinfo.md)
  The user-info dictionary that contains additional information about the error.
- [var failureReason: String?](financeerror/failurereason.md)
  A localized message that describes the reason for the failure.
### Type Properties
- [static var errorDomain: String](financeerror/errordomain.md)
  The domain of the error.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financeerror)*