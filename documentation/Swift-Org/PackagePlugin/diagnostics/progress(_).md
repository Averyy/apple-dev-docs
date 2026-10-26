---
url: "https://docs.swift.org/latest/documentation/packageplugin/diagnostics/progress(_:)"
framework: "Swift-Org/PackagePlugin"
---

# progress(_:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Type Method

Emits a progress message.

## Declaration

```swift
static func progress(_ message: String)
```

## Parameters

- `message`: The description of the progress.

## See Also

### Emitting Errors and Diagnostics
- [static func error(String, file: String?, line: Int?)](./error%28_,file,line%29.md)
  Emits an error with the message you specify.
- [static func warning(String, file: String?, line: Int?)](./warning%28_,file,line%29.md)
  Emits a warning with the message you specify.
- [static func remark(String, file: String?, line: Int?)](./remark%28_,file,line%29.md)
  Emits a remark with the message you specify.
- [static func emit(Severity, String, file: String?, line: Int?)](./emit%28_,_,file,line%29.md)
  Emits an error with a specified severity and message, and optional file path and line number.
- [Diagnostics.Severity](./severity.md)
  The severity of the diagnostic.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/diagnostics/progress(_:))*