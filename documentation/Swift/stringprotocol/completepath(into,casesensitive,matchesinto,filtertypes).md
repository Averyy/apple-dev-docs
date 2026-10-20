# completePath(into:caseSensitive:matchesInto:filterTypes:)

**Framework**: Swift  
**Kind**: method

Interprets the string as a path in the file system and attempts to perform filename completion, returning a numeric value that indicates whether a match was possible, and by reference the longest path that matches the string.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func completePath(into outputName: UnsafeMutablePointer<String>? = nil, caseSensitive: Bool, matchesInto outputArray: UnsafeMutablePointer<[String]>? = nil, filterTypes: [String]? = nil) -> Int
```

#### Return Value

The actual number of matching paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/completepath(into:casesensitive:matchesinto:filtertypes:))*