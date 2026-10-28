# max(_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Type Method

Creates a demand for the given maximum number of elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func max(_ value: Int) -> Subscribers.Demand
```

## Discussion

The publisher is free to send fewer than the requested maximum number of elements.

## Parameters

- `value`: The maximum number of elements. Providing a negative value for this parameter results in a fatal error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand/max(_:))*