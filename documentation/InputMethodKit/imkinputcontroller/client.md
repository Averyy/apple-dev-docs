# client()

**Framework**: InputMethodKit  
**Kind**: method

Returns the client object associated with the input controller.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func client() -> (any IMKTextInput & NSObjectProtocol)!
```

#### Return Value

The client object.

#### Discussion

The client object conforms to the `IMKTextInput` protocol.

## See Also

- [func server() -> IMKServer!](imkinputcontroller/server.md)
  Returns the server object that manages the input controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/client())*