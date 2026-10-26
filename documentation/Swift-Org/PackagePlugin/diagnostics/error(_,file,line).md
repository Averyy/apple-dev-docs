---
url: "https://docs.swift.org/latest/documentation/packageplugin/diagnostics/error(_:file:line:)"
framework: "Swift-Org/PackagePlugin"
---

# error(_:file:line:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Type Method

Emits an error with the message you specify.

## Declaration

```swift
static func error(_ message: String, file: String? = #file, line: Int? = #line)
```

## Parameters

- `message`: The description of the error.
- `file`: The file responsible for the diagnostic, that defaults to `#file`.
- `line`: The line responsible for the diagnostic, that defaults to `#line`.

## See Also

### Emitting Errors and Diagnostics
- [static func progress(String)](./progress%28_%29.md)
  Emits a progress message.
- [static func warning(String, file: String?, line: Int?)](./warning%28_,file,line%29.md)
  Emits a warning with the message you specify.
- [static func remark(String, file: String?, line: Int?)](./remark%28_,file,line%29.md)
  Emits a remark with the message you specify.
- [static func emit(Severity, String, file: String?, line: Int?)](./emit%28_,_,file,line%29.md)
  Emits an error with a specified severity and message, and optional file path and line number.
- [Diagnostics.Severity](./severity.md)
  The severity of the diagnostic.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/diagnostics/error(_:file:line:))*