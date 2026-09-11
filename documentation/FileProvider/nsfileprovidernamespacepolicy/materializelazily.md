# NSFileProviderNamespacePolicy.materializeLazily

**Framework**: File Provider  
**Kind**: case

Enumerate this folder lazily (i.e upon access) if it is dataless. Keep populate new items below this folder eagerly if it’s already on disk.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case materializeLazily
```

#### Discussion

This is the default policy on the root.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidernamespacepolicy/materializelazily)*