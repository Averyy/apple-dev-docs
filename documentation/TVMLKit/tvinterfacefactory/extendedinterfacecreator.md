# extendedInterfaceCreator

**Framework**: TVMLKit  
**Kind**: property

The interface that is being extended.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var extendedInterfaceCreator: (any TVInterfaceCreating)? { get set }
```

## Mentions

- [Creating TVML Elements](creating-tvml-elements.md)

#### Discussion

An app can extend or override framework implementation by setting the [`extendedInterfaceCreator`](tvinterfacefactory/extendedinterfacecreator.md) property. An app must provide its own methods to handle custom registered elements.

## See Also

- [class func shared() -> Self](tvinterfacefactory/shared.md)
  Returns the singleton instance of the interface factory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacefactory/extendedinterfacecreator)*