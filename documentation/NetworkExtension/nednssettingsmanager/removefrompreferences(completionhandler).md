# removeFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Remove your DNS settings configuration from the system networking preferences.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
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

After you remove your configuration, the `NEDNSSettingsManager` object still contains the configuration parameters. Calling [`loadFromPreferences(completionHandler:)`](./loadfrompreferences%28completionhandler%29.md) clears out the configuration parameters from the `NEDNSSettingsManager` object.

## Parameters

- `completionHandler`: An optional block that takes an [`NSError`](../../Foundation/nserror.md) object. If specified, this block runs on your application’s main thread after your configuration is removed. If an error occurs while removing the configuration, the block returns an `NSError` object.

## See Also

### Managing DNS configurations
- [class func shared() -> NEDNSSettingsManager](./shared%28%29.md)
  Access the single instance of a DNS settings manager.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Load your DNS settings configuration from the system networking preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](./savetopreferences%28completionhandler%29.md)
  Save your DNS settings configuration to the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanager/removefrompreferences(completionhandler:))*