# removeFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Remove your relay configuration from the system networking preferences.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
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

#### Discussion

After you remove your configuration, the [`NERelayManager`](../nerelaymanager.md) object still contains the configuration parameters. Calling [`loadFromPreferences(completionHandler:)`](./loadfrompreferences%28completionhandler%29.md) clears out the configuration parameters from the [`NERelayManager`](../nerelaymanager.md) object.

## Parameters

- `completionHandler`: An optional block that takes an [`NSError`](../../Foundation/nserror.md) object. If specified, this block runs on your application’s main thread after your configuration is removed. If an error occurs while removing the configuration, the block returns an `NSError` object.

## See Also

### Managing relay configurations
- [class func shared() -> NERelayManager](./shared%28%29.md)
  Access the single instance of a network relay manager.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Load your relay configuration from the system networking preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](./savetopreferences%28completionhandler%29.md)
  Save your relay configuration to the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanager/removefrompreferences(completionhandler:))*