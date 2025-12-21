# com.apple.developer.wifi-infrastructure

**Framework**: Bundle Resources  
**Kind**: typealias

The entitlement the system requires for an app to use the Wi-Fi Infrastructure framework.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

#### Discussion

This entitlement works with the Wi-Fi Infrastructure framework, which enables your app and accessory to share Wi-Fi networks from the host device.

To use Wi-Fi Infrastructure, add this entitlement to your app by enabling the Wi-Fi Infrastructure capability on your target in Xcode. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

##### Transport Security

To use Wi-Fi network sharing, an accessory must be paired and use Bluetooth Secure Connections, as defined in Bluetooth 4.2 from 2014. This involves a Bluetooth connection using:

- Secure Simple Pairing
- Encryption of all data with AES-128

For information on Bluetooth security modes, see [`NIST Special Publication 800-121: Guide to Bluetooth Security`](https://developer.apple.comhttps://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-121r2-upd1.pdf).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.wifi-infrastructure)*