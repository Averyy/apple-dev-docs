# callAsFunction(_:)

**Framework**: UIKit  
**Kind**: method

Calls the transform closure of the text attributes transformer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
func callAsFunction(_ input: AttributeContainer) -> AttributeContainer
```

#### Return Value

A new, transformed attributes container.

#### Discussion

Using this syntax, you can call the text attributes transformer type as if it were a closure:

```swift
var container = AttributeContainer()
container.backgroundColor = UIColor.blue
let transformer = UIConfigurationTextAttributesTransformer { incoming in
    var outgoing = incoming
    outgoing.backgroundColor = incoming.backgroundColor?.withAlphaComponent(0.6)
    return outgoing
}
let transformed = transformer.callAsFunction(container)

```

## Parameters

- `input`: The current attributes container for a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct/callasfunction(_:))*