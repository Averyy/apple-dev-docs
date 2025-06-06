# init(title:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns a menu having the specified title and with autoenabling of menu items turned on.

**Availability**:
- macOS ?+

## Declaration

```swift
init(title: String)
```

#### Return Value

The initialized `NSMenu` object or `nil` if the object could not be initialized.

#### Discussion

This method is the designated initializer for the class.

## Parameters

- `title`: The title to assign to the menu.

## See Also

- [var autoenablesItems: Bool](nsmenu/autoenablesitems.md)
  Indicates whether the menu automatically enables and disables its menu items.
- [init(coder: NSCoder)](nsmenu/init(coder:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/init(title:))*