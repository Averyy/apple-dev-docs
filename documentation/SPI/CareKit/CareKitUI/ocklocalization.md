---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocklocalization"
framework: "CareKit/CareKitUI"
---

# OCKLocalization

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A hook for the free function `loc` to access the framework bundle for localizations

## Declaration

```swift
class OCKLocalization
```

## Topics

### Type Methods
- [static func localized(String, tableName: String?, bundle: Bundle?, value: String, comment: String) -> String](./ocklocalization/localized%28_,tablename,bundle,value,comment%29.md)
  An `NSLocalizedString` wrapper that searches for overrides in a main bundle before falling back to the framework provided strings

## See Also

### Localization
- [func loc(String, String, arguments: [CVarArg]) -> String](./loc%28_,_,arguments%29.md)
  A localization string wrapper to access framework specific strings


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocklocalization)*