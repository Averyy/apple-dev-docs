# CTTypesetterCreateWithAttributedStringAndOptions(_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Creates an immutable typesetter object using an attributed string and a dictionary of options.

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
func CTTypesetterCreateWithAttributedStringAndOptions(_ string: CFAttributedString, _ options: CFDictionary?) -> CTTypesetter?
```

```c
extern CTTypesetterRefCTTypesetterCreateWithAttributedStringAndOptions(CFAttributedStringRef string, CFDictionaryRef options);
```

## Return Value

A reference to a typesetter object if the call is successful; otherwise, `NULL`.

## Discussion

Use the typesetter to create lines, perform line breaking, and do other contextual analysis according to the characters in the string.

> ❗ **Important**:  By default, this function returns `NULL` if the string requires unreasonable effort to typeset. To create a typesetter that always typesets the text, regardless of the amount of effort, set the [`kCTTypesetterOptionAllowUnboundedLayout`](./kcttypesetteroptionallowunboundedlayout.md) option to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md).

## Parameters

- `string`: The attributed string to typeset. This parameter must be a valid `CFAttributedString` object.
- `options`: A dictionary of typesetter options, or `NULL` if there are none.

## See Also

### Creating a Typesetter
- [func CTTypesetterCreateWithAttributedString(CFAttributedString) -> CTTypesetter](./cttypesettercreatewithattributedstring%28_%29.md)
  Creates an immutable typesetter object using an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttypesettercreatewithattributedstringandoptions(_:_:))*