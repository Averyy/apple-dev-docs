# kCFTypeArrayCallBacks

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
let kCFTypeArrayCallBacks: CFArrayCallBacks
```

#### Discussion

Predefined [`CFArrayCallBacks`](cfarraycallbacks.md) structure containing a set of callbacks appropriate for use when the values in a CFArray are all CFType-derived objects. The retain callback is `CFRetain`, the release callback is `CFRelease`, the copy callback is `CFCopyDescription`, and the equal callback is `CFEqual`. Therefore, if you use this constant when creating the collection, items are automatically retained when added to the collection, and released when removed from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcftypearraycallbacks)*