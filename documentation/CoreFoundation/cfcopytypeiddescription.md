# CFCopyTypeIDDescription(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a textual description of a Core Foundation type, as identified by its type ID, which can be used when debugging.

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
func CFCopyTypeIDDescription(_ type_id: CFTypeID) -> CFString!
```

#### Return Value

A string containing a type description. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

You can use this function for debugging Core Foundation objects in your code. Note, however, that the description for a given object may be different in different releases of the operating system. Do   create dependencies in your code on the content or format of the information returned by this function.

## Parameters

- `type_id`: An integer of type   that uniquely identifies a Core Foundation opaque type.

## See Also

- [func CFCopyDescription(CFTypeRef!) -> CFString!](cfcopydescription(_:).md)
  Returns a textual description of a Core Foundation object.
- [func CFGetTypeID(CFTypeRef!) -> CFTypeID](cfgettypeid(_:).md)
  Returns the unique identifier of an opaque type to which a Core Foundation object belongs.
- [func CFShow(CFTypeRef!)](cfshow(_:).md)
  Prints a description of a Core Foundation object to stderr.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcopytypeiddescription(_:))*