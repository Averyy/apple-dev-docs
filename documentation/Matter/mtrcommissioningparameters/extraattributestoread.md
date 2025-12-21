# extraAttributesToRead

**Framework**: Matter  
**Kind**: property

List of attribute paths to read from the commissionee (in addition to whatever attributes are already read to handle readEndpointInformation being YES, or to handle other commissioning tasks).

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
var extraAttributesToRead: [MTRAttributeRequestPath]? { get set }
```

#### Discussion

The FeatureMap attribute of all Network Commissioning clusters on the commissionee will always be read and does not need to be included in this list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningparameters/extraattributestoread)*