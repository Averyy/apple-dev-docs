# scanString(_:into:)

**Framework**: Foundation  
**Kind**: method

Scans a given string, returning an equivalent string object by reference if a match is found.

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
func scanString(_ string: String, into result: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `string` matches the characters at the scan location, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If `string` is present at the current scan location, then the current scan location is advanced to after the string; otherwise the scan location does not change.

Invoke this method with `NULL` as `stringValue` to simply scan past a given string.

## Parameters

- `string`: The string for which to scan at the current scan location.
- `result`: Upon return, if the receiver contains a string equivalent to   at the current scan location, contains a string equivalent to  .

## See Also

- [func scanCharacters(from: CharacterSet, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scancharacters(from:into:).md)
  Scans the string as long as characters from a given character set are encountered, accumulating characters into a string that’s returned by reference.
- [func scanUpToCharacters(from: CharacterSet, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scanuptocharacters(from:into:).md)
  Scans the string until a character from a given character set is encountered, accumulating characters into a string that’s returned by reference.
- [func scanUpTo(String, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scanupto(_:into:).md)
  Scans the string until a given string is encountered, accumulating characters into a string that’s returned by reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scanstring(_:into:))*