# linkQuality

**Framework**: Network  
**Kind**: property

Represents the link quality measurement of the link layer network attachment

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var linkQuality: NWPath.LinkQuality { get }
```

#### Discussion

Use this value to tune initial values for algorithms that can scale with the capabilities of the network. Do not use this value to gate connection attempts or to override adjustments that would be made based on actual network performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpath/linkquality-swift.property)*