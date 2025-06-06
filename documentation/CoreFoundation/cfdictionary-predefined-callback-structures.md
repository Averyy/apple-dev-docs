# Predefined Callback Structures

**Framework**: Core Foundation

CFDictionary provides some predefined callbacks for your convenience.

## Topics

### Constants
- [let kCFCopyStringDictionaryKeyCallBacks: CFDictionaryKeyCallBacks](kcfcopystringdictionarykeycallbacks.md)
  Predefined [`CFDictionaryKeyCallBacks`](cfdictionarykeycallbacks.md) structure containing a set of callbacks appropriate for use when the keys of a CFDictionary are all CFString objects, which may be mutable and need to be copied in order to serve as constant keys for the values in the dictionary.
- [let kCFTypeDictionaryKeyCallBacks: CFDictionaryKeyCallBacks](kcftypedictionarykeycallbacks.md)
  Predefined [`CFDictionaryKeyCallBacks`](cfdictionarykeycallbacks.md) structure containing a set of callbacks appropriate for use when the keys of a CFDictionary are all CFType-derived objects.
- [let kCFTypeDictionaryValueCallBacks: CFDictionaryValueCallBacks](kcftypedictionaryvaluecallbacks.md)
  Predefined [`CFDictionaryValueCallBacks`](cfdictionaryvaluecallbacks.md) structure containing a set of callbacks appropriate for use when the values in a CFDictionary are all CFType-derived objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionary-predefined-callback-structures)*