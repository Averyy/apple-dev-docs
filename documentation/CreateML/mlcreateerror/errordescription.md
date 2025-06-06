# errorDescription

**Framework**: Create ML  
**Kind**: property

A localized, human-readable description of the error and why it occurred, if applicable.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var errorDescription: String? { get }
```

## See Also

- [static var errorDomain: String](mlcreateerror/errordomain-8raky.md)
  Default domain of the error.
- [var localizedDescription: String](mlcreateerror/localizeddescription.md)
  Retrieve the localized description for this error.
- [var errorCode: Int](mlcreateerror/errorcode.md)
  The numeric code of this error.
- [var errorUserInfo: [String : Any]](mlcreateerror/erroruserinfo.md)
  A dictionary that provides additional information about the error.
- [var failureReason: String?](mlcreateerror/failurereason.md)
  A localized, human-readable reason behind the failure, if applicable.
- [var helpAnchor: String?](mlcreateerror/helpanchor.md)
  A localized message providing “help” text if the user requests help.
- [var recoverySuggestion: String?](mlcreateerror/recoverysuggestion.md)
  A localized message describing how one might recover from the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlcreateerror/errordescription)*