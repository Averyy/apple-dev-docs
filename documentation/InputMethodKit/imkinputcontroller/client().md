# client()

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Returns the client object associated with the input controller.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func client() -> (any IMKTextInput & NSObjectProtocol)!
```

```objc
- (id<IMKTextInput,NSObject>) client;
```

#### Return Value

The client object.

#### Discussion

The client object conforms to the `IMKTextInput` protocol.

## See Also

### Getting the Client and Server Objects
- [func server() -> IMKServer!](./server%28%29.md)
  Returns the server object that manages the input controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/client())*