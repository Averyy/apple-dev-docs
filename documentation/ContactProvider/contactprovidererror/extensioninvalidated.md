# ContactProviderError.extensionInvalidated

**Framework**: ContactProvider  
**Kind**: case  
**Role**: Case

The app invalidated the extension while it was enumerating content or changes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
case extensionInvalidated
```

#### Discussion

A loaded and enumerating extension can become invalidated for many reasons, including:

- The app invalidates the extension by calling [`invalidate()`](../contactprovidermanager/invalidate%28%29.md).
- The app disables the domain by calling [`disable()`](../contactprovidermanager/disable%28%29.md).
- The app resets the domain by calling [`reset()`](../contactprovidermanager/reset%28%29.md).
- The person using the app disables the domain in the Settings app.

## See Also

### Invalidation errors
- [ContactProviderError.extensionInvalidateTimeout](./extensioninvalidatetimeout.md)
  The extension invalidate operation timed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidererror/extensioninvalidated)*