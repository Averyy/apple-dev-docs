# withTemporaryAllocation(of:capacity:_:)

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
func withTemporaryAllocation<T, R, E>(of type: T.Type, capacity: Int, _ body: @_lifetime(0: copy 0) (inout OutputSpan<T>) throws(E) -> R) throws(E) -> R where E : Error, T : ~Copyable, R : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withtemporaryallocation(of:capacity:_:))*