# current

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the current, activated, text input context object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class var current: NSTextInputContext? { get }
```

```objc
@property (class, strong, readonly, nullable) NSTextInputContext * currentInputContext;
```

## See Also

### Getting the Input Context and Client
- [var client: any NSTextInputClient](./client.md)
  The owner of this input context. (read-only)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/current)*