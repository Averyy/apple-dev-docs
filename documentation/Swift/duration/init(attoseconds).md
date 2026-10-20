# init(attoseconds:)

**Framework**: Swift  
**Kind**: init

Construct a `Duration` from the given number of attoseconds.

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
init(attoseconds: Int128)
```

#### Discussion

This directly constructs a `Duration` from the given number of attoseconds.

```swift
let d = Duration(attoseconds: 1_000_000_000_000_000_000)
print(d) // 1.0 seconds
```

## Parameters

- `attoseconds`: The total duration expressed in attoseconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/init(attoseconds:))*