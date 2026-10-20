# CLKTextProvider

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

The common behavior for displaying text-based data in a complication.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKTextProvider
```

```objc
@interface CLKTextProvider : NSObject
```

#### Overview

Typically, you don’t create instances of this class yourself. Instead, you create instances of an appropriate subclass, based on the type of text data you’re trying to create. However, you can use the [`init(format:_:)`](./clktextprovider/init%28format,_%29.md) initializer or [`textProviderWithFormat:`](./clktextprovider/textproviderwithformat_.md) class method to create a compound text provider constructed from a format string and the data from other text providers.

## Topics

### Creating a Compound Text Provider
- [convenience init(format: String, any CVarArg...)](./clktextprovider/init%28format,_%29.md)
  Creates and returns a text provider built from the specified format string.
### Creating Localized Text Providers
- [class func localizableTextProvider(withStringsFileTextKey: String) -> Self](./clktextprovider/localizabletextprovider%28withstringsfiletextkey%29.md)
  Creates a localizable simple text provider using the strings file key for the text.
- [class func localizableTextProvider(withStringsFileTextKey: String, shortTextKey: String?) -> Self](./clktextprovider/localizabletextprovider%28withstringsfiletextkey,shorttextkey%29.md)
  Creates a localizable simple text provider using strings file keys for both the regular text and the shorter fallback text.
- [class func localizableTextProvider(withStringsFileFormatKey: String, textProviders: [CLKTextProvider]) -> Self](./clktextprovider/localizabletextprovider%28withstringsfileformatkey,textproviders%29.md)
  Creates a localizable text provider with a strings file key that resolves to a format string, and with text providers for the replacement arguments.
### Setting the Tint Color
- [var tintColor: UIColor](./clktextprovider/tintcolor.md)
  The tint color to use for text.
### Supporting Accessibility
- [var accessibilityLabel: String?](./clktextprovider/accessibilitylabel.md)
  A localized string that describes the text.
### Creating Empty Text Providers
- [init()](./clktextprovider/init%28%29.md)
  Creates an empty text provider.
- [class func new() -> Self](./clktextprovider/new%28%29.md)
  Creates an empty text provider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CLKDateTextProvider](./clkdatetextprovider.md)
- [CLKRelativeDateTextProvider](./clkrelativedatetextprovider.md)
- [CLKSimpleTextProvider](./clksimpletextprovider.md)
- [CLKTimeIntervalTextProvider](./clktimeintervaltextprovider.md)
- [CLKTimeTextProvider](./clktimetextprovider.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Text providers
- [class CLKSimpleTextProvider](./clksimpletextprovider.md)
  A single line of text to display in your complication interface.
- [class CLKDateTextProvider](./clkdatetextprovider.md)
  A formatted string that conveys a date without any time information.
- [class CLKRelativeDateTextProvider](./clkrelativedatetextprovider.md)
  A formatted string that conveys the difference in time between the current date and a date that you specify.
- [class CLKTimeIntervalTextProvider](./clktimeintervaltextprovider.md)
  A formatted time range.
- [class CLKTimeTextProvider](./clktimetextprovider.md)
  A formatted time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktextprovider)*