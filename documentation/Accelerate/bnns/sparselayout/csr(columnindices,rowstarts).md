# BNNS.SparseLayout.csr(columnIndices:rowStarts:)

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

The compressed sparse row (CSR) format.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
case csr(columnIndices: BNNSNDArrayDescriptor, rowStarts: BNNSNDArrayDescriptor)
```

## See Also

### Enumeration Cases
- [case coo(indices: BNNSNDArrayDescriptor)](./coo%28indices%29.md)
  The sparse coordinate list (COO) format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/sparselayout/csr(columnindices:rowstarts:))*