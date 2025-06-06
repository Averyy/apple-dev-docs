# identifier()

**Framework**: Quartz  
**Kind**: method

Returns the unique and persistent identifier for the composition from the composition repository.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func identifier() -> String!
```

#### Return Value

The unique identifier for the composition if it comes from the composition repository; `nil` otherwise.

## See Also

- [func attributes() -> [AnyHashable : Any]!](qccomposition/attributes.md)
  Returns the attributes of the composition.
- [func protocols() -> [Any]!](qccomposition/protocols.md)
  Returns the list of protocols to which the composition conforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccomposition/identifier())*