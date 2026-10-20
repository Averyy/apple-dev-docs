# failureReason

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

A localized, human-readable reason behind the failure, if applicable.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var failureReason: String? { get }
```

## See Also

### Describing errors in a user interface
- [var errorCode: Int](./errorcode.md)
  The numeric code of this error.
- [var errorUserInfo: [String : Any]](./erroruserinfo.md)
  A dictionary that provides additional information about the error.
- [var errorDescription: String?](./errordescription.md)
  A localized, human-readable description of the error and why it occurred, if applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlcreateerror/failurereason)*