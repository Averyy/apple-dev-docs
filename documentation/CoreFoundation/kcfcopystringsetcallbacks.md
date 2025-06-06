# kCFCopyStringSetCallBacks

**Framework**: Core Foundation  
**Kind**: var

Predefined [`CFSetCallBacks`](cfsetcallbacks.md) structure containing a set of callbacks  appropriate for use when the values in a set are all CFString objects. The retain callback makes an immutable copy of strings added to the set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
let kCFCopyStringSetCallBacks: CFSetCallBacks
```

## See Also

- [let kCFTypeSetCallBacks: CFSetCallBacks](kcftypesetcallbacks.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfcopystringsetcallbacks)*