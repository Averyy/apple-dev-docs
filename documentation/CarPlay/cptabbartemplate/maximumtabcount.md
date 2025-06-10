# maximumTabCount

**Framework**: CarPlay  
**Kind**: property

The maximum number of tabs that the template can display.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class var maximumTabCount: Int { get }
```

#### Discussion

This property’s value depends on the app’s entitlements. At runtime, use this value to determine the maximum number of tabs that your tab bar can display.

## See Also

- [var templates: [CPTemplate]](cptabbartemplate/templates.md)
  The tab bar’s templates.
- [func updateTemplates([CPTemplate])](cptabbartemplate/updatetemplates(_:).md)
  Adds, removes, reorders, or updates the tab bar’s templates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptabbartemplate/maximumtabcount)*