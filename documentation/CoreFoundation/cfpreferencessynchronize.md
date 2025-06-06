# CFPreferencesSynchronize(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

For the specified domain, writes all pending changes to preference data to permanent storage, and reads latest preference data from permanent storage.

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
func CFPreferencesSynchronize(_ applicationID: CFString, _ userName: CFString, _ hostName: CFString) -> Bool
```

#### Return Value

`true` if synchronization was successful, `false` if an error occurred.

#### Discussion

This function is the primitive synchronize mechanism for the higher level preference function [`CFPreferencesAppSynchronize(_:)`](cfpreferencesappsynchronize(_:).md); it writes updated preferences to permanent storage, and reads the latest preferences from permanent storage. Only the exact domain specified is modified. Note that to modify “Any User” preferences requires root privileges (or Admin privileges prior to OS X v10.6)—see [`Authorization Services Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000995).

Do not use this function directly unless you have a specific need. All arguments must be non- `NULL`. Do not use arbitrary user and host names, instead pass the pre-defined constants.

## Parameters

- `applicationID`: The ID of the application whose preferences you wish to modify. Takes the form of a Java package name,  .
- `userName`:   to modify the current user’s preferences, otherwise   to modify the preferences of all users.
- `hostName`:   to search the current-host domain, otherwise   to search the any-host domain.

## See Also

- [func CFPreferencesAppSynchronize(CFString) -> Bool](cfpreferencesappsynchronize(_:).md)
  Writes to permanent storage all pending changes to the preference data for the application, and reads the latest preference data from permanent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencessynchronize(_:_:_:))*