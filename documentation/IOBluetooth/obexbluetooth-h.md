# OBEXBluetooth.h

**Framework**: IOBluetooth  
**Role**: API Collection

Object Exchange over Bluetooth.

## Overview

See the Overview section above for header-level documentation.

### Overview

#### Included Headers

- <IOBluetooth/OBEX.h>
- <IOBluetooth/IOBluetoothUserLib.h>

## Topics

### Miscellaneous
- [IOBluetoothOBEXSessionCreateWithIncomingIOBluetoothRFCOMMChannel](./iobluetoothobexsessioncreatewithincomingiobluetoothrfcommchannel.md)
  Create an OBEX session with an IOBluetoothRFCOMMchannel. This implies you are creating a OBEX SERVER session that will dole out info to remote Bluetooth clients.
- [IOBluetoothOBEXSessionCreateWithIOBluetoothDeviceRefAndChannelNumber](./iobluetoothobexsessioncreatewithiobluetoothdevicerefandchannelnumber.md)
  Create an OBEX session with a device ref and an RFCOMM channel ID. This allows you to bypass the browser if you already know the SDP information.
- [IOBluetoothOBEXSessionCreateWithIOBluetoothSDPServiceRecordRef](./iobluetoothobexsessioncreatewithiobluetoothsdpservicerecordref.md)
  Create an OBEX session with a service ref, usually obtained from the device browser.
- [IOBluetoothOBEXSessionOpenTransportConnection](./iobluetoothobexsessionopentransportconnection.md)

## See Also

### Reference
- [Bluetooth.h User-Space](./bluetooth-h-user-space.md)
  Bluetooth wireless technology
- [IOBluetoothUserLib.h](./iobluetoothuserlib-h.md)
  Public Interfaces for Apple’s implementation of Bluetooth technology.
- [IOBluetoothUtilities.h](./iobluetoothutilities-h.md)
  See the Overview section above for header-level documentation.
- [OBEX.h](./obex-h.md)
  Public OBEX technology interfaces.
- [OBEXFileTransferServices.h](./obexfiletransferservices-h.md)
- [IOBluetooth Structures](./iobluetooth-structures.md)
- [IOBluetooth Enumerations](./iobluetooth-enumerations.md)
- [IOBluetooth Constants](./iobluetooth-constants.md)
- [IOBluetooth Functions](./iobluetooth-functions.md)
- [IOBluetooth Data Types](./iobluetooth-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexbluetooth-h)*