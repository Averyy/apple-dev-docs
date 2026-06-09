# withBytes(_:)

**Framework**: Foundation  
**Kind**: method

Calls the given closure with the contents of underlying storage.

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
func withBytes<R, E>(_ body: (RawSpan) throws(E) -> R) throws(E) -> R where E : Error
```

#### Discussion

> **Note**: Calling `withBytes` multiple times does not guarantee that the same span will be passed in every time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/contiguousbytes/withbytes(_:))*