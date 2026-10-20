# SecAsn1TemplateChooser

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

Dynamically provides the sub-template to use during encode or decode.

**Availability**:
- macOS 10.0+ - Deprecated in 12.0

> **Deprecated**: SecAsn1 is not supported

## Declaration

```swift
typealias SecAsn1TemplateChooser = (UnsafeMutableRawPointer, DarwinBoolean, UnsafePointer<CChar>, Int, UnsafeMutableRawPointer) -> UnsafePointer<SecAsn1Template>?
```

```c
typedef const struct SecAsn1Template_struct *(void *, unsigned char, const char *, unsigned long, void *) SecAsn1TemplateChooser;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secasn1templatechooser)*