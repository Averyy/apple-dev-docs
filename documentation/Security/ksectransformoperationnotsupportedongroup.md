# kSecTransformOperationNotSupportedOnGroup

**Framework**: Security  
**Kind**: var

An illegal action on a group transform has occurred.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var kSecTransformOperationNotSupportedOnGroup: CFIndex { get }
```

#### Discussion

This might happen, for example, if you call [`SecTransformSetAttribute(_:_:_:_:)`](sectransformsetattribute(_:_:_:_:).md) on a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformoperationnotsupportedongroup)*