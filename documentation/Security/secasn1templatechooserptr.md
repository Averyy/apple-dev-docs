# SecAsn1TemplateChooserPtr

**Framework**: Security  
**Kind**: typealias

A pointer to the template chooser function.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias SecAsn1TemplateChooserPtr = (UnsafeMutableRawPointer, DarwinBoolean, UnsafePointer<CChar>, Int, UnsafeMutableRawPointer) -> UnsafePointer<SecAsn1Template>?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secasn1templatechooserptr)*