# SecAsn1TemplateChooser

**Framework**: Security  
**Kind**: typealias

Dynamically provides the sub-template to use during encode or decode.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias SecAsn1TemplateChooser = (UnsafeMutableRawPointer, DarwinBoolean, UnsafePointer<CChar>, Int, UnsafeMutableRawPointer) -> UnsafePointer<SecAsn1Template>?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secasn1templatechooser)*