# init(file:)

**Framework**: Quartz  
**Kind**: init

Initializes and returns a composition layer using the Quartz Composer composition in the specified file.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init!(file path: String!)
```

#### Return Value

The initialized `QCCompositionLayer` object or `nil` if initialization is not successful.

## Parameters

- `path`: A string that specifies the location of a Quartz Composer composition.

## See Also

- [init!(composition: QCComposition!)](qccompositionlayer/init(composition:).md)
  Initializes and returns a  composition layer using the provided Quartz Composer composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionlayer/init(file:))*