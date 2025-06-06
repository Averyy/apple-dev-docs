# kCFTypeBagCallBacks

**Framework**: Core Foundation  
**Kind**: var

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
let kCFTypeBagCallBacks: CFBagCallBacks
```

#### Discussion

Predefined [`CFBagCallBacks`](cfbagcallbacks.md) structure containing a set of callbacks appropriate for use when the values in a CFBag are all CFType-derived objects. The retain callback is `CFRetain`, the release callback is `CFRelease`, the copy callback is `CFCopyDescription`, the equal callback is `CFEqual`, and the hash callback is `CFHash`. Therefore, if you use this constant when creating the collection, items are automatically retained when added to the collection, and released when removed from the collection.

## See Also

- [let kCFCopyStringBagCallBacks: CFBagCallBacks](kcfcopystringbagcallbacks.md)
  Predefined [`CFBagCallBacks`](cfbagcallbacks.md) structure containing a set of callbacks appropriate for use when the values in a CFBag are all CFString objects. The bag makes immutable copies of the strings placed into it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcftypebagcallbacks)*