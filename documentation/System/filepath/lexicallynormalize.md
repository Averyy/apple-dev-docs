# lexicallyNormalize()

**Framework**: System  
**Kind**: method

Collapse `.` and `..` components lexically (i.e. without following symlinks).

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
mutating func lexicallyNormalize()
```

#### Discussion

Examples:

- `/usr/./local/bin/.. => /usr/local`
- `/../usr/local/bin   => /usr/local/bin`
- `../usr/local/../bin => ../usr/bin`


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/lexicallynormalize())*