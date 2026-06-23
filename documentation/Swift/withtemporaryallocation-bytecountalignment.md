# withTemporaryAllocation(byteCount:alignment:_:)

**Framework**: Swift  
**Kind**: func

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
func withTemporaryAllocation<R, E>(byteCount: Int, alignment: Int, _ body: @_lifetime(0: copy 0) (inout OutputRawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withtemporaryallocation(bytecount:alignment:_:))*