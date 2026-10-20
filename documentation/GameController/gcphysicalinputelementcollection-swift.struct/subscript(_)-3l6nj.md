# subscript(_:)

**Framework**: Game Controller  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a contiguous subrange of a collection of button elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS

## Declaration

```swift
subscript(elementName: GCButtonElementName) -> T? { get }
```

Available when `T` is `any GCButtonElement`.

## See Also

### Accessing elements by name
- [subscript(GCDirectionPadElementName) -> T?](./subscript%28_%29-1twjd.md)
  Accesses a contiguous subrange of a collection of direction pad elements.
- [subscript(GCAxisElementName) -> T?](./subscript%28_%29-8m218.md)
  Accesses a contiguous subrange of a collection of axis elements.
- [subscript(GCSwitchElementName) -> T?](./subscript%28_%29-4oje0.md)
  Accesses a contiguous subrange of a collection of switch elements.
- [subscript(GCPhysicalInputElementName) -> T?](./subscript%28_%29-85c13.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputelementcollection-swift.struct/subscript(_:)-3l6nj)*