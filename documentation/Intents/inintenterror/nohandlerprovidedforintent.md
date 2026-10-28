# noHandlerProvidedForIntent

**Framework**: Intents  
**Kind**: property  
**Role**: Type Property

No object was provided to handle the specified intent.

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
static var noHandlerProvidedForIntent: INIntentError.Code { get }
```

## Discussion

If your extension declares support for an intent in its `Info.plist` file, the [`handler(for:)`](../inintenthandlerproviding/handler%28for%29.md) method of its [`INExtension`](../inextension.md) object must provide a corresponding handler object.

## See Also

### Extension Errors
- [static var intentSupportedByMultipleExtension: INIntentError.Code](./intentsupportedbymultipleextension.md)
  An intent was supported by more than one Intents extension in the same app.
- [static var restrictedIntentsNotSupportedByExtension: INIntentError.Code](./restrictedintentsnotsupportedbyextension.md)
  An intent was listed in the `IntentsRestrictedWhileLocked` key of the app’s `Info.plist`, but not in the `IntentsSupported` key.
- [static var invalidIntentName: INIntentError.Code](./invalidintentname.md)
  The extension declared support for a nonexistent intent.
- [static var noAppAvailable: INIntentError.Code](./noappavailable.md)
- [static var extensionLaunchingTimeout: INIntentError.Code](./extensionlaunchingtimeout.md)
  The extension failed to launch in a timely manner.
- [static var extensionBringUpFailed: INIntentError.Code](./extensionbringupfailed.md)
  There was an error while trying to communicate with the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintenterror/nohandlerprovidedforintent)*