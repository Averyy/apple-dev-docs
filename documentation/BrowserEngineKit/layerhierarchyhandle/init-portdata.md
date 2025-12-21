# init(port:data:)

**Framework**: BrowserEngineKit  
**Kind**: init

Decodes a handle form a `mach_port_t` send right and its accompanying metadata.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
init(port: mach_port_t, data: Data) throws
```

#### Discussion

- This method takes ownership of the port right (even if it returns an error).


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhandle/init(port:data:))*