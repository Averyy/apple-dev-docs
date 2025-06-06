# productID

**Framework**: Core HID  
**Kind**: property

The product ID for the device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var productID: UInt32?
```

#### Discussion

The product ID combines with the [`vendorID`](hiddevicemanager/devicematchingcriteria/vendorid.md) to specify the exact product. Without knowing the vendor, the product ID is meaningless. Look for vendor specific documentation for more details on the assigned product IDs for a vendor’s products.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager/devicematchingcriteria/productid)*