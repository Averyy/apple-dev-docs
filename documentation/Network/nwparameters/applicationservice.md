# applicationService

**Framework**: Network  
**Kind**: property

The default parameters for connecting with other, local devices that are running your app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
final class var applicationService: NWParameters { get }
```

#### Discussion

The default parameters set up an encrypted connection with another device on the local network. You can use these parameters as-is, or you can add a [`NWProtocolFramer`](nwprotocolframer.md) to provide application-level messaging support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/applicationservice)*