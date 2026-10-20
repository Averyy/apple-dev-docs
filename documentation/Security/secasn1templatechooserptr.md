# SecAsn1TemplateChooserPtr

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

A pointer to the template chooser function.

**Availability**:
- macOS 10.0+ - Deprecated in 12.0

> **Deprecated**: SecAsn1 is not supported

## Declaration

```swift
typealias SecAsn1TemplateChooserPtr = (UnsafeMutableRawPointer, DarwinBoolean, UnsafePointer<CChar>, Int, UnsafeMutableRawPointer) -> UnsafePointer<SecAsn1Template>?
```

```c
typedef const struct SecAsn1Template_struct *(*)(void *, unsigned char, const char *, unsigned long, void *) SecAsn1TemplateChooserPtr;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secasn1templatechooserptr)*