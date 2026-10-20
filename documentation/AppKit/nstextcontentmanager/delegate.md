# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the content manager object.

**Availability**:
- macOS 12.0+

## Declaration

```swift
weak var delegate: (any NSTextContentManagerDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSTextContentManagerDelegate> delegate;
```

## See Also

### Customizing and validating text elements
- [protocol NSTextContentManagerDelegate](../nstextcontentmanagerdelegate.md)
  The optional methods that delegates of content manager objects implement for customizing or validating text elements.
- [NSTextContentManager.EnumerationOptions](./enumerationoptions.md)
  Values that control the order in which the framework enumerates text elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager/delegate)*