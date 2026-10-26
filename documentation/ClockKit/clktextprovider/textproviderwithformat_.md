# textProviderWithFormat:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a text provider built from the specified format string.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

## Declaration

```objc
+ (CLKTextProvider *) textProviderWithFormat:(NSString *) format;
```

#### Return Value

A text provider object built from the specified arguments.

#### Discussion

Use this method to create a text provider comprising text and the content of other objects, including other text providers.

##### Set Up Multicolor Text

The graphic complications support multicolor text in some text fields. To create multicolor text, build a composite text provider using two or more text providers with different tint colors.

```objc
CLKTextProvider *energyTextProvider = [CLKSimpleTextProvider textProviderWithText:myMoveString];
energyTextProvider.tintColor = myEnergyColor;

CLKTextProvider *exerciseTextProvider = [CLKSimpleTextProvider textProviderWithText:myExerciseString];
exerciseTextProvider.tintColor = myExerciseColor;

CLKTextProvider *standTextProvider = [CLKSimpleTextProvider textProviderWithText:myStandString];
standTextProvider.tintColor = myStandColor;

NSString *separatorString = NSLocalizedString(MY_LOCALIZED_SEPERATOR, @"Seperator for compound data strings.");

CLKTextProvider *multiColorTextProvider = [CLKTextProvider textProviderWithFormat:@"%@%@%@%@%@",
                                           energyTextProvider,
                                           separatorString,
                                           exerciseTextProvider,
                                           separatorString,
                                           standTextProvider];

multiColorTextProvider.tintColor = UIColor.darkTextColor;
```

Tinted graphic complications flatten multicolor text, and display the text using the tint color selected by the user.

## Parameters

- `format`: A format string to use when building the text provider. To insert content from another text provider into the string, use the `%@` placeholder. For more information and examples about the placeholders you can use in this string, see [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) and [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265). This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktextprovider/textproviderwithformat:)*