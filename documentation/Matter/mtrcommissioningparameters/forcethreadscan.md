# forceThreadScan

**Framework**: Matter  
**Kind**: property

Whether to force a network scan before requesting Thread credentials. The default is NO.

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
var forceThreadScan: Bool { get set }
```

#### Discussion

Even if this value is NO a scan may still be performed.

This value will be ignored if a Thread operational dataset is provided or not needed.

NOTE: Not all APIs that take MTRCommissioningParameters pay attention to this flag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningparameters/forcethreadscan)*