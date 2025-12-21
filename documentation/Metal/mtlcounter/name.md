# name

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The name of a GPU’s counter instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var name: String { get }
```

#### Discussion

The property typically matches one of the common counter names that [`MTLCommonCounter`](mtlcommoncounter.md) defines (see [`Confirming which counters and counter sets a GPU supports`](confirming-which-counters-and-counter-sets-a-gpu-supports.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounter/name)*