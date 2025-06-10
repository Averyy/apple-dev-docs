# CPTabBarTemplateDelegate

**Framework**: CarPlay  
**Kind**: protocol

The methods an object implements to act as the delegate for a tab bar template.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
protocol CPTabBarTemplateDelegate : NSObjectProtocol
```

#### Overview

You use the `CPTabBarTemplateDelegate` protocol to respond to a tab bar template’s events. The protocol defines methods that the template calls in response to these events, and your implementation provides the appropriate behavior when the events occur. For example, reloading a tab’s contents when the user selects it to make sure it’s displaying the latest data.

## Topics

### Managing the Selected Template
- [func tabBarTemplate(CPTabBarTemplate, didSelect: CPTemplate)](cptabbartemplatedelegate/tabbartemplate(_:didselect:).md)
  Tells the delegate when the tab bar selects the specified template.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any CPTabBarTemplateDelegate)?](cptabbartemplate/delegate.md)
  The object that acts as the template’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptabbartemplatedelegate)*