# setRootElement(_:)

**Framework**: Foundation  
**Kind**: method

Set the root element of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setRootElement(_ root: XMLElement)
```

#### Discussion

As a side effect, this method removes all other children, including `NSXMLNode` objects representing comments and processing-instructions.

## Parameters

- `root`: An   object that is to be the root element.

## See Also

- [func rootElement() -> XMLElement?](xmldocument/rootelement.md)
  Returns the root element of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/setrootelement(_:))*