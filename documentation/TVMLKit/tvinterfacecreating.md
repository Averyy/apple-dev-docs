# TVInterfaceCreating

**Framework**: TVMLKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines methods used to create views and view controllers.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
protocol TVInterfaceCreating : NSObjectProtocol
```

```objc
@protocol TVInterfaceCreating <NSObject>
```

## Mentions

- [Creating TVML Elements](./creating-tvml-elements.md)

## Overview

This protocol contains methods used to create views and view controllers from a [`TVViewElement`](./tvviewelement.md).

## Topics

### Retrieving Resource Information
- [func resourceImage(name: String) -> UIImage?](./tvinterfacecreating/resourceimage%28name%29.md)
  Returns the image for the given resource
- [func resourceURL(name: String) -> URL?](./tvinterfacecreating/resourceurl%28name%29.md)
  Returns a URL for the given resource.
### Updating View Information
- [func makeViewController(element: TVViewElement, existingViewController: UIViewController?) -> UIViewController?](./tvinterfacecreating/makeviewcontroller%28element,existingviewcontroller%29.md)
  Returns a view controller for a view element.
- [func makeView(element: TVViewElement, existingView: UIView?) -> UIView?](./tvinterfacecreating/makeview%28element,existingview%29.md)
  Returns a view for a view element.
- [func collectionViewCellClass(for: TVViewElement) -> AnyClass?](./tvinterfacecreating/collectionviewcellclass%28for%29.md)
  Returns a collection view cell for the specified element.
- [func playerViewController(for: TVPlayer) -> UIViewController?](./tvinterfacecreating/playerviewcontroller%28for%29.md)
  Returns the custom player user interface for a custom player.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [TVInterfaceFactory](./tvinterfacefactory.md)

## See Also

### Views and View Controllers
- [class TVViewElement](./tvviewelement.md)
  A representation of a read-only DOM node.
- [class TVInterfaceFactory](./tvinterfacefactory.md)
  A factory for the creation of views and view controllers.
- [class TVBrowserViewController](./tvbrowserviewcontroller.md)
  A view controller that presents content in a browsable, full-screen format.
- [class TVDocumentViewController](./tvdocumentviewcontroller.md)
  A view controller that represents a TVMLKit document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating)*