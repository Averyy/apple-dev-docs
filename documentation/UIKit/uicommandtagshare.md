# UICommandTagShare

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A value that identifies a command as a Share menu.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
let UICommandTagShare: String
```

```c
extern NSString * const UICommandTagShare;
```

#### Discussion

To create a Share menu, add [`UICommandTagShare`](./uicommandtagshare.md) to the `propertyList` of a [`UICommand`](./uicommand.md) or [`UIKeyCommand`](./uikeycommand.md) object.

```swift
// Ensure that the builder is modifying the menu bar system.
guard builder.system == UIMenuSystem.main else { return }

let shareCommand = UICommand(title: "Share",
                             action: #selector(share(_:)),
                             propertyList: UICommandTagShare)

let shareMenu = UIMenu(title: "", options: .displayInline, children: [shareCommand])

// Insert the menu into the File menu before the Close menu.
builder.insertSibling(shareMenu, beforeMenu: .close)
```

## See Also

### Associating data
- [var propertyList: Any?](./uicommand/propertylist.md)
  An object that contains data to associate with the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommandtagshare)*