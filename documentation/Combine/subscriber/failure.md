# Failure

**Framework**: Combine  
**Kind**: associatedtype  
**Required**: Yes

The kind of errors this subscriber might receive.

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
associatedtype Failure : Error
```

#### Discussion

Use `Never` if this `Subscriber` cannot receive errors.

## See Also

- [associatedtype Input](subscriber/input.md)
  The kind of values this subscriber receives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscriber/failure)*