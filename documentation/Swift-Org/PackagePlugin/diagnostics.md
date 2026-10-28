---
url: "https://docs.swift.org/latest/documentation/packageplugin/diagnostics"
framework: "Swift-Org/PackagePlugin"
---

# Diagnostics

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

Emits errors, warnings, and remarks to show as a result of running the plugin.

## Declaration

```swift
struct Diagnostics
```

## Overview

After emitting one or more errors, a plugin should return a non-zero exit code.

## Topics

### Emitting Errors and Diagnostics
- [static func progress(String)](./diagnostics/progress%28_%29.md)
  Emits a progress message.
- [static func error(String, file: String?, line: Int?)](./diagnostics/error%28_,file,line%29.md)
  Emits an error with the message you specify.
- [static func warning(String, file: String?, line: Int?)](./diagnostics/warning%28_,file,line%29.md)
  Emits a warning with the message you specify.
- [static func remark(String, file: String?, line: Int?)](./diagnostics/remark%28_,file,line%29.md)
  Emits a remark with the message you specify.
- [static func emit(Severity, String, file: String?, line: Int?)](./diagnostics/emit%28_,_,file,line%29.md)
  Emits an error with a specified severity and message, and optional file path and line number.
- [Diagnostics.Severity](./diagnostics/severity.md)
  The severity of the diagnostic.

## See Also

### Plugin Diagnostics and Errors
- [enum PluginContextError](./plugincontexterror.md)
  Errors thrown while a plugin operates.
- [enum PluginDeserializationError](./plugindeserializationerror.md)
  Errors thrown while loading a plugin.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/diagnostics)*