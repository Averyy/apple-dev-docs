# TVMLKit

**Framework**: TVMLKit  
**Kind**: module

Create client-server apps by incorporating JavaScript and TVML files in your binary app.

**Availability**:
- tvOS 9.0+

#### Overview

The TVMLKit framework enables you to evaluate TVMLKit JS and TVML files from within your tvOS app. You can create TVML elements, styles, views, and view controllers through the JavaScript environment.

## Topics

### JavaScript Environment
- [Implementing a Hybrid TV App with TVMLKit](implementing-a-hybrid-tv-app-with-tvmlkit.md)
  Display content options with document view controllers and fetch and populate content with TVMLKit JS.
- [class TVApplicationController](tvapplicationcontroller.md)
  An object that bridges the UI, navigation stack, storage, and event handling from JavaScript.
- [class TVApplicationControllerContext](tvapplicationcontrollercontext.md)
  Launch information provided to the TV application controller.
### Views and View Controllers
- [class TVViewElement](tvviewelement.md)
  A representation of a read-only DOM node.
- [protocol TVInterfaceCreating](tvinterfacecreating.md)
  A protocol that defines methods used to create views and view controllers.
- [class TVInterfaceFactory](tvinterfacefactory.md)
  A factory for the creation of views and view controllers.
- [class TVBrowserViewController](tvbrowserviewcontroller.md)
  A view controller that presents content in a browsable, full-screen format.
- [class TVDocumentViewController](tvdocumentviewcontroller.md)
  A view controller that represents a TVMLKit document.
### Custom Elements
- [class TVElementFactory](tvelementfactory.md)
  An object used to register new elements to extend the Apple TV Markup Language (TVML).
- [class TVImageElement](tvimageelement.md)
  A representation of a read-only DOM node containing the attributes that describe an image element.
- [class TVTextElement](tvtextelement.md)
  The textual content for the DOM element.
- [Creating TVML Elements](creating-tvml-elements.md)
  Avoid rewriting complex and often used elements by creating a simplified custom element.
### Custom Styles
- [class TVViewElementStyle](tvviewelementstyle.md)
  A style applied to a view element.
- [class TVStyleFactory](tvstylefactory.md)
  An object used to register custom style properties.
- [class TVColor](tvcolor.md)
  The color data used by styles.
### Custom Player
- [class TVMediaItem](tvmediaitem.md)
  A single audio or video item associated with the Apple TV JavaScript player.
- [class TVPlaylist](tvplaylist.md)
  A collection of media items associated with the Apple TV JavaScript player.
- [class TVPlayer](tvplayer.md)
  A customizable native media player used to control playback from the JavaScript player used in an Apple TV client-server app.
### Errors
- [let TVMLKitErrorDomain: String](tvmlkiterrordomain.md)
  An error occurred in TVMLKit.
- [enum TVMLKitError](tvmlkiterror.md)
  Error codes for the TVMLKit error domain.
- [struct TVDocumentError](tvdocumenterror-swift.struct.md)
### Reference
- [TVMLKit Enumerations](tvmlkit-enumerations.md)
- [TVMLKit Constants](tvmlkit-constants.md)
  This document defines constants in the TVMLKit framework that are not associated with a particular class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TVMLKit)*