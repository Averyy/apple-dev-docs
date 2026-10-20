# vendorID

**Framework**: Matter  
**Kind**: property  
**Role**: Instance Property

The Vendor Identifier associated with the device.

**Availability**:
- iOS 18.3+
- iPadOS 18.3+
- Mac Catalyst 18.3+
- macOS 15.3+
- tvOS 18.3+
- visionOS 2.3+
- watchOS 11.3+

## Declaration

```swift
@NSCopying
var vendorID: NSNumber? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * vendorID;
```

#### Discussion

A non-nil value if the vendor identifier has been determined from the device, nil if unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/vendorid)*