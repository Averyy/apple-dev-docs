# subscript(_:)

**Framework**: Game Controller  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a contiguous subrange of a collection of axis elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS

## Declaration

```swift
subscript(elementName: GCAxisElementName) -> T? { get }
```

Available when `T` is `any GCAxisElement`.

## See Also

### Accessing elements by name
- [subscript(GCDirectionPadElementName) -> T?](./subscript%28_%29-1twjd.md)
  Accesses a contiguous subrange of a collection of direction pad elements.
- [subscript(GCButtonElementName) -> T?](./subscript%28_%29-3l6nj.md)
  Accesses a contiguous subrange of a collection of button elements.
- [subscript(GCSwitchElementName) -> T?](./subscript%28_%29-4oje0.md)
  Accesses a contiguous subrange of a collection of switch elements.
- [subscript(GCPhysicalInputElementName) -> T?](./subscript%28_%29-85c13.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputelementcollection-swift.struct/subscript(_:)-8m218)*