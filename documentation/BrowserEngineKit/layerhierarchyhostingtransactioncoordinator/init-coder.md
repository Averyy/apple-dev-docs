# init(coder:)

**Framework**: BrowserEngineKit  
**Kind**: init

Creates a transaction coordinator from an encoded representation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init?(coder: NSCoder)
```

#### Discussion

This initializer can fail and return `nil` if the specified `coder` fails to decode.

## Parameters

- `coder`: An object that contains the encoded representation of the transaction coordinator.

## See Also

- [init() throws](layerhierarchyhostingtransactioncoordinator/init.md)
  Creates a transaction coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/init(coder:))*