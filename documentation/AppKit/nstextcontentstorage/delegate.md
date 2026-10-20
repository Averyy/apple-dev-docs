# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the content storage object.

**Availability**:
- macOS 12.0+

## Declaration

```swift
weak var delegate: (any NSTextContentStorageDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSTextContentStorageDelegate> delegate;
```

## See Also

### Accessing paragraphs
- [protocol NSTextContentStorageDelegate](../nstextcontentstoragedelegate.md)
  The optional methods that delegates of content storage objects implement to handle content processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentstorage/delegate)*