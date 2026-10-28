# kSecTransformOperationNotSupportedOnGroup

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

An illegal action on a group transform has occurred.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var kSecTransformOperationNotSupportedOnGroup: CFIndex { get }
```

```c
kSecTransformOperationNotSupportedOnGroup
```

## Discussion

This might happen, for example, if you call [`SecTransformSetAttribute(_:_:_:_:)`](./sectransformsetattribute%28_,_,_,_%29.md) on a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformoperationnotsupportedongroup)*