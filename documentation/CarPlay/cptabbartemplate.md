# CPTabBarTemplate

**Framework**: CarPlay  
**Kind**: class

A container template that displays and manages other templates, presenting them as tabs.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPTabBarTemplate
```

#### Overview

`CPTabBarTemplate` is a container template that displays a collection of other templates, where each template occupies a single tab in the tab bar. At runtime, use [`maximumTabCount`](cptabbartemplate/maximumtabcount.md) to determine the maximum number of tabs that your tab bar can display.

When creating an instance of `CPTabBarTemplate`, provide an array of templates for the tab bar to display. CarPlay treats the array’s templates as root templates, each with its own navigation hierarchy. When a tab bar template is the [`rootTemplate`](cpinterfacecontroller/roottemplate.md) of your app’s interface controller and you use the controller to add and remove templates, CarPlay applies those changes to the selected tab’s navigation hierarchy.

> **Note**:  You can’t add a tab bar template to an existing navigation hierarchy, or present one modally. Instead, use [`setRootTemplate(_:animated:completion:)`](cpinterfacecontroller/setroottemplate(_:animated:completion:).md) to set the tab bar as your app’s root template.

 You can’t add a tab bar template to an existing navigation hierarchy, or present one modally. Instead, use [`setRootTemplate(_:animated:completion:)`](cpinterfacecontroller/setroottemplate(_:animated:completion:).md) to set the tab bar as your app’s root template.

Use a transactional approach when making changes to the tab bar. Retrieve the current set of templates using the [`templates`](cptabbartemplate/templates.md) property. Add, remove, reorder, or make appearance changes to one or more of the array’s templates. For example, use the [`tabTitle`](cptemplate/tabtitle.md) property to update a template’s tab title, or set [`showsTabBadge`](cptemplate/showstabbadge.md) to `true` to add an indicator to a template’s tab. Then call the [`updateTemplates(_:)`](cptabbartemplate/updatetemplates(_:).md) method and pass it the updated array. CarPlay commits those changes and updates the tab bar.

When the user selects a tab, the template calls the [`tabBarTemplate(_:didSelect:)`](cptabbartemplatedelegate/tabbartemplate(_:didselect:).md) method on its delegate, which is an object you provide that conforms to the [`CPTabBarTemplateDelegate`](cptabbartemplatedelegate.md) protocol.

## Topics

### Creating a Tab Bar Template
- [init(templates: [CPTemplate])](cptabbartemplate/init(templates:).md)
  Creates a tab bar template that displays the provided root templates as tabs.
### Managing Tab Bar Interactions
- [var delegate: (any CPTabBarTemplateDelegate)?](cptabbartemplate/delegate.md)
  The object that acts as the template’s delegate.
- [protocol CPTabBarTemplateDelegate](cptabbartemplatedelegate.md)
  The methods an object implements to act as the delegate for a tab bar template.
### Managing the Templates
- [var templates: [CPTemplate]](cptabbartemplate/templates.md)
  The tab bar’s templates.
- [func updateTemplates([CPTemplate])](cptabbartemplate/updatetemplates(_:).md)
  Adds, removes, reorders, or updates the tab bar’s templates.
- [class var maximumTabCount: Int](cptabbartemplate/maximumtabcount.md)
  The maximum number of tabs that the template can display.
### Getting the Selected Template
- [var selectedTemplate: CPTemplate?](cptabbartemplate/selectedtemplate.md)
  The currently selected template in the tab bar.
### Instance Methods
- [func select(CPTemplate)](cptabbartemplate/select(_:).md)
- [func selectTemplate(at: Int)](cptabbartemplate/selecttemplate(at:).md)

## Relationships

### Inherits From
- [CPTemplate](cptemplate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CPListTemplate](cplisttemplate.md)
  A template that displays and manages a list of items.
- [class CPGridTemplate](cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPTemplate](cptemplate.md)
  An abstract base class for interface templates.
- [protocol CPBarButtonProviding](cpbarbuttonproviding.md)
  The methods that templates use to provide buttons for the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptabbartemplate)*