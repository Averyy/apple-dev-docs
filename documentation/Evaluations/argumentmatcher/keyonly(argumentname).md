# ArgumentMatcher.keyOnly(argumentName:)

**Framework**: Evaluations  
**Kind**: case  
**Role**: Case

A value that indicates that the argument must be present with this key and no specific value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
case keyOnly(argumentName: String)
```

## Parameters

- `argumentName`: The name of the argument that must be present.

## See Also

### Exact matching
- [case exact(argumentName: String, value: ArgumentValue)](./exact%28argumentname,value%29.md)
  A value that indicates that the argument must be present with this exact key and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/keyonly(argumentname:))*