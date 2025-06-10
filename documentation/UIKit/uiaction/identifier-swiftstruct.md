# UIAction.Identifier

**Framework**: UIKit  
**Kind**: struct

A type that represents an action identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct Identifier
```

## Topics

### Constants
- [static let paste: UIAction.Identifier](uiaction/identifier-swift.struct/paste.md)
  Identifies the action that pastes the current contents of the pasteboard into your app’s interface.
- [static let pasteAndGo: UIAction.Identifier](uiaction/identifier-swift.struct/pasteandgo.md)
  Identifies the action that pastes the current contents of the pasteboard into your app’s interface and navigates to the entity it references.
- [static let pasteAndMatchStyle: UIAction.Identifier](uiaction/identifier-swift.struct/pasteandmatchstyle.md)
  Identifies the action that pastes the current contents of the pasteboard into your app’s interface using the text style of the target.
- [static let pasteAndSearch: UIAction.Identifier](uiaction/identifier-swift.struct/pasteandsearch.md)
  Identifies the action that pastes the current contents of the pasteboard into your app’s interface and performs a search.
- [static let newFromPasteboard: UIAction.Identifier](uiaction/identifier-swift.struct/newfrompasteboard.md)
### Initializers
- [init(String)](uiaction/identifier-swift.struct/init(_:).md)
  Creates an action identifier from the specified string.
- [init(rawValue: String)](uiaction/identifier-swift.struct/init(rawvalue:).md)
  Creates an action identifier from the specified string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](uiaction/init(title:subtitle:image:identifier:discoverabilitytitle:attributes:state:handler:).md)
  Creates an action with the specified title, subtitle, image, identifier, discoverability title, attributes, state, and handler.
- [convenience init(title: String, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](uiaction/init(title:image:identifier:discoverabilitytitle:attributes:state:handler:).md)
  Creates an action with the specified title, image, identifier, discoverability title, attributes, state, and handler.
- [class func captureTextFromCamera(responder: any UIResponder & UIKeyInput, identifier: UIAction.Identifier?) -> Self](uiaction/capturetextfromcamera(responder:identifier:).md)
  Creates an action for capturing text using the device’s camera.
- [typealias UIActionHandler](uiactionhandler.md)
  A type that defines the closure for an action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaction/identifier-swift.struct)*