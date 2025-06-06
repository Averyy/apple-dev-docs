# lexicallyNormalized()

**Framework**: System  
**Kind**: method

Returns a copy of `self` in lexical-normal form, that is `.` and `..` components have been collapsed lexically (i.e. without following symlinks). See `lexicallyNormalize`

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func lexicallyNormalized() -> FilePath
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/lexicallynormalized())*