# stateHash

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Instance Property

Contains state hash data for the available biometry type. Returns `nil` if no biometry entities are enrolled.

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

#### Discussion

If biometric database was modified (fingers, faces were removed or added), `stateHash` data will change. Nature of such database changes cannot be determined but comparing data of `stateHash` after different evaluatePolicy calls will reveal the fact database was changed between the calls.

```
     the state of biometry has not changed.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/ladomainstatebiometry/statehash)*