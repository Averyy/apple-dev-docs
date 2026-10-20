# IOBluetoothPasskeyDisplay

**Framework**: IOBluetooth UI  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS 10.2+

## Declaration

```swift
class IOBluetoothPasskeyDisplay
```

```objc
@interface IOBluetoothPasskeyDisplay : NSView
```

## Topics

### Instance Properties
- [var backgroundImageConstraint: NSLayoutConstraint!](./iobluetoothpasskeydisplay/backgroundimageconstraint.md)
- [var centeredView: NSView!](./iobluetoothpasskeydisplay/centeredview.md)
- [var isIncomingRequest: Bool](./iobluetoothpasskeydisplay/isincomingrequest-swift.property.md)
- [var passkey: String!](./iobluetoothpasskeydisplay/passkey-swift.property.md)
- [var returnHighlightImage: NSImage!](./iobluetoothpasskeydisplay/returnhighlightimage.md)
- [var returnImage: NSImage!](./iobluetoothpasskeydisplay/returnimage.md)
- [var usePasskeyNotificaitons: Bool](./iobluetoothpasskeydisplay/usepasskeynotificaitons.md)
### Instance Methods
- [func advancePasskeyIndicator()](./iobluetoothpasskeydisplay/advancepasskeyindicator%28%29.md)
- [func resetPasskeyIndicator()](./iobluetoothpasskeydisplay/resetpasskeyindicator%28%29.md)
- [func retreatPasskeyIndicator()](./iobluetoothpasskeydisplay/retreatpasskeyindicator%28%29.md)
- [func setPasskey(String!, for: IOBluetoothDevice!, usingSSP: Bool)](./iobluetoothpasskeydisplay/setpasskey%28_,for,usingssp%29.md)
### Type Methods
- [class func sharedDisplayView() -> IOBluetoothPasskeyDisplay!](./iobluetoothpasskeydisplay/shareddisplayview%28%29.md)

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class IOBluetoothAccessibilityIgnoredImageCell](./iobluetoothaccessibilityignoredimagecell.md)
- [class IOBluetoothAccessibilityIgnoredTextFieldCell](./iobluetoothaccessibilityignoredtextfieldcell.md)
- [class IOBluetoothDeviceSelectorController](./iobluetoothdeviceselectorcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothDeviceSelectorControllerRef](./iobluetoothdeviceselectorcontrollerref.md)
- [class IOBluetoothObjectPushUIController](./iobluetoothobjectpushuicontroller.md)
  An NSWindowController subclass that supports the creation of an IOBluetoothObjectPushUIController object.
- [class IOBluetoothPairingController](./iobluetoothpairingcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothPairingControllerRef](./iobluetoothpairingcontrollerref.md)
- [class IOBluetoothServiceBrowserController](./iobluetoothservicebrowsercontroller.md)
  A NSWindowController subclass to display a window to search for and perform SDP queries on bluetooth devices within range.
- [class IOBluetoothServiceBrowserControllerRef](./iobluetoothservicebrowsercontrollerref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay)*