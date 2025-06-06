# SecKeyGeneratePairAsync(_:_:_:)

**Framework**: Security  
**Kind**: func

Generates a public/private key pair.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecKeyGeneratePairAsync(_ parameters: CFDictionary, _ deliveryQueue: dispatch_queue_t, _ result: @escaping SecKeyGeneratePairBlock)
```

## Parameters

- `parameters`: These default values can be overridden by adding a value for the associated key in the parameter dictionary.
- `deliveryQueue`: The dispatch queue on which the result block should be scheduled.
- `result`: A block of type   that gets called with the result upon completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeygeneratepairasync(_:_:_:))*