# TVInterfaceCreating

**Framework**: TVMLKit  
**Kind**: protocol

A protocol that defines methods used to create views and view controllers.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
protocol TVInterfaceCreating : NSObjectProtocol
```

## Mentions

- [Creating TVML Elements](creating-tvml-elements.md)

#### Overview

This protocol contains methods used to create views and view controllers from a [`TVViewElement`](tvviewelement.md).

## Topics

### Retrieving Resource Information
- [func resourceImage(name: String) -> UIImage?](tvinterfacecreating/resourceimage(name:).md)
  Returns the image for the given resource
- [func resourceURL(name: String) -> URL?](tvinterfacecreating/resourceurl(name:).md)
  Returns a URL for the given resource.
### Updating View Information
- [func makeViewController(element: TVViewElement, existingViewController: UIViewController?) -> UIViewController?](tvinterfacecreating/makeviewcontroller(element:existingviewcontroller:).md)
  Returns a view controller for a view element.
- [func makeView(element: TVViewElement, existingView: UIView?) -> UIView?](tvinterfacecreating/makeview(element:existingview:).md)
  Returns a view for a view element.
- [func collectionViewCellClass(for: TVViewElement) -> AnyClass?](tvinterfacecreating/collectionviewcellclass(for:).md)
  Returns a collection view cell for the specified element.
- [func playerViewController(for: TVPlayer) -> UIViewController?](tvinterfacecreating/playerviewcontroller(for:).md)
  Returns the custom player user interface for a custom player.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [TVInterfaceFactory](tvinterfacefactory.md)

## See Also

- [class TVViewElement](tvviewelement.md)
  A representation of a read-only DOM node.
- [class TVInterfaceFactory](tvinterfacefactory.md)
  A factory for the creation of views and view controllers.
- [class TVBrowserViewController](tvbrowserviewcontroller.md)
  A view controller that presents content in a browsable, full-screen format.
- [class TVDocumentViewController](tvdocumentviewcontroller.md)
  A view controller that represents a TVMLKit document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating)*