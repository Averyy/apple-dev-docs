# UISupportedExternalAccessoryProtocols

**Framework**: Bundle Resources  
**Kind**: typealias

The protocols that the app uses to communicate with external accessory hardware.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+

#### Discussion

Add this key to your app’s `Info.plist` file, and set the value to the names of the hardware protocols your app supports. You format protocol names as reverse-DNS strings. For example, the string “`com.apple.myProtocol`” might represent a custom protocol that Apple defines. Manufacturers can define custom protocols for their accessories or work with other manufacturers and organizations to define standard protocols for different accessory types.

## See Also

- [UIApplicationSupportsPrintCommand](information-property-list/uiapplicationsupportsprintcommand.md)
  A Boolean value that indicates whether the app supports the Command-P keyboard shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uisupportedexternalaccessoryprotocols)*