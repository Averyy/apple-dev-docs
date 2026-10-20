# client

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The owner of this input context. (read-only)

**Availability**:
- macOS 10.6+

## Declaration

```swift
var client: any NSTextInputClient { get }
```

```objc
@property (readonly) id<NSTextInputClient> client;
```

#### Discussion

The client (owner) of the input context, typically an `NSView` instance, retains its `NSTextInputContext` instance. The `NSTextInputContext` instance doesn’t retain its client.

## See Also

### Getting the Input Context and Client
- [class var current: NSTextInputContext?](./current.md)
  Returns the current, activated, text input context object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/client)*