# headingAvailable

**Framework**: Core Location  
**Kind**: property

A Boolean value indicating whether the location manager is able to generate heading-related events.

**Availability**:
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var headingAvailable: Bool { get }
```

#### Discussion

Heading data may not be available on all iOS-based devices. You should check the value of this property before asking the location manager to deliver heading-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/headingavailable-swift.property)*