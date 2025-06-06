# ContactProviderError.extensionInvalidateTimeout

**Framework**: ContactProvider  
**Kind**: case

The extension invalidate operation timed out.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
case extensionInvalidateTimeout
```

#### Discussion

This can occur if the extension takes too long to return from [`invalidate()`](contactproviderextension/invalidate().md).

## See Also

- [ContactProviderError.extensionInvalidated](contactprovidererror/extensioninvalidated.md)
  The app invalidated the extension while it was enumerating content or changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidererror/extensioninvalidatetimeout)*