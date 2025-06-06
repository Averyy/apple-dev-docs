# Discovering HID devices from Terminal

**Framework**: Core HID

Identify devices connected to your Mac from the command line.

#### Overview

To interact with a human interface device (HID), you must identify what devices are available on your system. The `hidutil` command is a human interface device utility that you can use to probe a Mac for HID devices, monitor HID events, and to obtain device reports. Run `hidutil list` in Terminal (`/Applications/Utilities`) to receive a list of HID devices. The `Devices` portion of the output is relevant for discovering available human interface devices.

```shell
Devices:
VendorID ProductID LocationID UsagePage Usage RegistryID  Transport Class                      Product                            UserClass Built-In 
0x0      0x0       0x31       65280     11    0x100000b78 FIFO      AppleHIDTransportHIDDevice Apple Internal Keyboard / Trackpad (null)    1        
0x4c     0x269     0x74d7f698 65280     3     0x10000131f Bluetooth AppleHSBluetoothHIDDriver  Magic Mouse                        (null)    0        
0x4c     0x269     0x74d7f698 65280     11    0x10000130f Bluetooth AppleHSBluetoothHIDDriver  Magic Mouse                        (null)    0        
0x0      0x0       0x0        65280     255   0x100000636 SPU       AppleSPUHIDDevice          (null)                             (null)    1        
0x0      0x0       0x31       65280     3     0x100000b66 FIFO      AppleHIDTransportHIDDevice Apple Internal Keyboard / Trackpad (null)    1        
0x5ac    0x8104    0x0        65280     3     0x100000637 SPU       AppleSPUHIDDevice          (null)                             (null)    1        
0x0      0x0       0x5        65280     4     0x10000063d SPU       AppleSPUHIDDevice          (null)                             (null)    1        
0x0      0x0       0x0        65280     72    0x100000a4c SPMI      AppleBTM                   BTM                                (null)    0        
0x0      0x0       0x31       1         2     0x100000b88 FIFO      AppleHIDTransportHIDDevice Apple Internal Keyboard / Trackpad (null)    1        
0x4c     0x26c     0x1115ab62 65280     11    0x10000136b Bluetooth AppleHSBluetoothHIDDriver  Magic Keyboard with Numeric Keypad (null)    0        
0x4c     0x269     0x74d7f698 1         2     0x100001319 Bluetooth AppleHSBluetoothHIDDriver  Magic Mouse                        (null)    0        
0x0      0x0       0x31       65280     13    0x100000b6b FIFO      AppleHIDTransportHIDDevice Apple Internal Keyboard / Trackpad (null)    1        
0x5ac    0x8104    0x0        65280     9     0x100000638 SPU       AppleSPUHIDDevice          (null)                             (null)    1        
0x0      0x0       0x31       1         6     0x100000b64 FIFO      AppleHIDTransportHIDDevice Apple Internal Keyboard / Trackpad (null)    1        
0x5ac    0x0       0x0        65280     15    0x100000c5c USB       IOHIDResource              Keyboard Backlight                 (null)    1        
0x4c     0x26c     0x1115ab62 1         6     0x100001373 Bluetooth AppleHSBluetoothHIDDriver  Magic Keyboard with Numeric Keypad (null)    0        
0x5ac    0x8104    0x0        65280     5     0x10000063a SPU       AppleSPUHIDDevice          (null)                             (null)    1        
```

There are multiple entries with similar product names. Some products register as multiple devices to segment functionality that you match and interact with individually. For example, a device may have a keyboard and trackpad in the same form factor, but declare them as two separate components.

The `UsagePage` column contains the usage page, which is a category of broad functionality. In the above output, the usage page is either `1` or `65280`. According to [`HID Usage Tables for Universal Serial Bus (USB)`](https://developer.apple.comhttps://usb.org/sites/default/files/hut1_5.pdf), `65280 (0xFF00)` is a vendor-defined page and is reserved for the vendor to use as they see fit; therefore, ignore any entries with this page. Usage page `1` is the Generic Desktop page. Because both a keyboard and a mouse are Generic Desktop devices, you must further refine the search by examining the usage value.

Values in the `Usage` column relate to a category of specific functionality. In the output above, items with a usage page of `1` have a usage value of `2` or `6`, defined as a mouse or keyboard, respectively, according to [`HID Usage Tables for Universal Serial Bus (USB)`](https://developer.apple.comhttps://usb.org/sites/default/files/hut1_5.pdf).

## See Also

- [actor HIDDeviceManager](hiddevicemanager.md)
  A helper for discovering human interface devices (HID) connected to the system.
- [HIDDeviceManager.DeviceMatchingCriteria](hiddevicemanager/devicematchingcriteria.md)
  Matching criteria used to filter HID devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/discoveringhiddevicesfromterminal)*