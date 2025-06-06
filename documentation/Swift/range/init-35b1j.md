# init(_:)

**Framework**: Swift  
**Kind**: init

Now that Range is conditionally a collection when Bound: Strideable, CountableRange is no longer needed. This is a deprecated initializer for any remaining uses of Range(countableRange).

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(_ other: Range<Bound>)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/init(_:)-35b1j)*