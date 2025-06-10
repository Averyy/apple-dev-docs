# kCFCopyStringDictionaryKeyCallBacks

**Framework**: Core Foundation  
**Kind**: var

Predefined [`CFDictionaryKeyCallBacks`](cfdictionarykeycallbacks.md) structure containing a set of callbacks appropriate for use when the keys of a CFDictionary are all CFString objects, which may be mutable and need to be copied in order to serve as constant keys for the values in the dictionary.

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
let kCFCopyStringDictionaryKeyCallBacks: CFDictionaryKeyCallBacks
```

#### Discussion

You typically use a pointer to this constant when creating a new dictionary.

> ❗ **Important**:  For performance reasons, the default `kCFCopyStringDictionaryKeyCallBacks` behavior uses [`CFEqual(_:_:)`](cfequal(_:_:).md) which does not normalize the strings. This means that, for example, it does not consider CFStrings to be equal when they are the same but one is in pre-composed form (say, originating from a UTF-16 text file) and the other in decomposed form (say, originating from a file name). In cases where you use strings from different sources, you may want to pre-normalize the keys or else use a different set of functions to perform the comparison.

## See Also

- [let kCFTypeDictionaryKeyCallBacks: CFDictionaryKeyCallBacks](kcftypedictionarykeycallbacks.md)
  Predefined [`CFDictionaryKeyCallBacks`](cfdictionarykeycallbacks.md) structure containing a set of callbacks appropriate for use when the keys of a CFDictionary are all CFType-derived objects.
- [let kCFTypeDictionaryValueCallBacks: CFDictionaryValueCallBacks](kcftypedictionaryvaluecallbacks.md)
  Predefined [`CFDictionaryValueCallBacks`](cfdictionaryvaluecallbacks.md) structure containing a set of callbacks appropriate for use when the values in a CFDictionary are all CFType-derived objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfcopystringdictionarykeycallbacks)*