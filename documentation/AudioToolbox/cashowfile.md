# CAShowFile(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Prints the internal state of an object to a file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CAShowFile(_ inObject: UnsafeMutableRawPointer, _ inFile: UnsafeMutablePointer<FILE>)
```

#### Discussion

## Parameters

- `inObject`: The Core Audio object whose internal state you want to print.
- `inFile`: The file you want to print object state information to

## See Also

- [func CAShow(UnsafeMutableRawPointer)](cashow(_:).md)
  Prints the internal state of an object to `stdio`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/cashowfile(_:_:))*