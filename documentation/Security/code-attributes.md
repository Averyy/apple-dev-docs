# Code Attributes

**Framework**: Security

Specify these keys from the attribute dictionary when you create a static code instance.

#### Overview

Use these keys in the attribute dictionary when calling the [`SecStaticCodeCreateWithPathAndAttributes(_:_:_:_:)`](secstaticcodecreatewithpathandattributes(_:_:_:_:).md) function.

## Topics

### Constants
- [let kSecCodeAttributeArchitecture: CFString](kseccodeattributearchitecture.md)
  A key whose value is a string that indicates an architecture, such as `i386` or `x86_64`.
- [let kSecCodeAttributeSubarchitecture: CFString](kseccodeattributesubarchitecture.md)
  A key whose value is a string indicating a specific processor type, such as `i686` or `core2`.
- [let kSecCodeAttributeBundleVersion: CFString](kseccodeattributebundleversion.md)
  A key whose value indicates the bundle version.
- [let kSecCodeAttributeUniversalFileOffset: CFString](kseccodeattributeuniversalfileoffset.md)
  A key whose value indicates the offset of a Mach-O specific slice of a universal Mach-O file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/code-attributes)*