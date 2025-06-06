# subscript(_:)

**Framework**: Metal  
**Kind**: subscript

Returns the state of the specified attribute.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
subscript(index: Int) -> MTLAttributeDescriptor! { get set }
```

#### Return Value

The attribute descriptor for data bound at this index.

## Parameters

- `index`: A specified index in the argument table bindings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlattributedescriptorarray/subscript(_:))*