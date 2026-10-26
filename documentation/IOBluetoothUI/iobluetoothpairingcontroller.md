# IOBluetoothPairingController

**Framework**: IOBluetooth UI  
**Kind**: class  
**Role**: Class

A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.

**Availability**:
- macOS 10.2+

## Declaration

```swift
class IOBluetoothPairingController
```

```objc
@interface IOBluetoothPairingController : NSWindowController
```

#### Overview

Implementation of a window controller to handle pairing with a bluetooth device. This class will handle connecting to the Bluetooth Daemon for the purposes of searches, and displaying the results. When necessary this class will display a sheet asking the user for a PIN code. This window will not return anything to the caller if it is canceled or if pairing occurs.

## Topics

### Instance Methods
- [func addAllowedUUID(IOBluetoothSDPUUID!)](./iobluetoothpairingcontroller/addalloweduuid%28_%29.md)
  Adds a UUID to the list of UUIDs that are used to validate the user’s selection.
- [func addAllowedUUIDArray([Any]!)](./iobluetoothpairingcontroller/addalloweduuidarray%28_%29.md)
  Adds an array of UUIDs to the list of UUIDs that are used to validate the user’s selection.
- [func clearAllowedUUIDs()](./iobluetoothpairingcontroller/clearalloweduuids%28%29.md)
  Resets the controller back to the default state where it will accept any device the user selects.
- [func getDescriptionText() -> String!](./iobluetoothpairingcontroller/getdescriptiontext%28%29.md)
  Returns the description text that appears in the device selector panel.
- [func getOptions() -> IOBluetoothServiceBrowserControllerOptions](./iobluetoothpairingcontroller/getoptions%28%29.md)
  Returns the option bits that control the panel’s behavior.
- [func getPrompt() -> String!](./iobluetoothpairingcontroller/getprompt%28%29.md)
  Returns the title of the default/select button in the device selector panel.
- [func getResults() -> [Any]!](./iobluetoothpairingcontroller/getresults%28%29.md)
  Returns an NSArray of the devices that were paired.
- [func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>!](./iobluetoothpairingcontroller/getsearchattributes%28%29.md)
  Returns the search attributes that control the panel’s search/inquiry behavior.
- [func getTitle() -> String!](./iobluetoothpairingcontroller/gettitle%28%29.md)
  Returns the title of the device selector panel.
- [func runModal() -> Int32](./iobluetoothpairingcontroller/runmodal%28%29.md)
  Runs the pairing panel in a modal session to allow the user to select a Bluetooth device.
- [func setDescriptionText(String!)](./iobluetoothpairingcontroller/setdescriptiontext%28_%29.md)
  Sets the description text that appears in the device selector panel.
- [func setOptions(IOBluetoothServiceBrowserControllerOptions)](./iobluetoothpairingcontroller/setoptions%28_%29.md)
  Sets the option bits that control the panel’s behavior.
- [func setPrompt(String!)](./iobluetoothpairingcontroller/setprompt%28_%29.md)
  Sets the title of the default/select button in the device selector panel.
- [func setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>!)](./iobluetoothpairingcontroller/setsearchattributes%28_%29.md)
  Sets the search attributes that control the panel’s search/inquiry behavior.
- [func setTitle(String!)](./iobluetoothpairingcontroller/settitle%28_%29.md)
  Sets the title of the panel when not run as a sheet.
### Type Methods
- [+ pairingController](./iobluetoothpairingcontroller/pairingcontroller.md)

## Relationships

### Inherits From
- [NSWindowController](../AppKit/nswindowcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
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
- [class IOBluetoothPairingControllerRef](./iobluetoothpairingcontrollerref.md)
- [class IOBluetoothPasskeyDisplay](./iobluetoothpasskeydisplay.md)
- [class IOBluetoothServiceBrowserController](./iobluetoothservicebrowsercontroller.md)
  A NSWindowController subclass to display a window to search for and perform SDP queries on bluetooth devices within range.
- [class IOBluetoothServiceBrowserControllerRef](./iobluetoothservicebrowsercontrollerref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpairingcontroller)*