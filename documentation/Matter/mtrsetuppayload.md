# MTRSetupPayload

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRSetupPayload
```

## Mentions

- [Onboarding a Matter device](onboarding-a-matter-device.md)

## Topics

### Initializers
- [init(onboardingPayload: String) throws](mtrsetuppayload/init(onboardingpayload:).md)
- [init?(payload: String)](mtrsetuppayload/init(payload:).md)
- [init(setupPasscode: NSNumber, discriminator: NSNumber)](mtrsetuppayload/init(setuppasscode:discriminator:).md)
### Instance Properties
- [var commissioningFlow: MTRCommissioningFlow](mtrsetuppayload/commissioningflow.md)
- [var discoveryCapabilities: MTRDiscoveryCapabilities](mtrsetuppayload/discoverycapabilities.md)
- [var discriminator: NSNumber](mtrsetuppayload/discriminator.md)
- [var hasShortDiscriminator: Bool](mtrsetuppayload/hasshortdiscriminator.md)
- [var productID: NSNumber](mtrsetuppayload/productid.md)
- [var rendezvousInformation: NSNumber?](mtrsetuppayload/rendezvousinformation.md)
- [var serialNumber: String?](mtrsetuppayload/serialnumber.md)
- [var setUpPINCode: NSNumber](mtrsetuppayload/setuppincode.md)
- [var setupPasscode: NSNumber](mtrsetuppayload/setuppasscode.md)
- [var vendorElements: [MTROptionalQRCodeInfo]](mtrsetuppayload/vendorelements.md)
- [var vendorID: NSNumber](mtrsetuppayload/vendorid.md)
- [var version: NSNumber](mtrsetuppayload/version.md)
### Instance Methods
- [func addOrReplaceVendorElement(MTROptionalQRCodeInfo)](mtrsetuppayload/addorreplacevendorelement(_:).md)
- [func getAllOptionalVendorData() throws -> [MTROptionalQRCodeInfo]](mtrsetuppayload/getalloptionalvendordata.md)
- [func manualEntryCode() -> String?](mtrsetuppayload/manualentrycode.md)
- [func qrCodeString() -> String?](mtrsetuppayload/qrcodestring.md)
- [func qrCodeString(NSErrorPointer) -> String?](mtrsetuppayload/qrcodestring(_:).md)
- [func removeVendorElement(withTag: NSNumber)](mtrsetuppayload/removevendorelement(withtag:).md)
- [func vendorElement(withTag: NSNumber) -> MTROptionalQRCodeInfo?](mtrsetuppayload/vendorelement(withtag:).md)
### Type Methods
- [class func generateRandomPIN() -> Int](mtrsetuppayload/generaterandompin.md)
- [class func generateRandomSetupPasscode() -> NSNumber](mtrsetuppayload/generaterandomsetuppasscode.md)
- [class func new() -> Self](mtrsetuppayload/new.md)
- [class func isValidSetupPasscode(NSNumber) -> Bool](mtrsetuppayload/isvalidsetuppasscode(_:).md)
  Check whether the provided setup passcode (represented as an unsigned integer) is a valid setup passcode.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrsetuppayload)*