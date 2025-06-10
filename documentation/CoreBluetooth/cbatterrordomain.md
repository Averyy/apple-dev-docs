# CBATTErrorDomain

**Framework**: Core Bluetooth  
**Kind**: var

The domain for Core Bluetooth ATT errors.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let CBATTErrorDomain: String
```

#### Discussion

This value identifies Core Bluetooth Attribute Protocol (ATT) errors when used as the [`domain`](https://developer.apple.com/documentation/Foundation/NSError/domain) of an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) instance.

## See Also

- [struct CBError](cberror-swift.struct.md)
  An error that Core Bluetooth returns during Bluetooth transactions.
- [let CBErrorDomain: String](cberrordomain.md)
  The domain for Core Bluetooth errors.
- [CBError.Code](cberror-swift.struct/code.md)
  The codes for errors that Core Bluetooth returns during Bluetooth transactions.
- [struct CBATTError](cbatterror-swift.struct.md)
  An error that Core Bluetooth returns while using Attribute Protocol (ATT).
- [CBATTError.Code](cbatterror-swift.struct/code.md)
  The possible errors returned by a GATT server (a remote peripheral) during Bluetooth low energy ATT transactions.
- [struct CBATTError](cbatterror-swift.struct.md)
  An error that Core Bluetooth returns while using Attribute Protocol (ATT).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbatterrordomain)*