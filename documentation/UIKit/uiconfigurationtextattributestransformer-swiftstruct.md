# UIConfigurationTextAttributesTransformer

**Framework**: UIKit  
**Kind**: struct

Defines a text transformation that can affect the visual appearance of a string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
struct UIConfigurationTextAttributesTransformer
```

#### Overview

Use a transformer to affect how your attributed text appears on the UI. You provide a closure when initializing the transformer. Your closure accepts a container with the current text attributes and returns a container with the new text attributes.

```swift
let transformer = UIConfigurationTextAttributesTransformer { incoming in
    var outgoing = incoming
    outgoing.foregroundColor = UIColor.black
    outgoing.font = UIFont.boldSystemFont(ofSize: 20)
    return outgoing
}
```

## Topics

### Creating a text attributes transformer
- [init((AttributeContainer) -> AttributeContainer)](uiconfigurationtextattributestransformer-swift.struct/init(_:).md)
  Creates a new text attributes transformer.
### Defining a text transformation
- [let transform: (AttributeContainer) -> AttributeContainer](uiconfigurationtextattributestransformer-swift.struct/transform.md)
  A closure that defines the text transformation.
### Calling a text transformer
- [func callAsFunction(AttributeContainer) -> AttributeContainer](uiconfigurationtextattributestransformer-swift.struct/callasfunction(_:).md)
  Calls the transform closure of the text attributes transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct)*