# init(unsafeElements:)

**Framework**: Swift  
**Kind**: init

Unsafely convert a typed span to a raw span.

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
init<Element>(unsafeElements elements: consuming MutableSpan<Element>)
```

#### Discussion

Creates a `MutableRawSpan` over the memory represented by a `MutableSpan<Element>`.

## Parameters

- `elements`: An existing `MutableSpan<Element>`, from which this `MutableRawSpan` will inherit its lifetime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/init(unsafeelements:))*