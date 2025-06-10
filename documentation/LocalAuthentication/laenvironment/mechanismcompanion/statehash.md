# stateHash

**Framework**: Local Authentication  
**Kind**: property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var stateHash: Data? { get }
```

#### Discussion

If no companion are paired for this companion type, @c stateHash property is @c nil. If at least one companion is paired for this companion type, @c stateHash is not @c nil and it changes whenever the set of paired companions of this type is changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/mechanismcompanion/statehash)*