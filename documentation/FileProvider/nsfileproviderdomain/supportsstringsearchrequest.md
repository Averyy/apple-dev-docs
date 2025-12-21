# supportsStringSearchRequest

**Framework**: File Provider  
**Kind**: property

A Boolean value that indicates whether the provider supports search.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var supportsStringSearchRequest: Bool { get set }
```

#### Discussion

If this value is `true`, the framework uses the extension’s [`NSFileProviderSearching`](nsfileprovidersearching.md) implementation to support search.

The property defaults to `false` (Swift) or `NO` (Objective-C).


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/supportsstringsearchrequest)*