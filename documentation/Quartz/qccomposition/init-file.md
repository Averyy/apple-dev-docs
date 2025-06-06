# init(file:)

**Framework**: Quartz  
**Kind**: init

Returns a composition object initialized with a Quartz Composer composition file.

**Availability**:
- macOS 10.4+

## Declaration

```swift
init!(file path: String!)
```

#### Return Value

A Quartz Composer composition object or `nil` if there is an error.

## Parameters

- `path`: A path to a file created with the Quartz Composer developer tool (  extension).

## See Also

- [init!(data: Data!)](qccomposition/init(data:).md)
  Returns a composition object  initialized with the contents of a Quartz Composer composition file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccomposition/init(file:))*