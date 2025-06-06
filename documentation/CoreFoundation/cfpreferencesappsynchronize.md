# CFPreferencesAppSynchronize(_:)

**Framework**: Core Foundation  
**Kind**: func

Writes to permanent storage all pending changes to the preference data for the application, and reads the latest preference data from permanent storage.

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
func CFPreferencesAppSynchronize(_ applicationID: CFString) -> Bool
```

#### Return Value

`true` if synchronization was successful, otherwise `false`.

#### Discussion

Calling the function [`CFPreferencesSetAppValue(_:_:_:)`](cfpreferencessetappvalue(_:_:_:).md) is not in itself sufficient for storing preferences. The [`CFPreferencesAppSynchronize(_:)`](cfpreferencesappsynchronize(_:).md) function writes to permanent storage all pending preference changes for the application. Typically you would call this function after multiple calls to [`CFPreferencesSetAppValue(_:_:_:)`](cfpreferencessetappvalue(_:_:_:).md). Conversely, preference data is cached after it is first read. Changes made externally are not automatically incorporated. The [`CFPreferencesAppSynchronize(_:)`](cfpreferencesappsynchronize(_:).md) function reads the latest preferences from permanent storage.

## Parameters

- `applicationID`: The ID of the application whose preferences to write to storage, typically  . Do not pass   or  . Takes the form of a Java package name,  .

## See Also

- [func CFPreferencesSynchronize(CFString, CFString, CFString) -> Bool](cfpreferencessynchronize(_:_:_:).md)
  For the specified domain, writes all pending changes to preference data to permanent storage, and reads latest preference data from permanent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencesappsynchronize(_:))*