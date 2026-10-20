# kSecTransformActionProcessData

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

An action that triggers to process the data of an attribute.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecTransformActionProcessData: CFString
```

```c
extern CFStringRef const kSecTransformActionProcessData;
```

#### Discussion

Overrides the standard data processing for an attribute. This is almost exclusively used for processing the input attribute as the return value of their block sets the output attribute. This is used with the SecTransformOverrideAttributeAction block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformactionprocessdata)*