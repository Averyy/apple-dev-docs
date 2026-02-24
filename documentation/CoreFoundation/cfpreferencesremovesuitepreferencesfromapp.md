# CFPreferencesRemoveSuitePreferencesFromApp(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Removes suite preferences from an application’s search chain.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFPreferencesRemoveSuitePreferencesFromApp(_ applicationID: CFString, _ suiteID: CFString)
```

## Parameters

- `applicationID`: The ID of the application from which to remove suite preferences, typically [`kCFPreferencesCurrentApplication`](kcfpreferencescurrentapplication.md). Do not pass `NULL` or [`kCFPreferencesAnyApplication`](kcfpreferencesanyapplication.md). Takes the form of a Java package name, `com.foosoft`.
- `suiteID`: The ID of the application suite preferences to remove. Takes the form of a Java package name, `com.foosoft`.

## See Also

- [func CFPreferencesAddSuitePreferencesToApp(CFString, CFString)](cfpreferencesaddsuitepreferencestoapp(_:_:).md)
  Adds suite preferences to an application’s preference search chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencesremovesuitepreferencesfromapp(_:_:))*