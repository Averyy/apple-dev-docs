# CFPreferencesAddSuitePreferencesToApp(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Adds suite preferences to an application’s preference search chain.

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
func CFPreferencesAddSuitePreferencesToApp(_ applicationID: CFString, _ suiteID: CFString)
```

#### Discussion

Suite preferences allow you to maintain a set of preferences that are common to all applications in the suite. When a suite is added to an application’s search chain, all of the domains pertaining to that suite are inserted into the chain. Suite preferences are added between the “Current Application” domains and the “Any Application” domains. If you add multiple suite preferences to one application, the order of the suites in the search chain is non-deterministic. You can override a suite preference for a given application by defining the same preference key in the application specific preferences.

## Parameters

- `applicationID`: The ID of the application to which to add suite preferences, typically  . Do not pass   or  . Takes the form of a Java package name,  .
- `suiteID`: The ID of the application suite preferences to add. Takes the form of a Java package name,  .

## See Also

- [func CFPreferencesRemoveSuitePreferencesFromApp(CFString, CFString)](cfpreferencesremovesuitepreferencesfromapp(_:_:).md)
  Removes suite preferences from an application’s search chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencesaddsuitepreferencestoapp(_:_:))*