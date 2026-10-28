# kSecTransformActionInternalizeExtraData

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

An action that triggers after attributes are read into a transform.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecTransformActionInternalizeExtraData: CFString
```

```c
extern CFStringRef const kSecTransformActionInternalizeExtraData;
```

## Discussion

Overrides the standard processing that occurs when externalized data is used to create a transform. This is closely tied to the kSecTransformActionExternalizeExtraData override. The ‘normal’ attributes are read into the new transform and then this is called to read in the items that were written out using kSecTransformActionExternalizeExtraData override. A common use of this override would be to read in the version number of the externalized custom transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformactioninternalizeextradata)*