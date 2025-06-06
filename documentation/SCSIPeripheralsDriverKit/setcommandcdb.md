# SetCommandCDB

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: func

Fills a 16-byte Command Descriptor Block (CDB) with custom content.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
void SetCommandCDB(SCSICommandDescriptorBlock * cdb, UInt8 byte0, UInt8 byte1, UInt8 byte2, UInt8 byte3, UInt8 byte4, UInt8 byte5, UInt8 byte6, UInt8 byte7, UInt8 byte8, UInt8 byte9, UInt8 byte10, UInt8 byte11, UInt8 byte12, UInt8 byte13, UInt8 byte14, UInt8 byte15);
```

## Parameters

- `cdb`: The 16-byte Command Descriptor Block.
- `byte0`: Byte 0 of the CDB.
- `byte1`: Byte 1 of the CDB.
- `byte2`: Byte 2 of the CDB.
- `byte3`: Byte 3 of the CDB.
- `byte4`: Byte 4 of the CDB.
- `byte5`: Byte 5 of the CDB.
- `byte6`: Byte 6 of the CDB.
- `byte7`: Byte 7 of the CDB.
- `byte8`: Byte 8 of the CDB.
- `byte9`: Byte 9 of the CDB.
- `byte10`: Byte 10 of the CDB.
- `byte11`: Byte 11 of the CDB.
- `byte12`: Byte 12 of the CDB.
- `byte13`: Byte 13 of the CDB.
- `byte14`: Byte 14 of the CDB.
- `byte15`: Byte 15 of the CDB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/setcommandcdb)*