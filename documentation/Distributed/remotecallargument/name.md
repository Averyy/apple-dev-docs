# name

**Framework**: Distributed  
**Kind**: property

The internal name of parameter this argument is accessible as in the function body. It is not part of the functions API and may change without breaking the target identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
let name: String
```

#### Discussion

If the method did not declare an explicit `label`, it is used as the `effectiveLabel`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/remotecallargument/name)*