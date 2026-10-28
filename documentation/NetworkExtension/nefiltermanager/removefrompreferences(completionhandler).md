# removeFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Remove the filter configuration from the Network Extension preferences.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func removeFromPreferences(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func removeFromPreferences() async throws
```

```objc
- (void) removeFromPreferencesWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

After the configuration is removed from the preferences the `NEFilterManager` object will still contain the configuration parameters. Calling `loadFromPreferencesWithCompletionHandler:` will clear out the configuration parameters from the `NEFilterManager` object.

## Parameters

- `completionHandler`: A block that takes an [`NSError`](../../Foundation/nserror.md) object. This block will be executed on the caller’s main thread after the removal operation is complete. If the configuration does not exist in the Network Extension preferences or an error occurs while removing it, the error parameter will be set to an `NSError` object containing details about the error. See `NEFilterManagerError` for a list of possible errors. If the configuration is removed successfully the error parameter will be set to nil.

## See Also

### Managing the filter configuration
- [class func shared() -> NEFilterManager](./shared%28%29.md)
  Access the single instance of `NEFilterManager`.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Load the filter configuration from the Network Extension preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](./savetopreferences%28completionhandler%29.md)
  Save the filter configuration in the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/removefrompreferences(completionhandler:))*