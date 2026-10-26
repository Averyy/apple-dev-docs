---
url: "https://docs.swift.org/latest/documentation/packageplugin/diagnostics/severity"
framework: "Swift-Org/PackagePlugin"
---

# Diagnostics.Severity

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

The severity of the diagnostic.

## Declaration

```swift
enum Severity
```

## Topics

### Enumeration Cases
- [Diagnostics.Severity.error](./severity/error.md)
- [Diagnostics.Severity.remark](./severity/remark.md)
- [Diagnostics.Severity.warning](./severity/warning.md)
### Initializers
- [init?(rawValue: String)](./severity/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./severity/equatable-implementations.md)
- [RawRepresentable Implementations](./severity/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable

## See Also

### Emitting Errors and Diagnostics
- [static func progress(String)](./progress%28_%29.md)
  Emits a progress message.
- [static func error(String, file: String?, line: Int?)](./error%28_,file,line%29.md)
  Emits an error with the message you specify.
- [static func warning(String, file: String?, line: Int?)](./warning%28_,file,line%29.md)
  Emits a warning with the message you specify.
- [static func remark(String, file: String?, line: Int?)](./remark%28_,file,line%29.md)
  Emits a remark with the message you specify.
- [static func emit(Severity, String, file: String?, line: Int?)](./emit%28_,_,file,line%29.md)
  Emits an error with a specified severity and message, and optional file path and line number.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/diagnostics/severity)*