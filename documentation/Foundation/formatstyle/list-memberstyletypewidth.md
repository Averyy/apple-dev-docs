# list(memberStyle:type:width:)

**Framework**: Foundation  
**Kind**: method

Returns a format style to format a list of items.

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
static func list<MemberStyle, Base>(memberStyle: MemberStyle, type: ListFormatStyle<MemberStyle, Base>.ListType, width: ListFormatStyle<MemberStyle, Base>.Width = .standard) -> Self where Self == ListFormatStyle<MemberStyle, Base>, MemberStyle : FormatStyle, Base : Sequence, MemberStyle.FormatInput == Base.Element, MemberStyle.FormatOutput == String
```

#### Return Value

A list format style that formats an array as a textual list of items.

#### Discussion

Use the dot-notation form of this type method when the call point allows the use of [`ListFormatStyle`](listformatstyle.md). You typically do this when calling the [`formatted(_:)`](https://developer.apple.com/documentation/Swift/Sequence/formatted(_:)) method of [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence).

The following example creates an array of integers, then uses [`formatted(_:)`](https://developer.apple.com/documentation/Swift/Sequence/formatted(_:)) and the list format style provided by this method to format the items. By using a currency [`IntegerFormatStyle`](integerformatstyle.md), the list format style expresses each member as US dollars. The example also modifies the list format style to use the `en_US` locale, so the resulting string uses US English conventions for commas and conjunctions (“and”).

```swift
let items: [Int] = [100, 1000, 10000, 100000, 1000000]
let formatted = items.formatted(
    .list(memberStyle: .currency(code: "USD"),
          type: .and)
    .locale(Locale(identifier: "en_US"))) // "$100.00, $1,000.00, $10,000.00, $100,000.00, and $1,000,000.00"
```

## Parameters

- `memberStyle`: The format style to apply to each item in the list.
- `type`: The list type to apply, such as cumulative ( ) or alternative ( ) elements.
- `width`: The width to use when formatting, such as   or  .

## See Also

- [static func list<Base>(type: ListFormatStyle<StringStyle, Base>.ListType, width: ListFormatStyle<StringStyle, Base>.Width) -> Self](formatstyle/list(type:width:).md)
  Returns a format style to format a list of strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/list(memberstyle:type:width:))*