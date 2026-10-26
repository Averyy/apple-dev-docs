# getAllVoiceShortcuts(completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Retrieves all shortcuts added to Siri for your app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func getAllVoiceShortcuts(completion completionHandler: @escaping @Sendable ([INVoiceShortcut]?, (any Error)?) -> Void)
```

```swift
func allVoiceShortcuts() async throws -> [INVoiceShortcut]
```

```objc
- (void) getAllVoiceShortcutsWithCompletion:(void (^)(NSArray<INVoiceShortcut *> *voiceShortcuts, NSError *error)) completionHandler;
```

#### Discussion

Let users know when an action they perform in your app has an associated shortcut. For example, a user has created a shortcut in the soup-ordering app Soup Chef that allows them to place an order for tomato soup by speaking the phrase “Soup time.” The app shows the phrase in the user’s order history, reminding them that the shortcut exists and of the phrase to speak in order to invoke the shortcut in Siri.

![A screenshot of the order history screen in the Soup Chef app showing the invocation phrase for the shortcut.](https://developer.apple.com/tutorials/images/com.apple.sirikit/media-3027138@2x.png)

The app uses the [`getAllVoiceShortcuts(completion:)`](./getallvoiceshortcuts%28completion%29.md) method to retrieve the list of shortcuts associated to the app. The list contains shortcuts added to Siri with [`INUIAddVoiceShortcutViewController`](https://developer.apple.com/documentation/intentsui/inuiaddvoiceshortcutviewcontroller) and those added by the user in the Settings app.

The listing below retrieves shortcuts associated with the Soup Chef app.

```swift
public func updateVoiceShortcuts(completion: (() -> Void)?) {
    INVoiceShortcutCenter.shared.getAllVoiceShortcuts { (voiceShortcutsFromCenter, error) in
        if let voiceShortcutsFromCenter = voiceShortcutsFromCenter {
            self.voiceShortcuts = voiceShortcutsFromCenter
        } else {
            if let error = error as NSError? {
                os_log("Failed to fetch voice shortcuts with error: %@", log: OSLog.default, type: .error, error)
            }
        }

        if let completion = completion {
            completion()
        }
    }
}
```

## Parameters

- `completionHandler`: The block invoked on a background thread after the system retrieves the list of shortcuts. This block has no return value and takes the following parameters:

  - **voiceShortcuts**: An array of [`INVoiceShortcut`](../invoiceshortcut.md) objects. This parameter is `nil` when an error occurs.
  - **error**: An [`NSError`](../../Foundation/nserror.md) object if a problem occurred retrieving the shortcuts; otherwise, `nil`.

## See Also

### Related Documentation
- [Soup Chef: Accelerating App Interactions with Shortcuts](../../SiriKit/soup-chef-accelerating-app-interactions-with-shortcuts.md)
  Make it easy for people to use Siri with your app by providing shortcuts to your app’s actions.
### Getting Shortcuts Added to Siri
- [func getVoiceShortcut(with: UUID, completion: (INVoiceShortcut?, (any Error)?) -> Void)](./getvoiceshortcut%28with,completion%29.md)
  Retrieves a shortcut the user added to Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invoiceshortcutcenter/getallvoiceshortcuts(completion:))*