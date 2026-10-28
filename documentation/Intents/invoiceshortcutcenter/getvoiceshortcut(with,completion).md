# getVoiceShortcut(with:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Retrieves a shortcut the user added to Siri.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func getVoiceShortcut(with identifier: UUID, completion completionHandler: @escaping @Sendable (INVoiceShortcut?, (any Error)?) -> Void)
```

```swift
func getVoiceShortcut(with identifier: UUID) async throws -> INVoiceShortcut
```

```objc
- (void) getVoiceShortcutWithIdentifier:(NSUUID *) identifier completion:(void (^)(INVoiceShortcut *voiceShortcut, NSError *error)) completionHandler;
```

## Discussion

This method only retrieves shortcuts associated with the app that calls the method. It cannot retrieve shortcuts associated with other apps.

## Parameters

- `identifier`: The shortcut identifier.
- `completionHandler`: The block invoked on a background thread after the system retrieves the shortcut. This block has no return value and takes the following parameters:

  - **`voiceShortcut`**: An instance of [`INVoiceShortcut`](../invoiceshortcut.md) representing the requested shortcut; otherwise, `nil` if the shortcut doesn’t exist or an error occurs.
  - **`error`**: An [`NSError`](../../Foundation/nserror.md) object if a problem occurred retrieving the shortcut; otherwise, `nil`.

## See Also

### Getting Shortcuts Added to Siri
- [func getAllVoiceShortcuts(completion: ([INVoiceShortcut]?, (any Error)?) -> Void)](./getallvoiceshortcuts%28completion%29.md)
  Retrieves all shortcuts added to Siri for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invoiceshortcutcenter/getvoiceshortcut(with:completion:))*