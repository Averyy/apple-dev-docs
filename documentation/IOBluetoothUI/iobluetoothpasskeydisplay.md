# IOBluetoothPasskeyDisplay

**Framework**: IOBluetooth UI  
**Kind**: class

**Availability**:
- macOS 10.2+

## Declaration

```swift
class IOBluetoothPasskeyDisplay
```

## Topics

### Instance Properties
- [var backgroundImageConstraint: NSLayoutConstraint!](iobluetoothpasskeydisplay/backgroundimageconstraint.md)
- [var centeredView: NSView!](iobluetoothpasskeydisplay/centeredview.md)
- [var isIncomingRequest: Bool](iobluetoothpasskeydisplay/isincomingrequest-swift.property.md)
- [var passkey: String!](iobluetoothpasskeydisplay/passkey-swift.property.md)
- [var returnHighlightImage: NSImage!](iobluetoothpasskeydisplay/returnhighlightimage.md)
- [var returnImage: NSImage!](iobluetoothpasskeydisplay/returnimage.md)
- [var usePasskeyNotificaitons: Bool](iobluetoothpasskeydisplay/usepasskeynotificaitons.md)
### Instance Methods
- [func advancePasskeyIndicator()](iobluetoothpasskeydisplay/advancepasskeyindicator.md)
- [func resetPasskeyIndicator()](iobluetoothpasskeydisplay/resetpasskeyindicator.md)
- [func retreatPasskeyIndicator()](iobluetoothpasskeydisplay/retreatpasskeyindicator.md)
- [func setPasskey(String!, for: IOBluetoothDevice!, usingSSP: Bool)](iobluetoothpasskeydisplay/setpasskey(_:for:usingssp:).md)
### Type Methods
- [class func sharedDisplayView() -> IOBluetoothPasskeyDisplay!](iobluetoothpasskeydisplay/shareddisplayview.md)

## Relationships

### Inherits From
- [NSView](../appkit/nsview.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class IOBluetoothAccessibilityIgnoredImageCell](iobluetoothaccessibilityignoredimagecell.md)
- [class IOBluetoothAccessibilityIgnoredTextFieldCell](iobluetoothaccessibilityignoredtextfieldcell.md)
- [class IOBluetoothDeviceSelectorController](iobluetoothdeviceselectorcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothDeviceSelectorControllerRef](iobluetoothdeviceselectorcontrollerref.md)
- [class IOBluetoothObjectPushUIController](iobluetoothobjectpushuicontroller.md)
  An NSWindowController subclass that supports the creation of an IOBluetoothObjectPushUIController object.
- [class IOBluetoothPairingController](iobluetoothpairingcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothPairingControllerRef](iobluetoothpairingcontrollerref.md)
- [class IOBluetoothServiceBrowserController](iobluetoothservicebrowsercontroller.md)
  A NSWindowController subclass to display a window to search for and perform SDP queries on bluetooth devices within range.
- [class IOBluetoothServiceBrowserControllerRef](iobluetoothservicebrowsercontrollerref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay)*