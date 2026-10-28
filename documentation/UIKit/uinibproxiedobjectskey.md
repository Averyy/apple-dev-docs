# UINibProxiedObjectsKey

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

The runtime replacement objects for any proxy objects in the nib file.

**Availability**:
- iOS 2.0+ - Deprecated in 3.0
- iPadOS 2.0+ - Deprecated in 3.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`externalObjects`](./uinib/optionskey/externalobjects.md) key instead.

## Declaration

```c
extern NSString * const UINibProxiedObjectsKey;
```

## Discussion

In iOS 2, the value for this key is a dictionary that contains the runtime replacement objects for any proxy objects used in the nib file. In this dictionary, the keys are the names associated with the proxy objects and the values are the actual objects from your code that should be used in their place.

## See Also

### Retrieving objects from the nib file
- [func instantiate(withOwner: Any?, options: [UINib.OptionsKey : Any]?) -> [Any]](./uinib/instantiate%28withowner,options%29.md)
  Unarchives and instantiates the in-memory contents of the nib object’s nib file, creating a distinct object tree and set of top-level objects.
- [struct OptionsKey](./uinib/optionskey.md)
  Options that specify how to unarchive and instantiate the nib.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinibproxiedobjectskey)*