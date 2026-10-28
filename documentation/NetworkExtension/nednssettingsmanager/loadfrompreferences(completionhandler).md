# loadFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Load your DNS settings configuration from the system networking preferences.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func loadFromPreferences(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func loadFromPreferences() async throws
```

```objc
- (void) loadFromPreferencesWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

You must call this method at least once before calling [`saveToPreferences(completionHandler:)`](./savetopreferences%28completionhandler%29.md) for the first time after your app launches.

## Parameters

- `completionHandler`: A block that takes an [`NSError`](../../Foundation/nserror.md) object. This block runs on your application’s main thread after the load operation is complete. If an error occurs while loading the configuration, the block returns an `NSError` object.

## See Also

### Managing DNS configurations
- [class func shared() -> NEDNSSettingsManager](./shared%28%29.md)
  Access the single instance of a DNS settings manager.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](./savetopreferences%28completionhandler%29.md)
  Save your DNS settings configuration to the system networking preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](./removefrompreferences%28completionhandler%29.md)
  Remove your DNS settings configuration from the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanager/loadfrompreferences(completionhandler:))*