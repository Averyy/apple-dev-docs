# INIntentError.Code.invalidIntentName

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The extension declared support for a nonexistent intent. Check your extension’s `Info.plist` file to make sure all intent names are spelled correctly.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case invalidIntentName
```

```c
INIntentErrorInvalidIntentName
```

## See Also

### Extension Errors
- [INIntentError.Code.extensionLaunchingTimeout](./extensionlaunchingtimeout.md)
  The extension failed to launch in a timely manner.
- [INIntentError.Code.extensionBringUpFailed](./extensionbringupfailed.md)
  There was an error while trying to communicate with the extension.
- [INIntentError.Code.noAppAvailable](./noappavailable.md)
- [INIntentError.Code.intentSupportedByMultipleExtension](./intentsupportedbymultipleextension.md)
  An intent was supported by more than one Intents extension in the same app. An app may have multiple Intents extensions, but each one must support a unique set of intents.
- [INIntentError.Code.restrictedIntentsNotSupportedByExtension](./restrictedintentsnotsupportedbyextension.md)
  An intent was listed in the `IntentsRestrictedWhileLocked` key of the app’s `Info.plist`, but not in the `IntentsSupported` key. All intents in the `IntentsRestrictedWhileLocked` key must also be present in the `IntentsSupported` key.
- [INIntentError.Code.noHandlerProvidedForIntent](./nohandlerprovidedforintent.md)
  No object was provided to handle the specified intent. If your extension declares support for an intent in its `Info.plist` file, the [`handler(for:)`](../../inintenthandlerproviding/handler%28for%29.md) method of its [`INExtension`](../../inextension.md) object must provide a corresponding handler object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintenterror/code/invalidintentname)*