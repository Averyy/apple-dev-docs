# CFXMLCreateStringByUnescapingEntities(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Given a CFString object containing XML source with escaped entities, returns a string with specified XML entities unescaped.

**Availability**:
- macOS

## Declaration

```swift
func CFXMLCreateStringByUnescapingEntities(_ allocator: CFAllocator!, _ string: CFString!, _ entitiesDictionary: CFDictionary!) -> CFString!
```

```c
extern CFStringRefCFXMLCreateStringByUnescapingEntities(CFAllocatorRef allocator, CFStringRef string, CFDictionaryRef entitiesDictionary);
```

## Return Value

A CFString object derived from `string` with entities identified in `entitiesDictionary` unescaped to their corresponding substrings. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The standard five predefined entities are automatically supported.

As an example of using this function, say you apply this function to string “Refer to ¶ 5 of the contract” with a key of “para” mapped to “¶” in `entitiesDictionary`. The resulting string is “Refer to ¶ 5 of the contract”.

> **Note**:  Currently, only the standard predefined entities are supported; passing `NULL` for `entitiesDictionary` is sufficient.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `string`: Any CFString object that may contain XML source. This function translates any entity that is mapped to an substring in `entitiesDictionary` to the specified substring.
- `entitiesDictionary`: Specifies the entities to be replaced. Dictionary keys should be the entity names (for example, “para” for ¶), and the values should be CFString objects containing the expansion. Pass `NULL` to indicate no entities other than the standard five.

## See Also

### CFXMLTree Miscellaneous Functions
- [func CFXMLCreateStringByEscapingEntities(CFAllocator!, CFString!, CFDictionary!) -> CFString!](./cfxmlcreatestringbyescapingentities%28_,_,_%29.md)
  Given a CFString object containing XML source with unescaped entities, returns a string with specified XML entities escaped.
- [CFXMLTreeCreateFromData](./cfxmltreecreatefromdata.md)
  Parses the given XML data and returns the resulting CFXMLTree object.
- [CFXMLTreeCreateFromDataWithError](./cfxmltreecreatefromdatawitherror.md)
  Parses the given XML data and returns the resulting CFXMLTree object and any error information.
- [CFXMLTreeCreateWithDataFromURL](./cfxmltreecreatewithdatafromurl.md)
  Creates a new CFXMLTree object by loading the data to be parsed directly from a data source.
- [CFXMLTreeCreateWithNode](./cfxmltreecreatewithnode.md)
  Creates a childless, parentless CFXMLTree object node for a CFXMLNode object.
- [CFXMLTreeCreateXMLData](./cfxmltreecreatexmldata.md)
  Generates an XML document from a CFXMLTree object which is ready to be written to permanent storage.
- [CFXMLTreeGetNode](./cfxmltreegetnode.md)
  Returns the node of a CFXMLTree object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlcreatestringbyunescapingentities(_:_:_:))*