# establishmentReport()

**Framework**: Network  
**Kind**: method

Asynchronously request the establishment report for this connection. If called prior to the connection being in the .ready state, the report will be nil.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
final func establishmentReport() async throws -> NWConnection.EstablishmentReport?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/establishmentreport())*