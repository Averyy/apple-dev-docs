# CTTypesetterCreateWithAttributedString(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Creates an immutable typesetter object using an attributed string.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTTypesetterCreateWithAttributedString(_ string: CFAttributedString) -> CTTypesetter
```

```c
extern CTTypesetterRefCTTypesetterCreateWithAttributedString(CFAttributedStringRef string);
```

## Return Value

A reference to a CTTypesetter object if the call was successful; otherwise, `NULL`.

## Discussion

The resultant typesetter can be used to create lines, perform line breaking, and do other contextual analysis based on the characters in the string.

## Parameters

- `string`: The attributed string to typeset. This parameter must be filled in with a valid CFAttributedString object.

## See Also

### Creating a Typesetter
- [func CTTypesetterCreateWithAttributedStringAndOptions(CFAttributedString, CFDictionary?) -> CTTypesetter?](./cttypesettercreatewithattributedstringandoptions%28_,_%29.md)
  Creates an immutable typesetter object using an attributed string and a dictionary of options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttypesettercreatewithattributedstring(_:))*