# templates

**Framework**: CarPlay  
**Kind**: property

The tab bar’s templates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
var templates: [CPTemplate] { get }
```

#### Discussion

The array contains the root template from each of the tab bar’s tabs. To add new templates to the tab bar, to remove or reorder existing templates, or to update a template’s tab bar appearance, use the [`updateTemplates(_:)`](cptabbartemplate/updatetemplates(_:).md) method.

## See Also

- [func updateTemplates([CPTemplate])](cptabbartemplate/updatetemplates(_:).md)
  Adds, removes, reorders, or updates the tab bar’s templates.
- [class var maximumTabCount: Int](cptabbartemplate/maximumtabcount.md)
  The maximum number of tabs that the template can display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptabbartemplate/templates)*