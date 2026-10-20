# kSecTransformActionAttributeValidation

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

An action that triggers to perform validation of an attribute.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecTransformActionAttributeValidation: CFString
```

```c
extern CFStringRef const kSecTransformActionAttributeValidation;
```

#### Discussion

Allows a block to be called to validate the new value for an attribute. The default is no validation and any CFTypeRef can be used as the new value. The block should return NULL if the value is ok to set on the attribute or a CFErrorRef otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformactionattributevalidation)*