# networkIdentifier

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

A unique identifier for a Downlink Time-Difference-of-Arrival network.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var networkIdentifier: Int { get set }
```

```objc
@property (nonatomic, assign) NSInteger networkIdentifier;
```

#### Discussion

Set this to the value of the session ID in the anchor’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoaconfiguration/networkidentifier)*