# candidates(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns an array of candidates.

**Availability**:
- macOS ?+

## Declaration

```swift
func candidates(_ sender: Any!) -> [Any]!
```

#### Return Value

An array of candidates. The returned array should be an autoreleased object.

#### Discussion

An input method should look up its currently composed string and return a list of candidate strings that the composed string might map to.

## Parameters

- `sender`: The client object requesting the candidates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/candidates(_:))*