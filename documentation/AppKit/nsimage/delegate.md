# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The image’s delegate object.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSImageDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSImageDelegate> delegate;
```

## Discussion

By default, this property contains `nil`.

## See Also

### Managing Loading and Drawing of Images
- [protocol NSImageDelegate](../nsimagedelegate.md)
  A set of optional methods that you can use to respond to drawing failures and manage incremental loads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/delegate)*