# runModal(for:keychain:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Displays a panel that allows users to change keychain settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func runModal(for settings: UnsafeMutablePointer<SecKeychainSettings>!, keychain: SecKeychain!) -> Int
```

```objc
- (NSInteger) runModalForSettings:(SecKeychainSettings *) settings keychain:(SecKeychainRef) keychain;
```

#### Discussion

The method result indicates which button the user clicks: [`NSOKButton`](../../AppKit/nsokbutton.md) or [`NSCancelButton`](../../AppKit/nscancelbutton.md) .

If the user attempts to chanage the settings of a locked keychain, the unlock authorization dialog appears.

## Parameters

- `settings`: A pointer to a keychain settngs structure. Because this structure is versioned, you must preallocate it and fill in the version of the structure.
- `keychain`: The keychain whose settings you wish to have the user change.

## See Also

### Displaying a sheet or panel
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, settings: UnsafeMutablePointer<SecKeychainSettings>!, keychain: SecKeychain!)](./beginsheet%28for,modaldelegate,didend,contextinfo,settings,keychain%29.md)
  Displays a sheet that allows users to change keychain settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsettingspanel/runmodal(for:keychain:))*