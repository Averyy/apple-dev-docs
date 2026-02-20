# .|=(_:_:)

**Framework**: Swift  
**Kind**: op

Replaces `a` with the pointwise logical disjunction of `a` and `b`.

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
static func .|= (a: inout SIMDMask<Storage>, b: SIMDMask<Storage>)
```

#### Discussion

Equivalent to:

```swift
for i in a.indices {
  a[i] = a[i] || b[i]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdmask/'._=(_:_:)-9cexc)*