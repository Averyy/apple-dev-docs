# NSTouchBarDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that allows you to provide the items for a bar dynamically.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
protocol NSTouchBarDelegate : NSObjectProtocol
```

```objc
@protocol NSTouchBarDelegate <NSObject>
```

#### Overview

Use a bar delegate, according to the needs of your app, to dynamically create items ([`NSTouchBarItem`](./nstouchbaritem.md) instances). For more information, see [Item objects](./nstouchbar.md#Item-objects).

## Topics

### Providing bar items
- [func touchBar(NSTouchBar, makeItemForIdentifier: NSTouchBarItem.Identifier) -> NSTouchBarItem?](./nstouchbardelegate/touchbar%28_,makeitemforidentifier%29.md)
  Asks the delegate object for the bar item for the specified bar and item identifier.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSTextView](./nstextview.md)

## See Also

### Essentials
- [Integrating a Toolbar and Touch Bar into Your App](./integrating-a-toolbar-and-touch-bar-into-your-app.md)
  Provide users quick access to your app’s features from a toolbar and corresponding Touch Bar.
- [Creating and Customizing the Touch Bar](./creating-and-customizing-the-touch-bar.md)
  Adopt Touch Bar support by displaying interactive content and controls for your macOS apps.
- [class NSTouchBar](./nstouchbar.md)
  An object that provides dynamic contextual controls in the Touch Bar of supported models of MacBook Pro.
- [protocol NSTouchBarProvider](./nstouchbarprovider.md)
  A protocol that an object adopts to create a bar object in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbardelegate)*