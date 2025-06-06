# init(data:)

**Framework**: Quartz  
**Kind**: init

Returns a composition object  initialized with the contents of a Quartz Composer composition file.

**Availability**:
- macOS 10.4+

## Declaration

```swift
init!(data: Data!)
```

#### Return Value

A Quartz Composer composition object or `nil` if there is an error.

## Parameters

- `data`: The contents of a file created with the Quartz Composer developer tool.

## See Also

- [init!(file: String!)](qccomposition/init(file:).md)
  Returns a composition object initialized with a Quartz Composer composition file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccomposition/init(data:))*