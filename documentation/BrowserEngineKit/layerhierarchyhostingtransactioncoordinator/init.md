# init()

**Framework**: BrowserEngineKit  
**Kind**: init

Creates a transaction coordinator.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init() throws
```

#### Discussion

This initializer can fail and throw an error if the process fails to retrieve a connection to the system’s Core Animation rendering server.

This method takes ownership of the port send right.

## See Also

- [init?(coder: NSCoder)](layerhierarchyhostingtransactioncoordinator/init(coder:).md)
  Creates a transaction coordinator from an encoded representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/init())*