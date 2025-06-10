# AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes

**Framework**: Foundation  
**Kind**: struct

A type for using a localized string argument as an attribute.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct LocalizedStringArgumentAttributes
```

#### Overview

You use the this scope’s attributes when creating an attributed string from a [`LocalizedStringResource`](localizedstringresource.md). The process creating the attributed string may not have access to the original arguments passed to the interpolation. Instead, the attributed string marks formatted runs with this type, allowing you to retrieve the original values.

## Topics

### Retrieving localization arguments
- [let localizedNumericArgument: AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes.LocalizedNumericArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizednumericargument.md)
  The value of a numeric argument used to format the run with this attribute.
- [AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes.LocalizedNumericArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizednumericargumentattribute.md)
  A type for a numeric argument used to format the run with this attribute.
- [let localizedDateArgument: AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes.LocalizedDateArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizeddateargument.md)
  The date value used to format the run with this attribute.
- [AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes.LocalizedDateArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizeddateargumentattribute.md)
  A type for a date argument used to format the run with this attribute.
- [let localizedDateIntervalArgument: AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes.LocalizedDateIntervalArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizeddateintervalargument.md)
  The date interval value used to format the run with this attribute.
- [AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes.LocalizedDateIntervalArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizeddateintervalargumentattribute.md)
  A type for a date interval argument used to format the run with this attribute.
- [let localizedURLArgument: AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes.LocalizedURLArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizedurlargument.md)
  The URL value used to format the run with this attribute.
- [AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes.LocalizedURLArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizedurlargumentattribute.md)
  A type for a URL argument used to format the run with this attribute.

## See Also

- [let localizedStringArgumentAttributes: AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes](attributescopes/foundationattributes/localizedstringargumentattributes-swift.property.md)
  A property for accessing a localized string argument attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct)*