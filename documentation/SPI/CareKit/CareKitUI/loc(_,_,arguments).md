---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/loc(_:_:arguments:)"
framework: "CareKit/CareKitUI"
---

# loc(_:_:arguments:)

**Framework**: CareKit/CareKitUI  
**Kind**: func  
**Role**: Function

A localization string wrapper to access framework specific strings

## Declaration

```swift
func loc(_ key: String, _ comment: String = "", arguments: [CVarArg] = []) -> String
```

## Parameters

- `key`: The `NSLocalizedString` key
- `comment`: The `NSLocalizedString` comment
- `arguments`: The `CVarArg` arguments to use in the formatted string This is a free function for developer convenience.

## See Also

### Localization
- [class OCKLocalization](./ocklocalization.md)
  A hook for the free function `loc` to access the framework bundle for localizations


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/loc(_:_:arguments:))*