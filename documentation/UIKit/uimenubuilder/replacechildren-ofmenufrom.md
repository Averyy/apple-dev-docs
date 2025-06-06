# replaceChildren(ofMenu:from:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Replaces the elements in a menu with the elements returned by the specified handler block.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func replaceChildren(ofMenu parentIdentifier: UIMenu.Identifier, from childrenBlock: ([UIMenuElement]) -> [UIMenuElement])
```

#### Discussion

Use this method to add, remove, and rearrange the children elements of a menu. For example, the following code listing uses this method to insert a Copy HTML menu element before Paste in the [`standardEdit`](uimenu/identifier-swift.struct/standardedit.md) menu.

```swift
builder.replaceChildren(ofMenu: .standardEdit) { (oldChildren) -> [UIMenuElement] in
    // Find the index of Paste menu element.
    var indexOfPaste = 0
    for (index, menuElement) in oldChildren.enumerated() {
        if let keyCommand = menuElement as? UIKeyCommand {
            if keyCommand.action == #selector(UIResponderStandardEditActions.paste(_:)) {
                indexOfPaste = index
                break
            }
        }
    }
    
    // Create a Copy HTML menu element.
    let copyHTML = UIKeyCommand(title: "Copy as HTML",
                                action: #selector(copyHTML(_:)),
                                input: "c",
                                modifierFlags: [.control, .command])
    
    // Insert Copy HTML before the Paste menu element
    // if found; otherwise, insert Copy HTML at the
    // beginning of the array.
    var newChildren = oldChildren
    newChildren.insert(copyHTML, at: indexOfPaste)
    return newChildren
}
```

## Parameters

- `parentIdentifier`: The identifier of the menu containing the children to replace.
- `childrenBlock`: A handler that returns the menu elements that replace the children in the menu associated with  . This handler has the following parameter:

## See Also

- [func replace(menu: UIMenu.Identifier, with: UIMenu)](uimenubuilder/replace(menu:with:).md)
  Replaces the specified menu with a new menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/replacechildren(ofmenu:from:))*