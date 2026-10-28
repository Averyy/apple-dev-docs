# initWithFormat:options:locale:context:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initializes an attributed string by substituting arguments into a specially formatted string and applying additional contextual information.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
- (instancetype) initWithFormat:(NSAttributedString *) format options:(NSAttributedStringFormattingOptions) options locale:(NSLocale *) locale context:(NSDictionary<NSString *,id> *) context;
```

## Return Value

An initialized attributed string that combines the format string with the provided arguments and other information.

## Discussion

Pass an optional list of trailing variadic arguments to substitute into the `format` string.

## Parameters

- `format`: The format string to use to create the final string. For a list of format specifiers you can include in this string, see [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265).
- `options`: Options for how to apply attributes to the string’s content.
- `locale`: The locale to use for formatting the string. The locale controls the formatting of region-sensitive values such as numbers and currencies.
- `context`: Additional options to apply to the string.

## See Also

### Creating a formatted string
- [- initWithFormat:options:locale:](./initwithformat_options_locale_.md)
  Initializes an attributed string by substituting arguments into a specially formatted string.
- [- initWithFormat:options:locale:arguments:](./initwithformat_options_locale_arguments_.md)
  Initializes an attributed string by substituting a list of function arguments into a specially formatted string.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/initwithformat:options:locale:context:)*