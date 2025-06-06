# beginSheet(for:modalDelegate:didEnd:contextInfo:settings:keychain:)

**Framework**: Security Interface  
**Kind**: method

Displays a sheet that allows users to change keychain settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func beginSheet(for docWindow: NSWindow!, modalDelegate delegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!, settings: UnsafeMutablePointer<SecKeychainSettings>!, keychain: SecKeychain!)
```

#### Discussion

The delegate method has the following signature:

```objc
- (void)createPanelDidEnd:(NSWindow *)sheet
        returnCode:(int)returnCode
        contextInfo:(void *)contextInfo
```

The parameters for the delegate method are:

The delegate method may dismiss the keychain settings sheet itself; if it does not, the sheet is dismissed on return from the `beginSheetForDirectory:...` method.

## Parameters

- `docWindow`: The parent window to which the sheet is attached. If this parameter is  , the behavior defaults to a standalone modal window.
- `delegate`: The delegate object in which the method specified in the   parameter is implemented.
- `didEndSelector`: A method selector for a delegate method called after the modal session has ended, but before the sheet has been dismissed. Implementation of this delegate method is optional.
- `contextInfo`: A pointer to data that is passed to the delegate method. You can use this data pointer for any purpose you wish.
- `settings`: A pointer to a keychain settings structure. Because this structure is versioned, you must preallocate it and fill in the version of the structure.
- `keychain`: The keychain whose settings you wish to have the user change.

## See Also

- [func runModal(for: UnsafeMutablePointer<SecKeychainSettings>!, keychain: SecKeychain!) -> Int](sfkeychainsettingspanel/runmodal(for:keychain:).md)
  Displays a panel that allows users to change keychain settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsettingspanel/beginsheet(for:modaldelegate:didend:contextinfo:settings:keychain:))*