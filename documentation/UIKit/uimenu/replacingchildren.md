# replacingChildren(_:)

**Framework**: UIKit  
**Kind**: method

Creates a new menu with the same configuration as the current menu, but with a new set of child elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func replacingChildren(_ newChildren: [UIMenuElement]) -> UIMenu
```

#### Return Value

A new menu object containing the specified children.

#### Discussion

The new menu contains the same title, image, identifier, and options as the current menu. The new menu contains only the children in the `newChildren` parameter. It doesn’t contain any child elements from the current menu.

## Parameters

- `newChildren`: The child elements to include in the new menu.

## See Also

- [var children: [UIMenuElement]](uimenu/children.md)
  The contents of the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/replacingchildren(_:))*