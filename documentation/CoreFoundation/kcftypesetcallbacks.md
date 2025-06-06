# kCFTypeSetCallBacks

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
let kCFTypeSetCallBacks: CFSetCallBacks
```

#### Discussion

Predefined [`CFSetCallBacks`](cfsetcallbacks.md) structure containing a set of callbacks  appropriate for use when the values in a CFSet are all CFType-derived objects. The retain callback is [`CFRetain`](cfretain.md), the release callback is [`CFRelease`](cfrelease.md), the copy callback is [`CFCopyDescription(_:)`](cfcopydescription(_:).md), the equal callback is [`CFEqual(_:_:)`](cfequal(_:_:).md), and the hash callback is [`CFHash(_:)`](cfhash(_:).md). Therefore, if you use this constant when creating the collection, items are automatically retained when added to the collection, and released when removed from the collection.

## See Also

- [let kCFCopyStringSetCallBacks: CFSetCallBacks](kcfcopystringsetcallbacks.md)
  Predefined [`CFSetCallBacks`](cfsetcallbacks.md) structure containing a set of callbacks  appropriate for use when the values in a set are all CFString objects. The retain callback makes an immutable copy of strings added to the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcftypesetcallbacks)*