# CFCharacterSetIsLongCharacterMember(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Reports whether or not a given UTF-32 character is in a character set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFCharacterSetIsLongCharacterMember(_ theSet: CFCharacterSet!, _ theChar: UTF32Char) -> Bool
```

#### Return Value

`true` if `theSet` contains `theChar`, otherwise `false`.

## Parameters

- `theSet`: The character set to examine.
- `theChar`: The UTF-32 character for which to test against the character set.

## See Also

- [func CFCharacterSetCreateBitmapRepresentation(CFAllocator!, CFCharacterSet!) -> CFData!](cfcharactersetcreatebitmaprepresentation(_:_:).md)
  Creates a new immutable data with the bitmap representation from the given character set.
- [func CFCharacterSetHasMemberInPlane(CFCharacterSet!, CFIndex) -> Bool](cfcharactersethasmemberinplane(_:_:).md)
  Reports whether or not a character set contains at least one member character in the specified plane.
- [func CFCharacterSetIsCharacterMember(CFCharacterSet!, UniChar) -> Bool](cfcharactersetischaractermember(_:_:).md)
  Reports whether or not a given Unicode character is in a character set.
- [func CFCharacterSetIsSupersetOfSet(CFCharacterSet!, CFCharacterSet!) -> Bool](cfcharactersetissupersetofset(_:_:).md)
  Reports whether or not a character set is a superset of another set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetislongcharactermember(_:_:))*