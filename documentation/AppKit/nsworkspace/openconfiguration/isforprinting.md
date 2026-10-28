# isForPrinting

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether you want to print the contents of documents and URLs instead of opening them.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var isForPrinting: Bool { get set }
```

```objc
@property (getter=isForPrinting) BOOL forPrinting;
```

## Discussion

The default value of this property is [`false`](../../../Swift/false.md), which causes the app to open documents and URLs. Set the value to [`true`](../../../Swift/true.md) if you want the app to print the items instead.

## See Also

### Handling URLs
- [var requiresUniversalLinks: Bool](./requiresuniversallinks.md)
  A Boolean value indicating whether you require the URL to have an associated universal link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/isforprinting)*