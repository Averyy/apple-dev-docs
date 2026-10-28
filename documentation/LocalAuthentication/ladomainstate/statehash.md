# stateHash

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Instance Property

Contains combined state hash data for biometry and companion state hashes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var stateHash: Data? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSData * stateHash;
```

## Discussion

```
     the list of paired companions has not changed.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/ladomainstate/statehash)*