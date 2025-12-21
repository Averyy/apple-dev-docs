# didChange()

**Framework**: Objective-C Runtime  
**Kind**: method

Returns a publisher that emits values when a KVO-compliant property changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func didChange() -> Publishers.Map<NSObject.KeyValueObservingPublisher<Subject, Value>, Void>
```

#### Return Value

A key-value observing publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/didchange())*