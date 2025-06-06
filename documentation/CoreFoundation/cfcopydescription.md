# CFCopyDescription(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a textual description of a Core Foundation object.

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
func CFCopyDescription(_ cf: CFTypeRef!) -> CFString!
```

#### Return Value

A string that contains a description of `cf`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The nature of the description differs by object. For example, a description of a CFArray object would include descriptions of each of the elements in the collection.

You can use this function for debugging Core Foundation objects in your code. Note, however, that the description for a given object may be different in different releases of the operating system. Do   create dependencies in your code on the content or format of the information returned by this function.

## Parameters

- `cf`: The CFType object (a generic reference of type  ) from which to derive a description.

## See Also

- [func CFCopyTypeIDDescription(CFTypeID) -> CFString!](cfcopytypeiddescription(_:).md)
  Returns a textual description of a Core Foundation type, as identified by its type ID, which can be used when debugging.
- [func CFGetTypeID(CFTypeRef!) -> CFTypeID](cfgettypeid(_:).md)
  Returns the unique identifier of an opaque type to which a Core Foundation object belongs.
- [func CFShow(CFTypeRef!)](cfshow(_:).md)
  Prints a description of a Core Foundation object to stderr.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcopydescription(_:))*