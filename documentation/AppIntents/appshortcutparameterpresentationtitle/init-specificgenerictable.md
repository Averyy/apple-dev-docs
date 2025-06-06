# init(specific:generic:table:)

**Framework**: App Intents  
**Kind**: init

Initializes an `AppShortcutParameterPresentationTitle` with the specified parameters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+
- Unknown ?+ - Deprecated
- visionOS 1.0+

## Declaration

```swift
init(specific: AppShortcutParameterPresentationTitleString<Intent, Value, Parameter, ParameterKeyPath>, generic: StaticString, table: StaticString? = nil)
```

## Parameters

- `specific`: An   representing the specific title of the  .   Example:  .
- `generic`: A   representing the generic title of the  . Example:  .
- `table`: An optional   representing the table to use when localizing the title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutparameterpresentationtitle/init(specific:generic:table:))*