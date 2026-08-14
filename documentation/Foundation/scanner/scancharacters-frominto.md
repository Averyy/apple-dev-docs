# scanCharacters(from:into:)

**Framework**: Foundation  
**Kind**: method

Scans the string as long as characters from a given character set are encountered, accumulating characters into a string that’s returned by reference.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func scanCharacters(from set: CharacterSet, into result: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver scanned any characters, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Invoke this method with `NULL` as `stringValue` to simply scan past a given set of characters.

## Parameters

- `set`: The set of characters to scan.
- `result`: Upon return, contains the characters scanned.

## See Also

- [func scanUpToCharacters(from: CharacterSet, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scanuptocharacters(from:into:).md)
  Scans the string until a character from a given character set is encountered, accumulating characters into a string that’s returned by reference.
- [func scanString(String, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scanstring(_:into:).md)
  Scans a given string, returning an equivalent string object by reference if a match is found.
- [func scanUpTo(String, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scanupto(_:into:).md)
  Scans the string until a given string is encountered, accumulating characters into a string that’s returned by reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scancharacters(from:into:))*