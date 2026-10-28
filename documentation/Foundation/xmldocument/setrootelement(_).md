# setRootElement(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Set the root element of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setRootElement(_ root: XMLElement)
```

```objc
- (void) setRootElement:(NSXMLElement *) root;
```

## Discussion

As a side effect, this method removes all other children, including `NSXMLNode` objects representing comments and processing-instructions.

## Parameters

- `root`: An [`XMLNode`](../xmlnode.md) object that is to be the root element.

## See Also

### Managing the Root Element
- [func rootElement() -> XMLElement?](./rootelement%28%29.md)
  Returns the root element of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/setrootelement(_:))*