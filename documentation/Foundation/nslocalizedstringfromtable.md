# NSLocalizedStringFromTable

**Framework**: Foundation  
**Kind**: macro  
**Role**: Macro

Returns a localized version of a string from the table that you specify, which Xcode autogenerates when exporting localizations.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
#define NSLocalizedStringFromTable(key, tbl, comment)
```

#### Return Value

The result of invoking [`localizedString(forKey:value:table:)`](./bundle/localizedstring%28forkey,value,table%29.md) on the main bundle, passing the specified `key` and `tableName`.

#### Discussion

Use this macro to automatically generate a strings file named `[tableName].strings` from your code when exporting localizations from Xcode or the `genstrings` utility. You can specify Unicode characters in `key` using `\\Uxxxx`—see the `-u` option for the `genstrings` utility.

The initial value for `key` in the strings file is `key`. To avoid collisions between words or phrases with multiple meanings, use a unique `key` for each use of the same phrase. Use the [`NSLocalizedStringWithDefaultValue`](./nslocalizedstringwithdefaultvalue.md) macro to specify another value for `key`.

For information about inserting plural nouns and units into localized strings, see [Localizing strings that contain plurals](../Xcode/localizing-strings-that-contain-plurals.md).

As of OS X 10.11 and iOS 9, [`Bundle`](./bundle.md) is thread-safe. As such, you can safely call [`NSLocalizedStringFromTable`](./nslocalizedstringfromtable.md) from any execution context.

> ❗ **Important**:  The values for `key`, `tableName`, and `comment` must be string literal values. Xcode can read these values from source code to automatically create localization tables when exporting localizations, but it doesn’t resolve string variables. If you want to use string variables, manually create a strings file and use [`localizedString(forKey:value:table:)`](./bundle/localizedstring%28forkey,value,table%29.md) instead. For more information on strings files, see [String Resources](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Strings/Strings.html#//apple_ref/doc/uid/10000051i-CH6).

> 💡 **Tip**:  Break up long string values into consecutive string literals.

```objc
NSLocalizedStringFromTable(
    @"Did you know that venus flytraps have flowers"
        @" atop very long stems?\nThe long stem keeps"
        @" insects a safe distance away from their"
        @" digestive leaves below.",
    @"Localized",
    @"An interesting fact about venus flytraps shown"
        @" on the loading screen.");
```

## Parameters

- `key`: The key for a string in the specified table.

  > **Note**:  Xcode can’t export localizations for strings whose `key` is a string variable, `nil`, or an empty string.
- `tbl`: The name of the table containing the key-value pairs. Also, the suffix for the strings file (a file with the `.strings` extension) to store the localized string. The default table in `Localizable.strings` is used when `tableName` is `nil` or an empty string.
- `comment`: The comment to place above the key-value pair in the strings file. This parameter provides the translator with some context about the localized string’s presentation to the user.

## See Also

### Related Documentation
- [Exporting localizations](../Xcode/exporting-localizations.md)
  Provide the localizable files from your project to localizers.
- [Importing localizations](../Xcode/importing-localizations.md)
  Import the files that you translate or adapt for a language and region into your project.
### Localization
- [class NSLocale](./nslocale.md)
  Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [class NSOrthography](./nsorthography.md)
  A description of the linguistic content of natural language text, typically used for spelling and grammar checking.
- [NSLocalizedString](./nslocalizedstring.md)
  Returns a localized version of a string from the default table, which Xcode autogenerates when exporting localizations.
- [NSLocalizedStringFromTableInBundle](./nslocalizedstringfromtableinbundle.md)
  Returns a localized version of a string from the table and bundle that you specify, which Xcode autogenerates when exporting localizations.
- [NSLocalizedStringWithDefaultValue](./nslocalizedstringwithdefaultvalue.md)
  Returns a localized version of a string identified by a key in the table that you specify, which Xcode autogenerates when exporting localizations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocalizedstringfromtable)*