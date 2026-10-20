# init(fileType:delegate:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a file promise provider for a certain file type.

**Availability**:
- macOS 10.12+

## Declaration

```swift
convenience init(fileType: String, delegate: any NSFilePromiseProviderDelegate)
```

```objc
- (instancetype) initWithFileType:(NSString *) fileType delegate:(id<NSFilePromiseProviderDelegate>) delegate;
```

## Parameters

- `fileType`: A string describing the file type.
- `delegate`: An object that conforms to the NSFilePromiseProviderDelegate protocol, for providing promised file data.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Initializes a file promise provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromiseprovider/init(filetype:delegate:))*