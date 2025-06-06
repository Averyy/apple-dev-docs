# kSecTransformActionExternalizeExtraData

**Framework**: Security  
**Kind**: var

An action that triggers after data is stored.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecTransformActionExternalizeExtraData: CFString
```

#### Discussion

Allows for adding to the data that is stored using an override to the kSecTransformActionExternalizeExtraData block. The output of this override is a dictionary that contains the custom externalized data. A common use of this override is to write out a version number of a custom transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformactionexternalizeextradata)*