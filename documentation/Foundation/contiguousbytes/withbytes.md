# withBytes(_:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Calls the given closure with the contents of underlying storage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func withBytes<R, E>(_ body: (RawSpan) throws(E) -> R) throws(E) -> R where E : Error
```

#### Discussion

> **Note**: Calling `withBytes` multiple times does not guarantee that the same span will be passed in every time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/contiguousbytes/withbytes(_:))*