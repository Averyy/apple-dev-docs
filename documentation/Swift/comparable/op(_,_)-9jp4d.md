# <(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator  
**Required**: Yes

Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

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
static func < (lhs: borrowing Self, rhs: borrowing Self) -> Bool
```

#### Discussion

This function is the only requirement of the `Comparable` protocol. The remainder of the relational operator functions are implemented by the standard library for any type that conforms to `Comparable`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## Default Implementations

### Comparable Implementations
- [static func < (Self, Self) -> Bool](./op%28_,_%29-2qz41.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func < (Self, Self) -> Bool](./op%28_,_%29-8kchc.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func < <RHS>(Self, RHS) -> Bool](./op%28_,_%29-8ogs5.md)
- [static func < <Other>(Self, Other) -> Bool](./op%28_,_%29-z2os.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/comparable/_(_:_:)-9jp4d)*