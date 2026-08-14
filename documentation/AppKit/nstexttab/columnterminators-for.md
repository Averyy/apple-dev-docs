# columnTerminators(for:)

**Framework**: AppKit  
**Kind**: method

Returns the column terminators for the specified locale.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class func columnTerminators(for aLocale: Locale?) -> CharacterSet
```

#### Return Value

The characters for the column terminators.

#### Discussion

The returned value can be used as the value for [`columnTerminators`](nstexttab/optionkey/columnterminators.md) to make a decimal tab stop.

## Parameters

- `aLocale`: The locale to use when determining the terminators. Specify `nil` to use the system’s current locale. You can get the user’s locale using the [`current`](https://developer.apple.com/documentation/foundation/nslocale/current) method of [`NSLocale`](https://developer.apple.com/documentation/foundation/nslocale).

## See Also

- [var alignment: NSTextAlignment](nstexttab/alignment.md)
  The text alignment of the text tab.
- [var options: [NSTextTab.OptionKey : Any]](nstexttab/options.md)
  The dictionary of attributes for the text tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttab/columnterminators(for:))*