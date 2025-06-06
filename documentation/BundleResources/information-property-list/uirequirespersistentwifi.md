# UIRequiresPersistentWiFi

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app requires a Wi-Fi connection.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- visionOS 1.0+

#### Discussion

If `YES`, iOS opens a Wi-Fi connection when the app launches and keeps it open while the app is running. If `NO`, iOS closes the active Wi-Fi connection after 30 minutes. If the app tries to connect to the network when there’s no open Wi-Fi connection, the system may use the cellular network instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uirequirespersistentwifi)*