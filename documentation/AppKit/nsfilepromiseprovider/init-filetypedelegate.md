# init(fileType:delegate:)

**Framework**: AppKit  
**Kind**: init

Initializes a file promise provider for a certain file type.

**Availability**:
- macOS 10.12+

## Declaration

```swift
convenience init(fileType: String, delegate: any NSFilePromiseProviderDelegate)
```

## Parameters

- `fileType`: A string describing the file type.
- `delegate`: An object that conforms to the NSFilePromiseProviderDelegate protocol, for providing promised file data.

## See Also

- [init()](nsfilepromiseprovider/init.md)
  Initializes a file promise provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromiseprovider/init(filetype:delegate:))*