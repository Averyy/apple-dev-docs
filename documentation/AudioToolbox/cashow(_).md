# CAShow(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Prints the internal state of an object to `stdio`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CAShow(_ inObject: UnsafeMutableRawPointer)
```

```c
extern void CAShow(void *inObject);
```

## Discussion

## Parameters

- `inObject`: The Core Audio object whose internal state you want to print.

## See Also

### Audio Toolbox Debugging Functions
- [func CAShowFile(UnsafeMutableRawPointer, UnsafeMutablePointer<FILE>)](./cashowfile%28_,_%29.md)
  Prints the internal state of an object to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/cashow(_:))*