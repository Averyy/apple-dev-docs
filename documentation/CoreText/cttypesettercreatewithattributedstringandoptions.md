# CTTypesetterCreateWithAttributedStringAndOptions(_:_:)

**Framework**: Core Text  
**Kind**: func

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

#### Return Value

A reference to a typesetter object if the call is successful; otherwise, `NULL`.

#### Discussion

Use the typesetter to create lines, perform line breaking, and do other contextual analysis according to the characters in the string.

> ❗ **Important**:  By default, this function returns `NULL` if the string requires unreasonable effort to typeset. To create a typesetter that always typesets the text, regardless of the amount of effort, set the [`kCTTypesetterOptionAllowUnboundedLayout`](kcttypesetteroptionallowunboundedlayout.md) option to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue).

 By default, this function returns `NULL` if the string requires unreasonable effort to typeset. To create a typesetter that always typesets the text, regardless of the amount of effort, set the [`kCTTypesetterOptionAllowUnboundedLayout`](kcttypesetteroptionallowunboundedlayout.md) option to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue).

## Parameters

- `string`: The attributed string to typeset. This parameter must be a valid   object.
- `options`: A dictionary of typesetter options, or   if there are none.

## See Also

- [func CTTypesetterCreateWithAttributedString(CFAttributedString) -> CTTypesetter](cttypesettercreatewithattributedstring(_:).md)
  Creates an immutable typesetter object using an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttypesettercreatewithattributedstringandoptions(_:_:))*