# AirPrint.AirPrintItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary of AirPrint printer details.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.10+
- visionOS 2.0+

## Declaration

```swift
object AirPrint.AirPrintItem
```

## Properties

- `ForceTLS` (boolean): If `true`, Transport Layer Security (TLS) secures AirPrint connections. Available only in iOS 11 and later. Available: iOS 11+ | iPadOS 11+ | visionOS 2+
- `IPAddress` (string) *(required)*: The IP address or hostname of the AirPrint destination.
- `Port` (integer): The listening port of the AirPrint destination. Available only in iOS 11 and later. Available: iOS 11+ | iPadOS 11+ | visionOS 2+
- `ResourcePath` (string) *(required)*: The resource path associated with the printer. This path corresponds to the `rp` parameter of the `_ipps.tcp` Bonjour record. For example: - `printers/Canon_MG5300_series`
- `printers/Xerox_Phaser_7600`
- `ipp/print`
- `Epson_IPP_Printer`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/airprint/airprintitem)*