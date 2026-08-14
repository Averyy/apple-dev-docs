# list(type:width:)

**Framework**: Foundation  
**Kind**: method

Returns a format style to format a list of strings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func list<Base>(type: ListFormatStyle<StringStyle, Base>.ListType, width: ListFormatStyle<StringStyle, Base>.Width = .standard) -> Self where Self == ListFormatStyle<StringStyle, Base>, Base : Sequence, Base.Element == String
```

#### Return Value

A list format style that formats a string array as a textual list of items.

#### Discussion

Use the dot-notation form of this type method when the call point allows the use of [`ListFormatStyle`](listformatstyle.md), and the [`Sequence`](https://developer.apple.com/documentation/swift/sequence) element type is [`String`](https://developer.apple.com/documentation/swift/string). You typically do this when calling the [`formatted(_:)`](https://developer.apple.com/documentation/swift/sequence/formatted(_:)) method of [`Sequence`](https://developer.apple.com/documentation/swift/sequence).

The following example creates an array of strings, then uses [`formatted(_:)`](https://developer.apple.com/documentation/swift/sequence/formatted(_:)) and the list format style provided by this method to format the items. It modifies the list format style to use the `en_US` locale, so the resulting string uses US English conventions for commas and conjunctions (“and”).

```swift
let items = ["Atlantic", "Pacific", "Indian", "Arctic", "Southern"]
let formatted = items.formatted(
    .list(type:.and)
    .locale(Locale(identifier: "en_US"))) // "Atlantic, Pacific, Indian, Arctic, and Southern"
```

## Parameters

- `type`: The list type to apply, such as cumulative ([`ListFormatStyle.ListType.and`](listformatstyle/listtype-swift.enum/and.md)) or alternative ([`ListFormatStyle.ListType.or`](listformatstyle/listtype-swift.enum/or.md)) elements.
- `width`: The width to use when formatting, such as [`ListFormatStyle.Width.standard`](listformatstyle/width-swift.enum/standard.md) or [`ListFormatStyle.Width.narrow`](listformatstyle/width-swift.enum/narrow.md).

## See Also

- [static func list<MemberStyle, Base>(memberStyle: MemberStyle, type: ListFormatStyle<MemberStyle, Base>.ListType, width: ListFormatStyle<MemberStyle, Base>.Width) -> Self](formatstyle/list(memberstyle:type:width:).md)
  Returns a format style to format a list of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/list(type:width:))*