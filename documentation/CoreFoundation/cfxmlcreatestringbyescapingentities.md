# CFXMLCreateStringByEscapingEntities(_:_:_:)

**Framework**: Corefoundation  
**Kind**: func

Given a CFString object containing XML source with unescaped entities, returns a string with specified XML entities escaped.

**Availability**:
- macOS ?+

## Declaration

```swift
func CFXMLCreateStringByEscapingEntities(_ allocator: CFAllocator!, _ string: CFString!, _ entitiesDictionary: CFDictionary!) -> CFString!
```

#### Return Value

A CFString object derived from `string` with substrings identified in `entitiesDictionary` escaped to their corresponding entities. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The standard five predefined entities are automatically supported.

As an example of using this function, say you apply this function to string “Refer to ¶ 5 of the contract” with a key of “para” mapped to “¶” in `entitiesDictionary`. The resulting string is “Refer to ¶ 5 of the contract”.

> **Note**:  Currently, only the standard predefined entities are supported; passing `NULL` for `entitiesDictionary` is sufficient.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `string`: Any CFString object that may contain XML source. This function translates any substring that is mapped to an entity in   to the specified entity.
- `entitiesDictionary`: Specifies the entities to be replaced. Dictionary keys should be the entity names (for example, “para” for ¶), and the values should be CFString objects containing the expansion. Pass   to indicate no entities other than the standard five.

## See Also

- [func CFXMLCreateStringByUnescapingEntities(CFAllocator!, CFString!, CFDictionary!) -> CFString!](cfxmlcreatestringbyunescapingentities(_:_:_:).md)
  Given a CFString object containing XML source with escaped entities, returns a string with specified XML entities unescaped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlcreatestringbyescapingentities(_:_:_:))*