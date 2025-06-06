# tabBarTemplate(_:didSelect:)

**Framework**: CarPlay  
**Kind**: method  
**Required**: Yes

Tells the delegate when the tab bar selects the specified template.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func tabBarTemplate(_ tabBarTemplate: CPTabBarTemplate, didSelect selectedTemplate: CPTemplate)
```

#### Discussion

The tab bar template calls this method each time the user selects a tab. `tabBarTemplate` is the same template that the tab bar’s [`selectedTemplate`](cptabbartemplate/selectedtemplate.md) property returns.

## Parameters

- `tabBarTemplate`: The tab bar template that alerts you to the change in selection.
- `selectedTemplate`: The template that the user selects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptabbartemplatedelegate/tabbartemplate(_:didselect:))*