# request()

**Framework**: BrowserEngineKit  
**Kind**: method

Requests the capability to be granted to the current process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
func request() throws -> ProcessCapability.Grant
```

#### Discussion

Returns the granted capability or throws an error if it can not be granted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/request())*