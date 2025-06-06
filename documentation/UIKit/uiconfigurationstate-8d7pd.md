# UIConfigurationState

**Framework**: UIKit  
**Kind**: protocol

The requirements for an object that encapsulates a view’s state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
protocol UIConfigurationState
```

#### Overview

This protocol provides a blueprint for a configuration state object, which encompasses a trait collection along with all of the common states that affect a view’s appearance. A configuration state encapsulates the inputs that configure a view for any possible state or combination of states. You use a configuration state with background and content configurations to obtain the default appearance for a specific state.

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [`updateConfiguration(using:)`](uicollectionviewcell/updateconfiguration(using:).md) method in your view subclass and use the state parameter. Outside of this method, you can get a view’s configuration state by using its [`configurationState`](uicollectionviewcell/configurationstate-4u37h.md) property.

For more information, see [`UIViewConfigurationState`](uiviewconfigurationstate-swift.struct.md) and [`UICellConfigurationState`](uicellconfigurationstate-swift.struct.md).

## Topics

### Managing configuration states
- [var traitCollection: UITraitCollection](uiconfigurationstate-8d7pd/traitcollection.md)
  The traits that describe the current layout environment of the view, such as the user interface style and layout direction.
- [subscript(UIConfigurationStateCustomKey) -> AnyHashable?](uiconfigurationstate-8d7pd/subscript(_:).md)
  Accesses custom states by key.
### Creating a configuration state manually
- [init(traitCollection: UITraitCollection)](uiconfigurationstate-8d7pd/init(traitcollection:).md)
  Creates a view configuration state with the specified trait collection.

## Relationships

### Conforming Types
- [UICellConfigurationState](uicellconfigurationstate-swift.struct.md)
- [UIContentUnavailableConfigurationState](uicontentunavailableconfigurationstate-swift.struct.md)
- [UIViewConfigurationState](uiviewconfigurationstate-swift.struct.md)

## See Also

- [struct UIViewConfigurationState](uiviewconfigurationstate-swift.struct.md)
  A structure that encapsulates a view’s state.
- [struct UICellConfigurationState](uicellconfigurationstate-swift.struct.md)
  A structure that encapsulates a cell’s state.
- [struct UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md)
  A key that defines a custom state for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationstate-8d7pd)*