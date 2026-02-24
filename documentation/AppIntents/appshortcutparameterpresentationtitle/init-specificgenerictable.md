# init(specific:generic:table:)

**Framework**: App Intents  
**Kind**: init

Initializes an `AppShortcutParameterPresentationTitle` with the specified parameters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
init(specific: AppShortcutParameterPresentationTitleString<Intent, Value, Parameter, ParameterKeyPath>, generic: StaticString, table: StaticString? = nil)
```

## Parameters

- `specific`: An `AppShortcutParameterPresentationTitleString` representing the specific title of the `AppShortcutParameterPresentation`. Example: `"Call \(\.$person)"`.
- `generic`: A `StaticString` representing the generic title of the `AppShortcutParameterPresentation`. Example: `"Call Person..."`.
- `table`: An optional `StaticString` representing the table to use when localizing the title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutparameterpresentationtitle/init(specific:generic:table:))*