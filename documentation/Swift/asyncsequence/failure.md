# Failure

**Framework**: Swift  
**Kind**: associatedtype  
**Required**: Yes

The type of errors produced when iteration over the sequence fails.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
associatedtype Failure = any Error where Self.Failure == Self.AsyncIterator.Failure
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncsequence/failure)*