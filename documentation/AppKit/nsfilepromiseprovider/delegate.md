# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 10.12+

## Declaration

```swift
weak var delegate: (any NSFilePromiseProviderDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSFilePromiseProviderDelegate> delegate;
```

## See Also

### Instance Properties
- [var fileType: String](./filetype.md)
  The file type of the file promise provider.
- [var userInfo: Any?](./userinfo.md)
  Optional user information to pass to the file promise provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromiseprovider/delegate)*