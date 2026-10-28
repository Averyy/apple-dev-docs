# ContactProviderError.enumerationTimeout

**Framework**: ContactProvider  
**Kind**: case  
**Role**: Case

The extension enumeration timed out.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
case enumerationTimeout
```

## Discussion

This can occur if the [`ContactItemEnumerator`](../contactitemenumerator.md) takes too long to enumerate a batch of content or changes.

## See Also

### Enumeration errors
- [ContactProviderError.cannotEnumerate](./cannotenumerate.md)
  The extension is unable to enumerate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidererror/enumerationtimeout)*