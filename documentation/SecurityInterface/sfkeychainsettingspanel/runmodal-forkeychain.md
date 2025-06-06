# runModal(for:keychain:)

**Framework**: Security Interface  
**Kind**: method

Displays a panel that allows users to change keychain settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func runModal(for settings: UnsafeMutablePointer<SecKeychainSettings>!, keychain: SecKeychain!) -> Int
```

#### Discussion

The method result indicates which button the user clicks: [`NSOKButton`](https://developer.apple.com/documentation/AppKit/NSOKButton) or [`NSCancelButton`](https://developer.apple.com/documentation/AppKit/NSCancelButton) .

If the user attempts to chanage the settings of a locked keychain, the unlock authorization dialog appears.

## Parameters

- `settings`: A pointer to a keychain settngs structure. Because this structure is versioned, you must preallocate it and fill in the version of the structure.
- `keychain`: The keychain whose settings you wish to have the user change.

## See Also

- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, settings: UnsafeMutablePointer<SecKeychainSettings>!, keychain: SecKeychain!)](sfkeychainsettingspanel/beginsheet(for:modaldelegate:didend:contextinfo:settings:keychain:).md)
  Displays a sheet that allows users to change keychain settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsettingspanel/runmodal(for:keychain:))*