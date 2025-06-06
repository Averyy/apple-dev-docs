# removeFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Remove the filter configuration from the Network Extension preferences.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func removeFromPreferences() async throws
```

#### Discussion

After the configuration is removed from the preferences the `NEFilterManager` object will still contain the configuration parameters. Calling `loadFromPreferencesWithCompletionHandler:` will clear out the configuration parameters from the `NEFilterManager` object.

## Parameters

- `completionHandler`: A block that takes an   object. This block will be executed on the caller’s main thread after the removal operation is complete. If the configuration does not exist in the Network Extension preferences or an error occurs while removing it, the error parameter will be set to an   object containing details about the error. See   for a list of possible errors. If the configuration is removed successfully the error parameter will be set to nil.

## See Also

- [class func shared() -> NEFilterManager](nefiltermanager/shared.md)
  Access the single instance of `NEFilterManager`.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nefiltermanager/loadfrompreferences(completionhandler:).md)
  Load the filter configuration from the Network Extension preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](nefiltermanager/savetopreferences(completionhandler:).md)
  Save the filter configuration in the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/removefrompreferences(completionhandler:))*