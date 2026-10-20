# columnTerminators(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the column terminators for the specified locale.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class func columnTerminators(for aLocale: Locale?) -> CharacterSet
```

```objc
+ (NSCharacterSet *) columnTerminatorsForLocale:(NSLocale *) aLocale;
```

#### Return Value

The characters for the column terminators.

#### Discussion

The returned value can be used as the value for [`columnTerminators`](./optionkey/columnterminators.md) to make a decimal tab stop.

## Parameters

- `aLocale`: The locale to use when determining the terminators. Specify `nil` to use the system’s current locale. You can get the user’s locale using the [`current`](../../Foundation/nslocale/current.md) method of [`NSLocale`](../../Foundation/nslocale.md).

## See Also

### Getting text tab information
- [var alignment: NSTextAlignment](./alignment.md)
  The text alignment of the text tab.
- [var options: [NSTextTab.OptionKey : Any]](./options.md)
  The dictionary of attributes for the text tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttab/columnterminators(for:))*