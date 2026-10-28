# SecItemAttr.volumeItemAttr

**Framework**: Security  
**Kind**: case  
**Role**: Case

Identifies the volume attribute.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case volumeItemAttr
```

```c
kSecVolumeItemAttr
```

## Discussion

You use this tag to set or get a string value that represents the AppleShare volume. This is unique to AppleShare password attributes. Keychain strings should use UTF-8 encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemattr/volumeitemattr)*