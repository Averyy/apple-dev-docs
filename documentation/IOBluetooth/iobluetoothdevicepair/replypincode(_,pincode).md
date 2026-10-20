# replyPINCode(_:pinCode:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

This is the required reply to the devicePairingPINCodeRequest delegate message. Set the PIN code to use during pairing if required.

**Availability**:
- macOS

## Declaration

```swift
func replyPINCode(_ PINCodeSize: Int, pinCode PINCode: UnsafeMutablePointer<BluetoothPINCode>!)
```

```objc
- (void) replyPINCode:(ByteCount) PINCodeSize PINCode:(BluetoothPINCode *) PINCode;
```

## Parameters

- `PINCodeSize`: The PIN code length in octets (8 bits).
- `PINCode`: PIN code for the device. Can be up to a maximum of 128 bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepair/replypincode(_:pincode:))*