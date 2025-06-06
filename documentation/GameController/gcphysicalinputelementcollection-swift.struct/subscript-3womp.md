# subscript(_:)

**Framework**: Game Controller  
**Kind**: subscript

Accesses the collection’s elements using the element’s name.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
subscript<Name>(elementName: Name) -> Name.PhysicalInputElement? where Name : GCPhysicalInputElementTypedName { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputelementcollection-swift.struct/subscript(_:)-3womp)*