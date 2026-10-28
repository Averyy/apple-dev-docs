# UICellConfigurationState

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that encapsulates a cell’s state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface UICellConfigurationState : UIViewConfigurationState
```

## Overview

A cell configuration state encompasses a trait collection along with all of the common states that affect a cell’s appearance — view states like selected, focused, or disabled, and cell states like editing or swiped. A cell configuration state encapsulates the inputs that configure a cell for any possible state or combination of states. You use a cell configuration state with background and content configurations to obtain the default appearance for a specific state.

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [`updateConfiguration(using:)`](./uicollectionviewcell/updateconfiguration%28using%29.md) method in your cell subclass and use the state parameter. Outside of this method, you can get a cell’s configuration state by using its [`configurationState`](./uicollectionviewcell/configurationstate-4u37h.md) property.

You can create your own custom states to add to a cell configuration state by defining a custom state key using [`UIConfigurationStateCustomKey`](./uiconfigurationstatecustomkey.md).

## Topics

### Managing cell configuration states
- [editing](./uicellconfigurationstate-c.class/editing.md)
  A Boolean value that indicates whether the cell is in editing mode.
- [swiped](./uicellconfigurationstate-c.class/swiped.md)
  A Boolean value that indicates whether the cell is in a swiped state.
- [expanded](./uicellconfigurationstate-c.class/expanded.md)
  A Boolean value that indicates whether the cell is in an expanded state, such as in an outline.
- [reordering](./uicellconfigurationstate-c.class/reordering.md)
  A Boolean value that indicates whether the cell is reordering.
- [cellDragState](./uicellconfigurationstate-c.class/celldragstate.md)
  The cell’s drag state.
- [cellDropState](./uicellconfigurationstate-c.class/celldropstate.md)
  The cell’s drop state.
- [UICellConfigurationDragState](./uicellconfigurationdragstate.md)
  Constants that describe the cell’s drag state.
- [UICellConfigurationDropState](./uicellconfigurationdropstate.md)
  Constants that describe the cell’s drop state.

## Relationships

### Inherits From
- [UIViewConfigurationState](./uiviewconfigurationstate-c.class.md)

## See Also

### Configuration states
- [UIViewConfigurationState](./uiviewconfigurationstate-c.class.md)
  A structure that encapsulates a view’s state.
- [UIConfigurationState](./uiconfigurationstate-1smq1.md)
  The requirements for an object that encapsulates a view’s state.
- [struct UIConfigurationStateCustomKey](./uiconfigurationstatecustomkey.md)
  A key that defines a custom state for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellconfigurationstate-c.class)*