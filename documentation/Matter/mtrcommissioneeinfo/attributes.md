# attributes

**Framework**: Matter  
**Kind**: property

Attributes that were read from the commissionee.  This will contain the following, if they are available:

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

## Declaration

```swift
var attributes: [MTRAttributePath : [String : Any]]? { get }
```

#### Discussion

1. The attributes in extraAttributesToRead on MTRCommissioningParameters.
2. The FeatureMap attributes of all Network Commissioning clusters on the commissionee.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioneeinfo/attributes)*