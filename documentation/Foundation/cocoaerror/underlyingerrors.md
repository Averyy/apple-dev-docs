# underlyingErrors

**Framework**: Foundation  
**Kind**: property

A list of underlying errors, if any. It includes the values of both NSUnderlyingErrorKey and NSMultipleUnderlyingErrorsKey. If there are no underlying errors, returns an empty array.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```swift
var underlyingErrors: [any Error] { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/cocoaerror/underlyingerrors)*