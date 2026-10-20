# SecKeyGeneratePairBlock

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

A block called with the results of a call to [`SecKeyGeneratePairAsync(_:_:_:)`](./seckeygeneratepairasync%28_,_,_%29.md).

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias SecKeyGeneratePairBlock = (SecKey, SecKey, CFError) -> Void
```

```c
typedef void (^)(struct __SecKey *, struct __SecKey *, struct __CFError *) SecKeyGeneratePairBlock;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeygeneratepairblock)*