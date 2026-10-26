# initWithFormat:options:locale:arguments:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initializes an attributed string by substituting a list of function arguments into a specially formatted string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
- (instancetype) initWithFormat:(NSAttributedString *) format options:(NSAttributedStringFormattingOptions) options locale:(NSLocale *) locale arguments:(va_list) arguments;
```

#### Return Value

An initialized attributed string that combines the format string with the provided arguments and other information.

## Parameters

- `format`: The format string to use to create the final string. For a list of format specifiers you can include in this string, see [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265).
- `options`: Options for how to apply attributes to the string’s content.
- `locale`: The locale to use for formatting the string. The locale controls the formatting of region-sensitive values such as numbers and currencies.
- `arguments`: A list of arguments to substitute into the `format` string.

## See Also

### Creating a formatted string
- [- initWithFormat:options:locale:](./initwithformat_options_locale_.md)
  Initializes an attributed string by substituting arguments into a specially formatted string.
- [- initWithFormat:options:locale:context:](./initwithformat_options_locale_context_.md)
  Initializes an attributed string by substituting arguments into a specially formatted string and applying additional contextual information.
- [- initWithFormat:options:locale:context:arguments:](./initwithformat_options_locale_context_arguments_.md)
  Initializes an attributed string by substituting a list of function arguments into a specially formatted string and applying additional contextual information.
- [+ localizedAttributedStringWithFormat:](./localizedattributedstringwithformat_.md)
  Creates an attributed string by substituting arguments into a specially formatted string.
- [+ localizedAttributedStringWithFormat:options:](./localizedattributedstringwithformat_options_.md)
  Creates an attributed string by substituting a list of function arguments into a specially formatted string.
- [+ localizedAttributedStringWithFormat:context:](./localizedattributedstringwithformat_context_.md)
  Creates an attributed string by substituting arguments into a specially formatted string and applying additional contextual information.
- [+ localizedAttributedStringWithFormat:options:context:](./localizedattributedstringwithformat_options_context_.md)
  Creates an attributed string by substituting a list of function arguments into a specially formatted string and applying additional contextual information.
- [NSAttributedStringFormattingOptions](../nsattributedstringformattingoptions.md)
  Options to use when creating an attributed string from a format string and variable list of arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/initwithformat:options:locale:arguments:)*