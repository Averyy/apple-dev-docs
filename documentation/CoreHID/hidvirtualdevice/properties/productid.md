# productID

**Framework**: Core HID  
**Kind**: property

The product ID for the device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
let productID: UInt32?
```

#### Discussion

The product ID combines with [`vendorID`](hidvirtualdevice/properties/vendorid.md) to specify the exact product. Without knowing the vendor, product ID is useless. Look for vendor specific documentation for more details on the assigned product IDs for their products.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice/properties/productid)*