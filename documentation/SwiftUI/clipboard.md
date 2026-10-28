# Clipboard

**Framework**: SwiftUI  
**Role**: API Collection

Enable people to move or duplicate items by issuing Copy and Paste commands.

## Overview

When people issue standard Copy and Cut commands, they expect to move items to the system’s Clipboard, from which they can paste the items into another place in the same app or into another app. Your app can participate in this activity if you add view modifiers that indicate how to respond to the standard commands.

![](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/clipboard-hero@2x.png)

In your copy and paste modifiers, provide or accept types that conform to the [`Transferable`](../CoreTransferable/transferable.md) protocol, or that inherit from the [`NSItemProvider`](../Foundation/nsitemprovider.md) class. When possible, prefer using transferable items.

## Topics

### Copying transferable items
- [func copyable<T>(@autoclosure () -> [T]) -> some View](./view/copyable%28_%29.md)
  Specifies a list of items to copy in response to the system’s Copy command.
- [func cuttable<T>(for: T.Type, action: () -> [T]) -> some View](./view/cuttable%28for,action%29.md)
  Specifies an action that moves items to the Clipboard in response to the system’s Cut command.
- [func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T]) -> [T]) -> some View](./view/pastedestination%28for,action,validator%29.md)
  Specifies an action that adds validated items to a view in response to the system’s Paste command.
### Copying items using item providers
- [func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View](./view/oncopycommand%28perform%29.md)
  Adds an action to perform in response to the system’s Copy command.
- [func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View](./view/oncutcommand%28perform%29.md)
  Adds an action to perform in response to the system’s Cut command.
- [func onPasteCommand(of:perform:)](./view/onpastecommand%28of,perform%29.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand(of:validator:perform:)](./view/onpastecommand%28of,validator,perform%29.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.

## See Also

### Event handling
- [Gestures](./gestures.md)
  Define interactions from taps, clicks, and swipes to fine-grained gestures.
- [Input events](./input-events.md)
  Respond to input from a hardware device, like a keyboard or a Touch Bar.
- [Drag and drop](./drag-and-drop.md)
  Enable people to move or duplicate items by dragging them from one location to another.
- [Focus](./focus.md)
  Identify and control which visible object responds to user interaction.
- [System events](./system-events.md)
  React to system events, like opening a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/clipboard)*