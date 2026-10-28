# saveToPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Save your DNS settings configuration to the system networking preferences.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func saveToPreferences(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func saveToPreferences() async throws
```

```objc
- (void) saveToPreferencesWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

You must call [`loadFromPreferences(completionHandler:)`](./loadfrompreferences%28completionhandler%29.md) at least once before calling this method the first time after your app launches.

## Parameters

- `completionHandler`: An optional block that takes an [`NSError`](../../Foundation/nserror.md) object. If specified, this block runs on your application’s main thread after the save operation completes. If an error occurs while saving the configuration, the block returns an `NSError` object.

## See Also

### Managing DNS configurations
- [class func shared() -> NEDNSSettingsManager](./shared%28%29.md)
  Access the single instance of a DNS settings manager.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Load your DNS settings configuration from the system networking preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](./removefrompreferences%28completionhandler%29.md)
  Remove your DNS settings configuration from the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanager/savetopreferences(completionhandler:))*